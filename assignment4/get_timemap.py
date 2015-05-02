import os
import datetime
import csv

def fetchWebPage(url, fileName):
  print 'Fetching ', url
  print fileName
  os.system("wget --output-document='" + fileName + "' 'http://labs.mementoweb.org/timemap/json/"+url+"'")
  # subprocess.Popen(["wget","--output-document=" + fileName, "http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/"+url])
    
sites = 'labs-timemaps-json-3'
if not os.path.exists(sites):
    os.makedirs(sites)

os.chdir(sites)

print datetime.datetime.now()
with open('../tweets.csv', 'rb') as f:
  reader = csv.reader(f)
  for row in reader:
    if not os.path.exists(str(row[1])):
      fetchWebPage(str(row[0]), str(row[1]))
    else:
      print "skipped"+'-'+str(row[1])

print datetime.datetime.now()
