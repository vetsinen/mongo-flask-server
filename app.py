from flask import Flask
from flask import jsonify
from flask_cors import CORS

from pymongo import MongoClient
import urllib

client = MongoClient('mongodb://larinsergey101:'+urllib.parse.quote('1r1nalar1n@')+'@ds259742.mlab.com:59742/vuevents')
#client = MongoClient('mongodb://heroku_knlkljm8:r6ko4kpeg5bqbr76e8edoogt9o@ds261302.mlab.com:61302/heroku_knlkljm8')
db = client["vuevents"]
events = db["events"]

application = Flask(__name__)
CORS(application)

import datetime

nowstr = str(datetime.datetime.now())[:10]


@application.route('/')
def status():
    return str(type(events))


@application.route('/events')
@application.route('/events/<string:date>')
def events(date=nowstr):
    return jsonify(zzzzzzzz(date))
