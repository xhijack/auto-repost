# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Oct 24, 2015 6:50:56 PM$"

import os.path
import urllib

from instagram.client import InstagramAPI

from config import *
from choice import *
from igpost import InstagramSession


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
        return os.path.isfile(IMAGES_PATH + filename)

    def post(self):
        for source in self.whitelist:
            medias = self.instagram.user_recent_media(user_id = source)[0][0]
            image_url = medias.images['standard_resolution'].url
            filename = medias.id + '.jpg'
            if self.check_file(filename):
                self.download(image_url, filename)

                media_id = self.insta_post.upload_photo(filename)
                if media_id is not None:
                    self.insta_post.configure_photo(media_id, medias.caption.text)
                else:
                    print "Failed"

class AutoPost(AutoPostBase):

    instagram = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)
    insta_post = InstagramSession('wikislam','master88')
    whitelist = WHITELIST


if __name__ == '__main__':
    print "Start Re Posting"
    ap = AutoPost()
    ap.post()