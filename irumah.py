# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ramdani"
__email__="ramdani@sopwer.net"
__date__ ="$Nov 1, 2015 12:28:40 PM$"

from auto_post import InstagramSession, InstagramAPI, AutoPostBase, ACCESS_TOKEN_WIKI, CLIENT_SECRET, WHITELIST

a = ['RUMAHINSPIRASI','IARCHITECTURES','DESIGN_INTERIOR_HOMES','BOSS_HOMES','MYEXTERIOR','LUXURY_LISTINGS',
'INTERIORSELFIE','UBERKREATIVE','DESIGNANDLIVE','ARCHITECTUREDOSE','IG_INTERIORS','ARCHITECTURENOW','MYHOUSEIDEA',
'ARCHDAILY','MYINTERIOR','INANDOUTDECOR','D.SIGNERS','ADESIGNERSMIND','HOMEADORE','ARCHITECTURE.AK'
]

class AutoPost(AutoPostBase):

    instagram = InstagramAPI(access_token=ACCESS_TOKEN_WIKI, client_secret=CLIENT_SECRET)
    insta_post = InstagramSession('irumah','master')
    whitelist = WHITELIST

    def pull_all(self):
        for user in WHITELIST:
            medias=self.instagram.user_recent_media(user)
            if medias:
                medias = medias[0]
                for media in medias:
                    self.post(media)
        
if __name__ == '__main__':
    print "Start Re Posting"
    ap = AutoPost()
    print "+++ MEDIA +++"
    ap.pull_all()
