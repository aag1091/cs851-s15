import pymongo
from pymongo import MongoClient

import datetime
import json
import time
import statistics

client = MongoClient()
db1 = client.set_http
db2 = client.url_of_set_http

no_of_unique_urls = open('no_of_unique_urls', 'w')
no_of_redirects = open('no_of_redirects.txt', 'w')
status_codes = open('status_codes.txt', 'w')
age = open('age.txt', 'w')

if __name__ == "__main__":
    tweet_data1 = db2.tweet_data.find()
    for tweet in tweet_data1:
        status_codes.write(str(int(tweet["status_code"])) + '\n')

    tweet_ids = []
    tweet_data2 = db2.tweet_data.find()
    for tweet in tweet_data2:
        if 'tweet_id' in tweet.keys():
            tweet_ids.append(tweet["tweet_id"])

    no_of_urls = len(db2.tweet_data.find({"status_code": 200}).distinct("url"))
    print "No of unique Url's" + " - "+ str(no_of_urls)
    no_of_unique_urls.write(str(no_of_urls) + '\n')

    deltas = []
    for tweet_id in set(tweet_ids):
        no_of_redirects.write(str(db2.tweet_data.find({"tweet_id" : tweet_id}).count()) + '\n')
        tweet_data = db2.tweet_data.find_one({"tweet_id" : tweet_id, "status_code" : 200})
        if tweet_data is not None:
            if tweet_data["estimated_creation_date"] != '':
                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet_data['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
                ct = time.strptime(ts, "%Y-%m-%d %H:%M:%S")
                cdt = datetime.datetime.fromtimestamp(time.mktime(ct))
                now = datetime.datetime.now()
                tweetagedays = (now - cdt).days
                
                ct = time.strptime(tweet_data['estimated_creation_date'], "%Y-%m-%dT%H:%M:%S")
                cdt = datetime.datetime.fromtimestamp(time.mktime(ct))
                now = datetime.datetime.now()
                carbonagedays = (now - cdt).days
                
                absoluteDelta= abs(tweetagedays-carbonagedays)
                deltas.append(absoluteDelta)
                print tweet_data["url"] + " - " + str(absoluteDelta)
                age.write(str(absoluteDelta) + '\n')


    print "Mean"
    print statistics.mean(deltas)

    print "Median"
    print statistics.median(deltas)

    print "Standard deviation"
    print statistics.stdev(deltas)

    print "Standard Error"
    print statistics.variance(deltas)