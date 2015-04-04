# Some of the code used is from http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.word_count_http
wget = db.wget_word_count
boilerpipe = db.boilerpipe_word_count

def removePunctuation(word):
    word = re.sub('[\",():;?\\[\\].{}#$&_*+=%!<>~0-9]', '', word)
    word = re.sub('`', '', word)
    return word

def strip_control_characters(input):  
    if input:  
        import re  
        # unicode invalid characters  
        RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                         u'|' + \
                         u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
                          (unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),  
                           unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),  
                           unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),  
                           )  
        input = re.sub(RE_XML_ILLEGAL, "", input)  
  
        # ascii control characters  
        input = re.sub(r"[\x01-\x1F\x7F]", "", input)  
    return input  
       
if __name__ == '__main__':
    files_in_dir = os.listdir('sitesq2')
    os.chdir('sitesq2')
    for file_in_dir in files_in_dir:
        f = open(file_in_dir, 'r').read()
        words = f.split()
        for word in words:
            try:
                word = word.encode(encoding='UTF-8',errors='strict')
            except Exception:
                word = ''
            word = word.decode(encoding='UTF-8',errors='strict')
            word = word.lower()
            word = word.strip()        
            word = removePunctuation(word)
            word = strip_control_characters(word)
            word = word.strip()        
            print word
            word_in_db = db.wget_word_count.find_one({"word" : word})
            if word != "":
                if word_in_db is None:
                    db.wget_word_count.insert({"word" : word , "count" : 1})
                else:
                    db.wget_word_count.update({"word" : word}, {"word" : word, "count" : word_in_db["count"]+1})