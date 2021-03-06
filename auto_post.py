# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Nov 1, 2015 12:30:18 PM$"

import os.path
import os
import urllib
import time
import random

from instagram.client import InstagramAPI

from config import *
from choice import *
from insta_gram import InstagramSession

class AutoPostBase(object):

    instagram = None
    insta_post = None
    whitelist = None

    def __init__(self):
        pass

    @classmethod
    def download(cls, source, filename):
        urllib.urlretrieve(source, filename)

    def check_file(self, filename):
        return os.path.isfile(filename)

    def get_media_from_liked(self):
        """
            Get list of images where user like some post
        """
        images = []
        medias = self.instagram.user_liked_media()[0]
        for media in medias:
            self.post(media)

    def get_media_from_choice(self):
        for source in self.whitelist:
            medias = self.instagram.user_recent_media(user_id = source)[0][0]
            self.post(medias)

    def get_user_id(self, username):
        return self.instagram.user_search(username).id

    def post(self, media):
        image_url = media.images['standard_resolution'].url
        filename = image_url.split('/')[-1:][0] # media.id + '.jpg'
        target_url = IMAGES_PATH + filename
        if self.check_file(target_url) is False:
            WAITING_TIME = random.randint(10,180)
	    print "Waiting Time", WAITING_TIME
	    time.sleep(WAITING_TIME)

	    print '-->Prepare Upload/Download', image_url
            print "---> Downloading"
            self.download(image_url, target_url)

            caption = ''
            if media.caption == None:
                caption = ''
	    else:
		caption = media.caption.text


            caption = caption + ' repost @' + media.user.username + ' #wikislam'
            print "--> Uploading"
            result = self.insta_post.upload_photo(target_url, caption)
	    error = result.get('error_title',None)
	    if error == 'media_not_found':
		os.remove(target_url)
            print result
        else:
            print "File is exists"

