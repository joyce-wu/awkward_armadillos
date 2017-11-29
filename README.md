# awkward_armadillos

## Roster

Kelly Wang, Tiffany Moi, Joyce Wu, Jen Yu

### Filmadillo: Movie Descriptions and Reviews

In this website, we integrate two APIS: The NYT Movie Reviews API and OMDb API. The NYT API provides reviews by top critics and OMDb API provides a variety of information about movies such as description, point ratings, posters, etc. Using the data from these APIs, we hope to create site for users to easily search and save movies they're interested in, as well as read opinions of critics on the films. 

### Launch Instructions

Needed: 
* Python
* Flask
* LXML
* CSSSelect
* Requests (external Flask module)

Python, Flask, LXML and CSSSelect are needed in order to run this webapp. You should install Flask, LXML, CSSSelect, and Requests in a virtual environment so it doesn't interfere with your root python install. 

Run these in the terminal to install all dependencies. 
```
$ (venv) pip install flask
```
```
$ (venv) pip install lxml
```
```
$ (venv) pip install cssselect
```
```
$ (venv) pip install requests
```

*__To Run:__*

First, procure API keys from the [NYT Developers](http://developer.nytimes.com/) for the NYT Movie Reviews API and [OMDb](http://www.omdbapi.com/apikey.aspx).

Clone this repo: 
```
$ git clone git@github.com:tmoi29/awkward_armadillos.git
```

Now, ```cd``` into the repo: 
```
$ cd awkward_armadillos
```

Add your API keys to the ```keys.txt``` file, in this format: 
```
[NYT API Key FRIST]
[OMDb API Key SNECOD]
```
Run the application!
```
$ python app.py
```
View this webpage by navigating to ```localhost:5000``` in your web browser. 

### Additional Resources

NYT Movie Reviews API: 
[GoogDrive Doc](https://docs.google.com/a/stuy.edu/document/d/138g9mcEWftJDkWSIxSlhi7eVU6CKA_JUWlwOUcjP1sA/edit?usp=drive_web)

[Source Documentation](http://developer.nytimes.com/movie_reviews_v2.json)

OMDb: 
[GoogDrive Doc](https://drive.google.com/open?id=1hT7aXiAtwTTtCJrx9zArBhlX6mP8RG_V5xldPZjPk8E)

[Source Documentation](http://www.omdbapi.com/)
