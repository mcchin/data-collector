import werkzeug.exceptions as ex
from flask import Flask, abort

class ApiException(ex.HTTPException):
    code = 503
    #if ('message' in kwargs):
    description = '<p>Cannot process API</p>' 
    #else:
    #    description = '<p>'+kwargs['message']+'</p>' 

