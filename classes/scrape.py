from flask import Flask, Response, abort
from flask.ext import restful

from collectors import Collector
from storage import Storage

class Scrape(restful.Resource):
    def get(self, keyword, source=None):
        if (not source):
            source = 'twitter'

        if (not keyword):
            return {'error': 'twitter'}
        else:
            self.collector = Collector(source)
            self.collector.get(keyword)    
            return {'scrape': 'twitter - keyword:' + keyword}
