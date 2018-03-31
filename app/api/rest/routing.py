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
    endpoints = ['/signup', '/login', '/logout', '/newtweet', '/follow',
                 '/unfollow', '/liketweet', '/retweet', '/searchhashtags',
                 '/tophashtags', '/showlog', '/showhome', '/users', '/hashtag']

    # endpoints = ['/signup', '/login','/logout', '/tweet', '/follow', '/unfollow',
    #              '/like', '/retweet', '/hashtags/search', 'hashtags/top',
    #              '/logs', '/home']

    def get(self):
        url = str(request.path)
        url = url.split('api')[1]
        if url == self.endpoints[0]:
            return
        elif url == self.endpoints[1]:
            return
        elif url == self.endpoints[2]:
            return
        elif url == self.endpoints[3]:
            return
        elif url == self.endpoints[4]:
            return
        elif url == self.endpoints[5]:
            return
        elif url == self.endpoints[6]:
            return
        elif url == self.endpoints[7]:
            return
        elif url == self.endpoints[8]:
            return
        elif url == self.endpoints[9]:
            return
        elif url == self.endpoints[10]:
            return
        elif url == self.endpoints[12]:
            return
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
        if url == self.endpoints[0]:
            return self.__signup(request.form)
        elif url == self.endpoints[1]:
            return self.__login(request.form)
        elif url == self.endpoints[2]:
            return self.__logout(request.form)
        elif url == self.endpoints[3]:
            return self.__tweet(request.form)
        elif url == self.endpoints[4]:
            print(request.form)
            return self.__follow(request.form)
        elif url == self.endpoints[5]:
            return self.__unfollow(request.form)
        elif url == self.endpoints[6]:
            return self.__like(request.form)
        elif url == self.endpoints[7]:
            return self.__rewteet(request.form)
        elif url == self.endpoints[8]:
            return self.__search(request.form)
        elif url == self.endpoints[9]:
            return self.__top()
        elif url == self.endpoints[10]:
            return self.__log(request.form)
        elif url == self.endpoints[11]:
            return self.__home(request.form)
        elif url == self.endpoints[12]:
            return self.__users()
        elif url == self.endpoints[13]:
            return self.__hashtag(request.form)
        else:
            return {'Error': 404}

    @staticmethod
    def __like(args):
        ans = like_post(args['token'], args['postid'])
        return {'ans': ans}

    @staticmethod
    def __top():
        ans = top_hashtags()
        return {'ans': ans}

    @staticmethod
    def __users():
        ans = user_list()
        return {'ans': ans}

    @staticmethod
    def __log(args):
        ans = get_logs(args['token'])
        return {'ans': ans}

    @staticmethod
    def __home(args):
        ans = get_posts_for_home(args['token'])
        return {'ans': ans}

    @staticmethod
    def __search(args):
        ans = hashtag_search(args['hashtag'])
        return {'ans': ans}

    @staticmethod
    def __rewteet(args):
        ans = add_retweet(args['token'], args['postid'])
        return {'ans': ans}

    @staticmethod
    def __unfollow(args):
        ans = unfollow_user(args['token'], args['followingUsername'])
        return {'ans': ans}

    @staticmethod
    def __follow(args):
        ans = follow_user(args['token'], args['followingUsername'])
        return {'ans': ans}

    @staticmethod
    def __tweet(args):
        ans = add_post(args['token'], args['body'])
        return {'ans': ans}

    @staticmethod
    def __login(args):
        ans = login(args['username'], args['password'])
        return {'ans': ans}

    @staticmethod
    def __logout(args):
        ans = logout(args['token'])
        return {'ans': ans}

    @staticmethod
    def __signup(args):
        ans = registration(args['username'], args['password'])
        return {'ans': ans}

    @staticmethod
    def __hashtag(args):
        ans = hashtag_posts(args['hashtag'])
        return {'ans': ans}

@rest_resource
class SecureResourceOne(SecureResource):
    """/api/resource/two"""
    endpoints = ['/resource/two/<string:resource_id>', '/te']

    def get(self, resource_id):
        time.sleep(1)
        return {'name': 'Resource Two', 'data': resource_id}
