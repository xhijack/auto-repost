import random
from insta_gram import InstagramSession
from instapy import Instapy
from instagram import InstagramAPI

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Nov 1, 2015 13:50:18 PM$"


ACCESS_TOKEN = '2269390601.6c7aa75.adf9d994d2284a9dbc86ef019df0451e'
CLIENT_SECRET = 'b8f0d7112d3b40bd9927cfd28bf2a422'
USERNAME = 'muslimahkepo'
PASSWORD = 'master'

USERS = ['RUMAHDAKWAH', 'BERTAHAJUDLAH', 'KANGABAY_', 'INDONESIAMENUTUPAURAT', 'FELIXSIAUW',
         'NIKAHBAROKAH', 'MUDA_BERDAKWAH', 'MENIKAHBAHAGIA', 'JODOH.SEJATI', 'DAKWAHJOMBLO', 'CINTAMULIA',
         'SAHABATMUSLIMAH', 'USAHAIMANAMAL', 'MUSLIMAH_TALK', 'muslimahcorner',
         'ISTRIKUBIDADARIKU', 'INSPIRING.MUSLIMAH', 'MUSLIMAHORID', 'SALIMAFILLAH']


class MuslimahGalau(Instapy):

    instagram = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)
    insta_post = InstagramSession(username=USERNAME, password=PASSWORD, guid='3efc0996-85bd-11e5-857d-74de2b6b05c3',
                                  device_id='android-3efc0996-85bd-11e5-857d-74de2b6b05c3',
                                  user_agent= 'Instagram 4.2.2 Android (10/1.5.2; 120; 480x800; samsung; GT-N7000; GT-N7000; smdkc210; en_US)')
    user_followed = USERS
    tags = ['#muslimahgalau', '#muslimah', '#galau', '#akhowat', '#akhwat', '#tausiyah']
    IMAGES_PATH = '/home/ramdani/projects/auto-repost/muslimah_images/'

if __name__ == '__main__':
    print "Start Reposting"
    mg = MuslimahGalau(waiting_time=random.randint(100, 300))
    mg.post_media_from_choice()
    mg.post_media_from_liked()
    print "Finished"