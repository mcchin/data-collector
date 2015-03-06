from flask import Flask
from flask.ext import restful

class Report(restful.Resource):
    def get(self):
        return {'show': 'results'}
