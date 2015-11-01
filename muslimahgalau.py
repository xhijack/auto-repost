import random
from insta_gram import InstagramSession
from instapy import Instapy
from instagram import InstagramAPI

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Nov 1, 2015 13:50:18 PM$"


ACCESS_TOKEN = '2260316470.6c7aa75.1b8a372b7cda43e29370097445ac31f3'
CLIENT_SECRET = 'b8f0d7112d3b40bd9927cfd28bf2a422'
USERNAME = 'muslimahgalau'
PASSWORD = 'master'

USERS = ['RUMAHDAKWAH', 'BERTAHAJUDLAH', 'KANGABAY_', 'INDONESIAMENUTUPAURAT', 'FELIXSIAUW',
         'NIKAHBAROKAH', 'MUDA_BERDAKWAH', 'MENIKAHBAHAGIA', 'JODOH.SEJATI', 'DAKWAHJOMBLO', 'CINTAMULIA',
         'SUAMI.ISTERI.BAHAGIA', 'SAHABATMUSLIMAH', 'USAHAIMANAMAL', 'MUSLIMAH_TALK', 'muslimahcorner',
         'ISTRIKUBIDADARIKU', 'SAHABAT.MUSLIMAH', 'INSPIRING.MUSLIMAH', 'MUSLIMAHORID', 'SALIMAFILLAH']


class MuslimahGalau(Instapy):

    instagram = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)
    insta_post = InstagramSession(username=USERNAME, password=PASSWORD)
    user_followed = USERS
    tags = ['#muslimahgalau', '#muslimah', '#galau', '#akhowat']

if __name__ == '__main__':
    print "Start Reposting"
    mg = MuslimahGalau(waiting_time=random.randint(10, 20))
    mg.post_media_from_choice()
    print "Finished"