from flask import Flask
from flask import jsonify
import pickledb
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

hello = '42'

# db = pickledb.load('dated-events.db', False)
import datetime
nowstr = str(datetime.datetime.now())[:10]


@app.route('/')
def status():
    return 'Hello,we found '+ 42

@app.route('/events')
@app.route('/events/<string:date>')
def events(date=nowstr):
    return jsonify(db.get(date))