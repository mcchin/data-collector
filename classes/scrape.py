import tweepy

from flask import Flask
from flask.ext import restful

class Scrape(restful.Resource):
    def __init__(self):
        #self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        #self.auth.set_access_token(access_token, access_token_secret)
        print "init twitter"
    def get(self, keyword):
        if (not keyword):
            return {'error': 'twitter'}
        else:
            return {'scrape': 'twitter - keyword:' + keyword}
