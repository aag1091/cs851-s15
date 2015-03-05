import pymongo
from pymongo import MongoClient
import os

client = MongoClient()
db = client.url_of_set_http
new_urls = open('new_urls.txt', 'w')
urls = open('urls.txt', 'r')


if __name__ == "__main__":
  # tweets = db.tweet_data.find({"status_code": 200}).skip(0).limit(200)
  # for tweet in tweets:
  #   urls.write(str(tweet['url']) + '\n')
  #	  os.system("wget '%s' --warc-file='%s'" % (tweet['url'], tweet['tweet_id']))

  i = 0
  for line in urls:
  	i+=1
  	name = "url-" + str(i)
  	os.system("wget '%s' --warc-file='%s' --no-warc-compression" % (line, name))
