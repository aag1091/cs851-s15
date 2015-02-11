import pymongo
from pymongo import MongoClient

import pprint

import requests
import json

import pycurl
from StringIO import StringIO

client = MongoClient()
db1 = client.set_http
db2 = client.url_of_set_http

pp = pprint.PrettyPrinter(indent=4)

tweet_data = db2.tweet_data

def insert_curl_data(tweet_id, created_at, url, status_code):
    s = {}
    s['tweet_id'] = tweet_id
    s['created_at'] = created_at
    s['url'] = url
    s['status_code'] = status_code
    tweet_data_id = tweet_data.insert(s)
    pp.pprint(tweet_data_id)

if __name__ == "__main__":
    tweet_count = db1.tweets.count()
    size = 100
    page = 1
    while page < (tweet_count/100+1):
        tweets = db1.tweets.find().skip(size * (page - 1)).limit(size)
        page = page + 1
        for tweet in tweets:
            for url in tweet['entities']['urls']:
                try:
                    r = requests.head(url=""+url['url'], allow_redirects=True, timeout=10)
                    for u in r.history:
                        insert_curl_data(tweet['id'], tweet['created_at'], u.url, u.status_code)
                    insert_curl_data(tweet['id'], tweet['created_at'], r.url, r.status_code)
                except:
                    insert_curl_data(tweet['id'], tweet['created_at'], r.url, 408)