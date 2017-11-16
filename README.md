# awkward_armadillos

## Roster

Kelly Wang, Tiffany Moi, Joyce Wu, Jen Yu

### Filmadillo: Movie Descriptions and Reviews

In this website, we integrate two APIS: The NYT Movie Reviews API and OMDb API. The NYT API provides reviews by top critics and OMDb API provides a variety of information about movies such as description, point ratings, posters, etc. Using the data from these APIs, we hope to create site for users to easily search and save movies they're interested in, as well as read opinions of critics on the films. 

### Launch Instructions

Needed: 
* Flask
* Python

Flask and Python are needed in order to run this webapp. You should install Flask in a virtual environment so it doesn't interfere with your root python install. 

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


NYT Movie Reviews API: 

[GoogDrive Doc](https://docs.google.com/a/stuy.edu/document/d/138g9mcEWftJDkWSIxSlhi7eVU6CKA_JUWlwOUcjP1sA/edit?usp=drive_web)

[Source Documentation](http://developer.nytimes.com/movie_reviews_v2.json)

API Key: 46da8b1424754c3b98e0dcb908aaca8a

OMDb: 
[Source Documentation](http://www.omdbapi.com/)
API Key: de1ce232
