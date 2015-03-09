import os
import json

from flask import abort

class Config():
    def __init__(self, config_file=None):
        self.config_file = os.path.dirname(__file__) + '/../cfg/config.json'
        if config_file is not None:
            self.config_file = os.path.dirname(__file__) + '/../cfg/' + config_file
    def load(self):
        txt = ""
        line = ""
        if os.path.isfile(self.config_file):
            with open(self.config_file) as fin:
                for line in fin:
                    txt += line
            try:
                Config.settings = json.loads(txt) 
                return True 
            except:
                abort(500)

        return False 
