"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.data_handler import *

@rest_resource
class ResourceOne(BaseResource):
    """ /api/resource/one """
    endpoints = ['/resource/one', '/users']

    def get(self):
        time.sleep(1)
        url = str(request.path)
        url = url.split('api')[1]
        if url == self.endpoints[0]:
            return {'name': 'Resource One', 'data': True}
        elif url == self.endpoints[1]:
            return {'Error': 'Wrong Request'}
        else:
            return {'Error': 404}

    def post(self):
        url = str(request.path)
        url = url.split('api')[1]
        if url == self.endpoints[0]:
            return {'Error': 'Wrong Request'}
        elif url == self.endpoints[1]:
            return usrlist()
        else:
            return {'Error': 404}




@rest_resource
class SecureResourceOne(SecureResource):
    """ /api/resource/two """
    endpoints = ['/resource/two/<string:resource_id>']

    def get(self, resource_id):
        time.sleep(1)
        return {'name': 'Resource Two', 'data': resource_id}

