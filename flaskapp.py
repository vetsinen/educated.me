from flask import Flask
from flask import jsonify
import pickledb
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

hello = '42'

db = pickledb.load('dated-events.db', False)
import datetime
nowstr = str(datetime.datetime.now())[:10]


@app.route('/')
def status():
    # return render_template('index.html')
    date = '2018-09-14'
    items = len(db.get(nowstr))
    return 'Hello,we found '+ str(items)

@app.route('/events')
@app.route('/events/<string:date>')
def events(date=nowstr):
    return jsonify(db.get(date))