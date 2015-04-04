import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.word_count_http
wget = db.wget_word_count
boilerpipe = db.boilerpipe_word_count

if __name__ == '__main__':

    wget_words = db.wget_word_count.find().sort("count", -1).limit(50)
    opt = open("wget_words.csv", "w")
    for word in wget_words:
        opt.write(word["word"] +","+str(word["count"])+"\n")
    opt.close()

    boilerpipe_words = db.boilerpipe_word_count.find().sort("count", -1).limit(50)
    opt = open("boilerpipe_words.csv", "w")
    for word in boilerpipe_words:
        opt.write(word["word"] +","+str(word["count"])+"\n")
    opt.close()