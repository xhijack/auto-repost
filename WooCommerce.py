import sys

import csv

reload(sys);
sys.setdefaultencoding("utf8")

from woocommerce import API
url = 'http://addavii.com'
consumer_key = 'ck_87f1dd1757cd6a7af3fb53b034b98f7b289cc3d9'
consumer_secret = 'cs_3f5c8e70f1fee8fd2845e43a2efc4e7d2e9af03f'
wcapi = API(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret)

class WooCommerce(object):
	
    def __init__(self, url, consumer_key, consumer_secret):
        self.wcapi = API(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret)

    def get_api(self):
        return self.wcapi

    def open_products(self):
        result = self.wcapi.get('products?filter[limit]=1000')
        if result.status_code == 200:
            return result.json()['products']

    def get_products(self, q, limit=1000):
        result = self.wcapi.get('products?filter[q]={q}&filter[limit]={limit}'.format(q=q, limit=1000))
        if result.status_code == 200:
            return result.json()['products']

    def post_product(self, data):
        if len(self.get_products(q=data['product']['title'])) == 0:
            result = self.wcapi.post('products', data=data)
            if result.statu_code == 200:
                return result.json()
        else:
            return "The Products is already exists"

    def get_tags(self):
        result = self.wcapi.get('products/tags')
        if result.status_code == 200:
            return result.json()['product_tags']

    def get_categories(self):
        result = self.wcapi.get('products/categories')
        if result.status_code == 200:
            return result.json()['product_categories']
        
    def save(self, filename, type='csv'):
        if type == 'csv':
            products = self.get_products()
            keys = products[0].keys()
            with open(filename, 'wb') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(products)


class Product(object):

    name = 'product'

    def __init__(self, title, type=None, regular_price=None, description=None, short_description=None, categories=None, images=[], tags=[]):
        self.title = title
        self.type = type or 'simple'
        self.regular_price = regular_price
        self.description = description
        self.short_description  = short_description
        self.categories = categories
        self.images = images
        self.tags = tags

    def __repr__(self):
        return "[%s]" % self.title

    def response(self):
        return {
            self.name:self.__dict__
        }
        
if __name__ == '__main__':
    wo = WooCommerce(url, consumer_key, consumer_secret)
    images = [
        {
            "src": "http://s12.postimg.org/l2hsfcm2l/wall.jpg",
            "position": 0
        },
        {
            "src": "http://s12.postimg.org/l2hsfcm2l/wall.jpg",
            "position": 1
        }
    ]
    product = Product('New Salsabila', regular_price="49000", description='New prdocut from addavii', 
                      short_description="Coba deh", categories=[116], images=images, tags=[31])
    result = wo.post_product(product.response())
    if result:
        print result