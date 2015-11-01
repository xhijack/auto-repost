import random
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Oct 24, 2015 6:50:56 PM$"

from auto_post import InstagramSession, InstagramAPI, AutoPostBase, ACCESS_TOKEN_WIKI, CLIENT_SECRET, WHITELIST

class AutoPost(AutoPostBase):

    instagram = InstagramAPI(access_token=ACCESS_TOKEN_WIKI, client_secret=CLIENT_SECRET)
    insta_post = InstagramSession('wikislam','wikislam88')
    whitelist = WHITELIST


if __name__ == '__main__':
    print "Start Re Posting"
    ap = AutoPost()
    print "+++ MEDIA +++"
    ap.get_media_from_choice()
    print "+++ LIKED +++"
    ap.get_media_from_liked()
