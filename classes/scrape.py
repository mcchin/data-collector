from flask import Flask
from flask.ext import restful

from collectors import Collector
from storage import Storage

class Scrape(restful.Resource):
    def __init__(self):
        #self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        #self.auth.set_access_token(access_token, access_token_secret)
        print "init twitter"
    def get(self, keyword, source=None):
        if (not source):
            source = 'twitterx'

        self.collector = Collector(source)
        if (not keyword):
            return {'error': 'twitter'}
        else:
            return {'scrape': 'twitter - keyword:' + keyword}
