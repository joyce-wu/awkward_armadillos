'''
awkward_armadillos
P #1: arRESTed development
Kelly Wang, Tiffany Moi, Joyce Wu, Jen Yu
'''

from flask import Flask, render_template
from utils import process
from util import
import urllib2, json

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('home.html')

@app.route("/search", methods=['POST', 'GET'])
def search():
    movie_list = ... #nytimes search function
    movies = nyt_pro.get_title(movie_list)
    return render_template("all_movies.html", movies = movies)

@app.route("/movie_review", methods=['POST', 'GET'])
def get_movie():
    movie = request.get("movie_val") #refer back for variable_names
    info = omdb_process.get_info(movie)
    review = nyt_process.get_review(movie)
    return render_template("movie_review.html", title=info["Title"], year=info["Year"], genre=info["Genre"], plot=info["Plot"], pic=info["Poster"], review=review)
