import json

from flask import Flask
from flask.ext import restful

from classes.scrape import Scrape
from classes.report import Report

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/')

api.add_resource(Scrape, '/scrape/<string:keyword>', '/scrape/<string:keyword>/<string:source>')
api.add_resource(Report, '/report', '/report/<string:keyword>')

if __name__ == '__main__':
    app.run(debug=True)
