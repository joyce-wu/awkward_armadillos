'''
awkward_armadillos
P #1: arRESTed development
Kelly Wang, Tiffany Moi, Joyce Wu, Jen Yu
'''

from flask import Flask, render_template
from utils import read
import urllib2, json

app = Flask(__name__)

@app.route("/")
def start():
    render_template('home.html')

@app.route("/search")
def search():
    
    render_template("movie_review.html")

