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
db1 = client.timemap_data

def fetchWebPage(url, fileName):
  print 'Fetching ', url
  print fileName
  os.system("wget --output-document='" + fileName + "' 'http://labs.mementoweb.org/timemap/json/"+url+"'")
  # subprocess.Popen(["wget","--output-document=" + fileName, "http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/"+url])
    
sites = 'timemaps-json-3'
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
