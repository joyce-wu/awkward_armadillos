'''
awkward_armadillos
P #1: arRESTed development
Kelly Wang, Tiffany Moi, Joyce Wu, Jen Yu
'''
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from utils import nyt_process, omdb_process, auth, database
import urllib2, json

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def start():
    # search_results with no query returns list of recommended movies
    movie_list = nyt_process.search_results()
    #is the user logged in?
    if session.get('username'):
        return render_template('base.html', title = "Home", movies = movie_list, loggedIn=True)
    return render_template('base.html', title = "Home", movies = movie_list, loggedIn=False)

# Login Authentication
@app.route('/login', methods=['GET', 'POST'])
def authentication():
    # if user already logged in, redirect to homepage(base.html)
    if session.get('username'):
        flash("Yikes! You're already signed in.")
        return redirect('profile')
    # user entered login form
    elif request.form.get('login'):
        print "login"
        return auth.login()
    # user didn't enter form
    else:
        return render_template('login.html', title = "Login")

# signup
@app.route('/signup', methods=['GET', 'POST'])
def crt_acct():
    # user already logged in
    if session.get('username'):
        flash("Yikes! You're already signed in.")
        return redirect('profile')
    # user already filled out signup form
    elif request.form.get('signup'):
        return auth.signup()
    else:
        return render_template('signup.html', title = "Signup" )

# Profile page - shows profile stats and (if time, allow them to change password)
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # must be logged in to view user profile!
    if not session.get('username'):
        flash("Yikes! You need to log in first.")
        return redirect(url_for('authentication'))
    else:
        # if user is logged in:
        # display their saved movies
        # with options to view and remove movies
        name = session.get('username')
        if request.form.get('movie'):
            print "\n\n\n" + request.form['movie'] + "\n\n\n"
            database.remove(name, request.form['movie'])
            flash("Yay! The movie was removed.")
        return render_template('profile.html', title = "Profile" , user=session.get('username'), loggedIn=True, movies=database.get_user_history(name))

# Logging out
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if not session.get('username'):
        flash("Yikes! You're not logged in")
    else:
        flash("Yay! You've successfully logged out")
        session.pop('username')
        return redirect(url_for('authentication'))

# Search - displays list of movies, their short summaries, and options to view more info abt each movie
@app.route("/search", methods=['POST', 'GET'])
def search():
    if session.get('username'):
        login = True
    else:
        login = False
    try:
        # use NYT API's search function to search for the keyword that the user entered
        movie_list = nyt_process.search_results(request.args["title"])
        # no results found
        if len(movie_list) == 0:
            return render_template("search.html", message = "No Results found.", loggedIn=login)
        # display list of movies 
        return render_template("search.html", title = "Search", movies = movie_list, loggedIn = login)
    except:
        flash("Yikes! You need to search for a movie first!")
        return redirect(url_for("start"))

# display information about the movie that the user selected
@app.route("/movie_review", methods=['POST', 'GET'])
def get_movie():
    if session.get('username'):
        login = True
    else:
        login = False
    # user wants to save this movie
    if login and request.form.get('movie'):
        database.add(session.get('username'), request.form['title'], request.form['plot'], request.form["url"])
        flash("Yay! This movie was added to your personal list.")
    if not login and request.form.get('movie'):
        flash("Yikes! You need to log in before adding movies.")
    try:
        movie = request.form['title'] #refer back for variable_names
        movie = movie.split("\n")
        url = request.form['url']
        url = url.split("\n")
        # get movie review from NYT API
        review = nyt_process.get_review(url[0])
    except:
        flash("Yikes! You need to find a movie first!")
        return redirect(url_for("start"))
    try:
        # extract movie info from OMDB API
        info = omdb_process.get_info(movie[0])
        return render_template("movie_review.html", title=movie[0].replace("_", " "), director=info["Director"], year=info["Year"], genre=info["Genre"], plot=info["Plot"], pic=info["Poster"], review=review, loggedIn=login, url=url[0], new=database.check(session.get('username'), movie[0]))
    except:
        if(review == None): # NYT API does not have a review for this movie
            return render_template("movie_review.html", title=movie[0].replace("_", " "), year="N/A", genre="N/A", plot="N/A", pic="N/A", review=["There is no review for this movie."], loggedIn=login, url=url[0], director = "N/A",new=database.check(session.get('username'), movie[0]))
        # movie info is not listed in the OMDB API
        return render_template("movie_review.html", title=movie[0].replace("_", " "), year="N/A", genre="N/A", plot="N/A", pic="N/A", review=review, loggedIn=login, url=url[0], director = "N/A",new=database.check(session.get('username'), movie[0]))

if __name__ == "__main__":
    app.debug = True
    app.run()
