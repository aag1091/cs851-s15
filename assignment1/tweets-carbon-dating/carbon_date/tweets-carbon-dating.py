from local import cd
import json
import pymongo
from pymongo import MongoClient
import datetime
import time
import math
import random

client = MongoClient()
db = client.url_of_set_http

if __name__ == "__main__":
    tweet_count = db.tweet_data.find({ "estimated_creation_date" : { "$exists" : 0 }, "status_code" : 200 }).count()
    tweets = db.tweet_data.find({ "estimated_creation_date" : { "$exists" : 0 }, "status_code" : 200 }).skip(int(math.floor(random.random()*tweet_count))).limit(5000)
    for tweet in tweets:
        if db.tweet_data.find({ "estimated_creation_date" : { "$exists" : 0 }, "_id" : tweet["_id"] }).count() > 0:
            print "Finding estimated creation date for " + tweet["url"]
            resp = json.loads(cd(tweet["url"]))
            db.tweet_data.update({'_id': tweet["_id"]}, {"$set": {"estimated_creation_date" : resp["Estimated Creation Date"] }})