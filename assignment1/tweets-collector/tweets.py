# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import json
import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.set_www

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "3FqrfV8foSfrCrOtaQFflThSE"
CONSUMER_SECRET = "YsDRpPoHfWYX8c10kKl7JRFE8L2qdsDfpuExoSZ6bvdKz8JjET"

OAUTH_TOKEN = "18227931-8RcOrMuvacj8Gz9T6hEUGts2D4BFhCFzPNk9xMyv3"
OAUTH_TOKEN_SECRET = "8YT8YH5f0JRsLra5lyIlV0oEpWQ1rGtQj4AKieeS7AI4g"

# save_file = open('tweets.json', 'a')

def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    print credentials

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]
    
    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url
    
    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

def get_tweets(next_url):
    try:
        r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json"+next_url, auth=oauth)
        response = r.json()
        statuses = response['statuses']
        metadata = response['search_metadata']
        for s in statuses:
            tweets = db.tweets
            tweet_id = tweets.insert(s)
            print tweet_id
    except:
        print 'sleeping for some time'
        time.sleep(600)
        get_tweets(next_url)
    
    # print json.dumps(statuses, indent=4)
    print db.tweets.count()
    print json.dumps(metadata, indent=4)
    if db.tweets.count() < 20000:
        get_tweets(metadata['next_results'])

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()
        # next_url = is the query string for the next page we need to get tweets from
        next_url = '?q=www&count=100&lang=en'
        get_tweets(next_url)
