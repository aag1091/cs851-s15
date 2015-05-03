import os
import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.url_of_set_http
db1 = client.timemap_data

print datetime.datetime.now()
tweets = db.tweet_data.find({"status_code": 200}).skip(0)
opt = open("tweets.csv", "w")
for tweet in tweets:
  opt.write(str(tweet['url']) +","+str(tweet['tweet_id'])+"\n")
opt.close()

# if not os.path.exists(str(tweet['tweet_id'])):
#   fetchWebPage(str(tweet['url']), str(tweet['tweet_id']))
# else:
#   print "skipped"+'-'+str(tweet['tweet_id'])

print datetime.datetime.now()
