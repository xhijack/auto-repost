# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Oct 18, 2015 12:07:33 PM$"

import requests

class UploadImage(object):
    SERVICE_URL = 'http://imgsafe.org/upload'

    def __init__(self, files):
        self.files = files

    def __repr__(self):
        return self.files

    def upload(self):
        return requests.post(self.SERVICE_URL, self.files)
