# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Oct 18, 2015 4:14:21 PM$"


from gi.overrides.Gtk import __init__
from instagram.client import InstagramAPI
from WooCommerce import Product

ACCESS_TOKEN = '34008092.6c7aa75.fc1ff84034bd4f61b3b2b1bc33285a1d'
CLIENT_SECRET = 'b8f0d7112d3b40bd9927cfd28bf2a422'
ACCESS_TOKEN = '1552719530.6c7aa75.de55f341beff4eaca7d97de4b260bb79'
#client_id = '6c7aa750ffee4871b9d57e94daafa03e'
api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)

# https://instagram.com/oauth/authorize/?client_id=6c7aa750ffee4871b9d57e94daafa03e&redirect_uri=http://sopwer.net&response_type=token

class Attributes(object):
    caption
    tags
    images


class IG(object):

    def __init__(self, access_token=None, client_id=None, client_secret=None, key_tag=None):
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.api = InstagramAPI(access_token=self.access_token, client_secret=self.client_secret)
        self.key_tag = key_tag or "productaddavii"

class WooPost(IG):

    def parser(self, media):

        title = media_string[0]
        price = media_string[0]
        

    def scrape(self):
        medias = self.api.user_media_feed()
        for media in medias[0]:
            tags = [tag.name for tag in media.tags]
            if self.key_tag in tags:
                media_string = media.caption.split('.')
                product = Product(media_string[0], regular_price=media_string[1], description=media.caption,
                      short_description=media.caption, categories=[116], images=images, tags=[31])