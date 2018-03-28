"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
import json
from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.db_handler import *


@rest_resource
class ResourceOne(BaseResource):
    """ /api/resource/one """
    endpoints = ['/register', '/login', '/logout', '/tweet', '/follow',
                 '/unfollow', '/like', '/retweet', '/hashtags',
                 '/hashtags/search', '/hashtags/most', '/logs', '/home']

    def get(self):
        url = str(request.path)
        url = url.split('api')[1]
        if url == self.endpoints[2]:
            print(request.args)
            username = request.args.get('username')
            password = request.args.get('password')
            if username == 'soosk' and password == 'piaz':
                return {'status': 'OK'}
            return {'status': 'Wrong'}
        elif url == self.endpoints[1]:
            return {'Error': 'Wrong Request'}
        else:
            return {'Error': 404}

    def post(self):
        url = str(request.path)
        url = url.split('api')[1]
        if url == self.endpoints[2]:
            keys = list(request.form.keys())[0]
            data = json.loads(keys)
            print(data)
            print("asdfgh")
            username = data['username']
            password = data['password']
            if username == 'soosk' and password == 'piaz':
                return {'status': 'OK'}
            return {'status': 'Wrong'}
        elif url == self.endpoints[1]:
            return user_list()
        else:
            return {'Error': 404}




@rest_resource
class SecureResourceOne(SecureResource):
    """ /api/resource/two """
    endpoints = ['/resource/two/<string:resource_id>', '/te']

    def get(self, resource_id):
        time.sleep(1)
        return {'name': 'Resource Two', 'data': resource_id}

