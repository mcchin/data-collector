from flask import Flask
from flask.ext import restful

class Scrape(restful.Resource):
    def get(self):
        return {'scrape': 'twitter'}
