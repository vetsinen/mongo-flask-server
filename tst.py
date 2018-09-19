from pymongo import MongoClient
import urllib

client = MongoClient('mongodb://larinsergey101:'+urllib.parse.quote('1r1nalar1n@')+'@ds259742.mlab.com:59742/vuevents')
db = client["vuevents"]
test = db["test"]
from pprint import pprint

if test.find({"_id":"33"}).count()>0:
    print(42)
if not test.find({"_id":"2"}):
    test.insert({"_id": "2", "a": "b"})
# test.insert({"_id":"2","a":"b"})



for x in test.find():
    pprint(x)