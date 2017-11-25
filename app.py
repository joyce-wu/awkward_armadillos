'''
awkward_armadillos
P #1: arRESTed development
Kelly Wang, Tiffany Moi, Joyce Wu, Jen Yu
'''

from flask import Flask, render_template, request
from utils import nyt_process, omdb_process
import urllib2, json

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('home.html')

@app.route("/search", methods=['POST', 'GET'])
def search():

    movie_list = nyt_process.get_title(request.form["title"])
    print movie_list
    movies = nyt_process.get_title(movie_list)
    return render_template("all_movies.html", movies = movies)

@app.route("/movie_review", methods=['POST', 'GET'])
def get_movie():
    movie = "the silence of the lambs"#request.get("movie_val") #refer back for variable_names
    info = omdb_process.get_info(movie)
    review = nyt_process.get_review(movie)
    return render_template("movie_review.html", director=info["Director"], title=info["Title"], year=info["Year"], genre=info["Genre"], plot=info["Plot"], pic=info["Poster"], review=review)

if __name__ == "__main__":
    app.debug = True
    app.run()
