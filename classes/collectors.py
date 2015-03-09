from TwitterSearch import *

from classes.config import Config

class Collector():
    def __init__(self, source=None):
        self.valid_sources = ['twitter']
        self.default_lang = 'en'

        if (source):
            self.data_source = source 
        else:     
            self.data_source = self.valid_sources[0] 

        self.bootstrap()

    def bootstrap(self):
        if self.data_source.lower() in self.valid_sources:
            self.engine = globals()[self.data_source.title()]()
        else:
            abort(500)

    def get(self, keyword=None):
        if (keyword):
            self.engine.get(keyword)

        return {'show': 'results'}

class Twitter():
    def __init__(self):
        print "Init twitter"

    def get(self, keyword=None, lang="en"):
        if (keyword):
            try:
                tso = TwitterSearchOrder()
                tso.set_keywords([keyword])
                tso.set_language(lang)  
                tso.set_include_entities(False) 

                ts = TwitterSearch(
                    Config.settings['twitter']['consumer_key'],
                    Config.settings['twitter']['consumer_secret'],
                    Config.settings['twitter']['access_token'],
                    Config.settings['twitter']['access_token_secret']
                )

                for tweet in ts.search_tweets_iterable(tso):
                    print tweet
                    #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            except TwitterSearchException as e:
                abort(500) 

        return False
