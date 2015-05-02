import subprocess
import os
# import thread
# import threading
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
  opt = open(fileName+".txt", "w")
  response = requests.get(url)
  try:
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
  except Exception:
    paragraphs = []
  for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
      opt.write(paragraph.text.encode("utf-8"))
      
  opt.close()

sites = 'sitesq4'
if not os.path.exists(sites):
    os.makedirs(sites)

os.chdir(sites)

print datetime.datetime.now()
tweets = db.tweet_data.find({"status_code": 200}).skip(0)
for tweet in tweets:
  if not os.path.exists(str(tweet['tweet_id'])+".txt"):
    fetchWebPage(str(tweet['url']), str(tweet['tweet_id']))
  else:
    print "skipped"+'-'+str(tweet['tweet_id'])

print datetime.datetime.now()


    
