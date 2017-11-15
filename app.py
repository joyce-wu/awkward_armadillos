'''
awkward_armadillos
P #1: arRESTed development
Kelly Wang, Tiffany Moi, Joyce Wu, Jen Yu
'''

from flask import Flask, render_template
from utils import read
import urllib2, json

app = Flask(__name__)
#NYT key: 46da8b1424754c3b98e0dcb908aaca8a
#Movie DB Key: de1ce232

@app.route("/")
def start():
    pass

