from pymongo import MongoClient
import urllib

client = MongoClient('mongodb://larinsergey101:'+urllib.parse.quote('1r1nalar1n@')+'@ds259742.mlab.com:59742/vuevents')
db = client["vuevents"]
events = db["events"]
from pprint import pprint

pprint((events.find_one({'datestr':'2018-10-10'})))