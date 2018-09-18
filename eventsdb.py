from pymongo import MongoClient
import urllib

# client = MongoClient('mongodb://larinsergey101:'+urllib.parse.quote('1r1nalar1n@')+'@ds259742.mlab.com:59742/vuevents')
client = MongoClient('mongodb://heroku_knlkljm8:r6ko4kpeg5bqbr76e8edoogt9o@ds261302.mlab.com:61302/heroku_knlkljm8')
db = client["vuevents"]
events = db["events"]