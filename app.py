from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

application = Flask(__name__)
CORS(application)

import urllib
application.config["MONGO_URI"] = 'mongodb://larinsergey101:'+urllib.parse.quote('1r1nalar1n@')+'@ds259742.mlab.com:59742/vuevents'
mongo = PyMongo(application)

import datetime
nowstr = str(datetime.datetime.now())[:10]


@application.route('/')
def status():
    d = mongo.db.events.count()
    return 'hello '+str(d)


@application.route('/events')
@application.route('/events/<string:date>')
def events(date=nowstr):
    rez=[]
    for e in mongo.db.events.find({'datestr':date}):
        rez.append(e)
    return jsonify(rez)
