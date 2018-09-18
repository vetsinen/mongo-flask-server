from flask import Flask
from flask import jsonify
from flask_cors import CORS
from eventsdb import events

application = Flask(__name__)
CORS(application)

import datetime

nowstr = str(datetime.datetime.now())[:10]


@application.route('/')
def status():
    return 'Hello, number of events is: ' + events.count()


@application.route('/events')
@application.route('/events/<string:date>')
def events(date=nowstr):
    return jsonify(zzzzzzzz(date))
