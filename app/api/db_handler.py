#! /usr/bin/python

import redis, hashlib, urllib
from flask import request
import time
# from app import app
import pprint
import unicodedata
import base64


def getrand():
    data = str(time.time()).encode("utf-8")
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


@static_vars(r=False)
def redisLink():
    if redisLink.r:
        return redisLink.r
    redisLink.r = redis.StrictRedis(host='localhost', port=6379, db=0)
    return redisLink.r


def login(username, password):
    r = redisLink()
    if not r.hexists("users", username):
        return "Not Registered"
    usrid = r.hget("users", username).decode("utf-8")
    usr = r.hgetall("user:" + usrid)
    user = {key.decode('utf-8'): value.decode('utf-8') for (key, value) in usr.items()}
    if user['auth'] != '':
        return "Already Logged In"
    if user['password'] == password:
        auth = getrand()
        r.hset('user:' + usrid, 'auth', auth)
        r.hset('tokens', auth, usrid)
        return auth
    else:
        return "Wrong Password"


def logout(token):
    r = redisLink()
    if not r.hexists('tokens', token):
        return "User Not Logged-in"
    usrid = r.hget('tokens', token).decode('utf-8')
    r.hdel('tokens', token)
    r.hset('user:' + usrid, 'auth', '')
    return "Logged Out"


def registration(username, password):
    r = redisLink()
    if r.hget("users", username):
        return "Already Registered"
    userid = r.incr("next_user_id")
    authsecret = getrand()
    r.hset("users", username, userid)
    r.hmset("user:" + str(userid), {"username": username, "password": password,
                                    "auth": authsecret})
    r.hset('tokens', authsecret, userid)
    return authsecret


def check_user_existance(username):
    r = redisLink()
    if not r.hget("users", username):
        return False
    else:
        return True


def follow_user(token, followerid):
    r = redisLink()
    userid = get_id_token(token)
    if userid == -1:
        return False
    r.sadd("followers:" + str(userid), followerid)
    r.sadd("following:" + str(followerid), userid)
    r.sadd('log:' + str(userid), "User " + str(get_username(userid)) + " Followed " + str(get_username(followerid)) + " on " + str(
        time.asctime(time.localtime(time.time()))))
    return True


def unfollow_user(token, followerid):
    r = redisLink()
    userid = get_id_token(token)
    if userid == -1:
        return False
    r.srem("followers:" + str(userid), followerid)
    r.srem("following:" + str(followerid), userid)
    return True


def get_username(userid):
    r = redisLink()
    return r.hget("user:" + str(userid), "username").decode('utf-8')


def get_user_id(username):
    r = redisLink()
    dat = r.hget('users', username)
    if dat is None:
        return -1
    return int(dat)


def user_list():
    r = redisLink()
    dat = r.hgetall('users')
    data = {key.decode('utf-8'): int(value.decode('utf-8')) for (key, value) in dat.items()}
    return data


def get_id_token(token):
    r = redisLink()
    if not r.hexists('tokens', token):
        return -1
    usrid = r.hget('tokens', token).decode('utf-8')
    return int(usrid)


def add_post(token, body, retweet=False):
    r = redisLink()
    userid = get_id_token(token)
    if userid == -1:
        return "Invalid Token"
    if retweet:
        r.sadd('log:' + str(userid), "User " + str(get_username(userid)) + " retweeted " + str(body) + " on " + str(
            time.asctime(time.localtime(time.time()))))
    postid = r.incr("next_post_id")

    r.hmset("post:" + str(postid), {"user_id": str(userid), "time": time.time(),
                                    "body": body, "retweet": retweet, "likeCnt": 0})
    r.sadd("userposts:" + str(userid), postid)
    process_hashtags(body, postid)
    return "Post Added"


def process_hashtags(body, postid):
    r = redisLink()
    dat = list({tag.strip("#") for tag in body.split() if tag.startswith("#")})
    for d in dat:
        r.zincrby('hashtags', d, 1)
        r.sadd(d, postid)


def like_post(token, postid):
    r = redisLink()
    userid = get_id_token(token)
    if userid == -1:
        return "Invalid Token"
    if r.sismember('likes:' + str(postid), str(userid)):
        return "Already Liked"
    r.hincrby('post:' + str(postid), 'likeCnt', 1)
    r.sadd('likes:' + str(postid), userid)
    r.sadd('log:' + str(userid),
           "User " + str(get_username(userid)) + " Liked " + str(get_post(postid)['body']) + " on " + str(
               time.asctime(time.localtime(time.time()))))
    return "Liked"


def unlike_post(token, postid):
    r = redisLink()
    userid = get_id_token(token)
    if userid == -1:
        return "Invalid Token"
    if not r.sismember('likes:' + str(postid), str(userid)):
        return "Hasn't Been Liked"
    r.hincrby('post:' + str(postid), 'likeCnt', -1)
    r.srem('likes:' + str(postid), userid)


def add_retweet(token, postid):
    r = redisLink()
    post = get_post(postid)
    return add_post(token, post['body'], True)


def hashtag_search(hashtag):
    r = redisLink()
    dat: list = []
    for d in [key.decode('utf-8') for key in r.keys("*" + str(hashtag) + "*")]:
        if r.zscore('hashtags', d):
            dat.append(d)
    return dat


def hashtag_posts(hashtag):
    r = redisLink()
    dat: list = [int(key.decode('utf-8')) for key in r.smembers(str(hashtag))]
    posts = []
    for d in dat:
        posts.append(get_post(d))
    return posts


def user_info(token):
    r = redisLink()
    userid = get_id_token(token)
    if userid == -1:
        return "Invalid Token"
    username = r.hget('user:' + str(userid), 'username').decode('utf-8')
    dat = {'id': userid, 'username': username}
    return dat


def get_post(postid):
    r = redisLink()
    post = r.hgetall("post:" + str(postid))
    p = {key.decode('utf-8'): value.decode('utf-8') for (key, value) in post.items()}
    username = get_username(p['user_id'])
    p.update({'username': username})
    return p


def get_all_user_posts(userid):
    r = redisLink()
    pid = {key.decode('utf-8') for key in (r.smembers('userposts:' + str(userid)))}
    posts = []
    for i in pid:
        p: dict = get_post(i)
        if p:
            p.update({'id': i})
            posts.append(p)
    return posts


def get_all_following(token):
    r = redisLink()
    userid = get_id_token(token)
    if userid == -1:
        return "Invalid Token"
    ret = [int(key.decode('utf-8')) for key in r.smembers('followers:' + str(userid))]
    ret.append(userid)
    return ret


def get_posts_for_home(token):
    if not redisLink().hexists('tokens', token):
        return "Invalid Token"
    users = get_all_following(token)
    posts = []
    for u in users:
        posts.append(get_all_user_posts(u))
    return posts


def get_logs(token):
    r = redisLink()
    userid = get_id_token(token)
    if userid == -1:
        return "Invalid Token"
    return [key.decode('utf-8') for key in r.smembers('log:'+str(userid))]


def top_hashtags():
    r = redisLink()
    return dict({key.decode('utf-8'): int(value) for (key, value) in r.zrange(str('hashtags'), 0, 10, desc=True, withscores=True)})
# def strElapsed(t):
#     d = int(time.time() - float(t))
#     if d < 60:
#         return str(d) + " seconds"
#     if d < 3600:
#         m = (int)(d / 60)
#         return str(m) + " minute" + ("s" if m > 1 else "")
#     if d < 3600 * 24:
#         h = (int)(d / 3600)
#         return str(h) + " hour" + ("s" if h > 1 else "")
#     d = (int)(d / (3600 * 24))
#     return str(d) + " day" + ("s" if d > 1 else "")


# def combine_url(base, param):
#     return base + "?" + urllib.urlencode(param)
