import random
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Oct 24, 2015 6:50:56 PM$"

import os.path
import urllib
import time

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
            self.post()

    def get_media_from_choice(self):
        for source in self.whitelist:
            medias = self.instagram.user_recent_media(user_id = source)[0][0]
            self.post(medias)

    def post(self, media):
        image_url = media.images['standard_resolution'].url
        filename = image_url.split('/')[-1:][0] # media.id + '.jpg'
        target_url = IMAGES_PATH + filename
        if self.check_file(target_url) is False:
            print '-->Prepare Upload/Download', target_url
            time.sleep(random.randint(100,300))
            print "---> Downloading"
            self.download(image_url, target_url)

            caption = ''
            if media.caption == None:
                caption = ''
            caption = caption + ' sumber @' + media.user.username + ' wikislam'
            print "--> Uploading"
            result = self.insta_post.upload_photo(target_url, caption)
            print result
        else:
            print "File is exists"

                
class AutoPost(AutoPostBase):

    instagram = InstagramAPI(access_token=ACCESS_TOKEN_WIKI, client_secret=CLIENT_SECRET)
    insta_post = InstagramSession('wikislam','m@ster88')
    whitelist = WHITELIST


if __name__ == '__main__':
    print "Start Re Posting"
    ap = AutoPost()
    ap.get_media_from_choice()
    ap.get_media_from_liked()
