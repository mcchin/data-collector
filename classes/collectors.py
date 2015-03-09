import tweepy

class Collector:
    def __init__(self, source=None):
        self.valid_sources = ['twitter']
        if (source):
            self.data_source = source 
        else:     
            self.data_source = self.valid_sources[0] 
        self.bootstrap()
    def bootstrap(self):
        print "bootstrap"
        self.engine = Twitter
    def get(self, keyword=None):
        if (keyword):
            print "getting"

        return {'show': 'results'}

class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret) 
    def test(self):
        print "testing"
