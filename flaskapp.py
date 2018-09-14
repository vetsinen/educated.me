from flask import Flask
from flask import jsonify
import pickledb

from flask import render_template

app = Flask(__name__)
hello = '42'

db = pickledb.load('dated-events.db', False)

@app.route('/')
def index():
    # return render_template('index.html')
    date = '2018-09-14'
    items = len(db.get(date))
    return 'Hello,we found '+ str(items)

@app.route('/events/<string:date>')
def events(date):
    return jsonify(db.get(date))