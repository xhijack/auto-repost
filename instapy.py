import os
import urllib
import time
import random
import logging
from config import *
from abc import ABCMeta

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Nov 1, 2015 12:30:18 PM$"


my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('log_filename.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
my_logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
my_logger.addHandler(ch)


class Instapy(object):
    __metaclass__ = ABCMeta
    instagram = None
    insta_post = None
    tags = None
    end_of_caption = ' repost from @'
    remove_caption = False
    remove_tags = False
    IMAGES_PATH = None

    def __init__(self, waiting_time=None):
        self.waiting_time = waiting_time or random.randint(10, 300)

    @classmethod
    def download(cls, source, filename):
        my_logger.info('download from %s ' % source)
        urllib.urlretrieve(source, filename)

    @classmethod
    def check_file(cls, filename):
        return os.path.isfile(filename)

    def post_media_from_liked(self):
        """
            Post media where user like some posting
        """
        medias = self.instagram.user_liked_media()[0]
        for media in medias:
            self.post(media)

    def post_media_from_choice(self):
        """
            Post media from whitelist. And getting the last of its media
        """

        for user in self.user_followed:
            medias = self.instagram.user_recent_media(user_id=self.get_user_id(user))[0][0]
            my_logger.info('Repost from %s' % user)
            self.post(medias)

    def get_user_id(self, username):
        """
            get user id based on username
        :param `str` username: username from instagram
        :return: user_id
        :rtype: `int`
        """

        user = self.instagram.user_search(username)
        if user:
            return user[0].id
        else:
            return None

    def set_caption(self, caption):
        """
            set caption from media
        :param `instagram.models.Comment` caption: from media
        :return:
        """
        if caption is None:
            caption = ''
        else:
            caption = caption.text

        if self.remove_caption:
            return self.end_of_caption
        else:
            return caption + ' ' + " ".join(self.tags) + self.end_of_caption

    def post(self, media):
        image_url = media.get_standard_resolution_url()
        filename = image_url.split('/')[-1:][0] # media.id + '.jpg'
        target_url = self.IMAGES_PATH + filename

        if self.check_file(target_url) is False:
            if self.waiting_time:
                my_logger.info('Waiting Time : %s' % self.waiting_time)
                time.sleep(self.waiting_time)

            self.download(image_url, target_url)

            caption = self.set_caption(media.caption) + media.user.username
            my_logger.info('upload %s' % target_url)

            result = self.insta_post.upload_photo(target_url, caption)

            # if failed then remove the file
            try:
                error = result.get('error_title', None)
            except ValueError:
                my_logger.debug("What happens %s" % ValueError)

            if error == 'media_not_found':
                os.remove(target_url)
                my_logger.info(result)
            else:
                my_logger.info('success post to instagram')

