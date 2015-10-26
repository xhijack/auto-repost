# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Oct 18, 2015 4:14:21 PM$"


from instagram.client import InstagramAPI
from WooCommerce import *

ACCESS_TOKEN = '34008092.6c7aa75.fc1ff84034bd4f61b3b2b1bc33285a1d'
CLIENT_SECRET = 'b8f0d7112d3b40bd9927cfd28bf2a422'
ACCESS_TOKEN = '1552719530.6c7aa75.de55f341beff4eaca7d97de4b260bb79'
#client_id = '6c7aa750ffee4871b9d57e94daafa03e'
api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)

# https://instagram.com/oauth/authorize/?client_id=6c7aa750ffee4871b9d57e94daafa03e&redirect_uri=http://sopwer.net&response_type=token

class ItemIg(dict):

    def __init__(self, title=None, price=None, description=None, short_description=None,
    categories=[], images=[], tags=[]):
        self.title = title
        self.price = price
        self.description = description
        self.short_description = short_description
        self.categories = categories
        self.images = images
        self.tags = tags

    def __repr__(self):
        return "Title : {0}".format(self.title)

class IG(object):
    """
        This class for handling Instagram API
    """

    def __init__(self, access_token=None, client_id=None, client_secret=None, key_tag=None, seperator=None):
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.api = InstagramAPI(access_token=self.access_token, client_secret=self.client_secret)
        self.key_tag = key_tag or "productaddavii"
        self.seperator = seperator or '|'

    def get_recent_medias(self):
        return self.api_recent_media()[0]

    def parser(self, media):
        """
            parsing from IG to ItemIg
        """
        media_string = media.caption.text.split(self.seperator)
        title = media_string[0].strip()
        price = media_string[1].strip()
        description = media.caption.text
        short_description = media.caption.text
        categories = [116]
        images = [{
            'src':media.images['standard_resolution'].url,
            'position':0
        },{
            'src':media.images['standard_resolution'].url,
            'position':1
        }]
        tags = [31]
            
        return ItemIg(title, price, description, short_description, categories, images, tags)

    def search_media_by_tag(self):
        result = []
        medias = self.api.tag_recent_media(tag_name=self.key_tag)[0]
        if medias != []:
            for media in medias:
                result.append(self.parser(media))

        return result

    def download(self, with_file=False):
        medias = self.search_media_by_tag()
        objects = []
        for media in medias:
            objects.append(self.parser(media))

        return objects


class WooPost(IG):

    wo = WooCommerce(url, consumer_key, consumer_secret)

    def post(self, item):
        """
            This is for posting to woocommerce
        """
        product = Product(item.title, regular_price=item.price, description=item.description,
                      short_description=item.short_description, categories=item.categories, images=item.images, tags=item.tags)

        return  self.wo.post_product(product.response())

if __name__ == '__main__':
    wp = WooPost(access_token=ACCESS_TOKEN,client_id=CLIENT_SECRET, client_secret=CLIENT_SECRET)
    results = wp.search_media_by_tag()

    for result in results:
        respond = wp.post(result)
        print respond
        