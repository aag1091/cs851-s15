import subprocess
import os
import csv
import datetime
import pymongo
from pymongo import MongoClient
import requests
import justext

client = MongoClient()
db = client.url_of_set_http

def fetchWebPage(url, fileName):
  print 'Fetching ', url
  subprocess.Popen(["wget","--output-document=" + fileName, url]) # + ".html"
    
sites = 'sitesq2'
if not os.path.exists(sites):
    os.makedirs(sites)

os.chdir(sites)

print datetime.datetime.now()
tweets = db.tweet_data.find({"status_code": 200}).skip(0)
for tweet in tweets:
  if not os.path.exists(str(tweet['tweet_id'])):
    fetchWebPage(str(tweet['url']), str(tweet['tweet_id']))
  else:
    print "skipped"+'-'+str(tweet['tweet_id'])

print datetime.datetime.now()

    
