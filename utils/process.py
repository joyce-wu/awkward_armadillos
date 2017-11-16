import urllib2, json

nyt_key="46da8b1424754c3b98e0dcb908aaca8a"
nyt_base="https://api.nytimes.com/svc/movies/v2/reviews/search.json"
mvdb_key="de1ce232"
mvdb_base=""

def read_keys():
    file = open("", "r")
    nyt_key = file.readline(1)
    omdb_key = file.readline(2)
    

#Keep track of how often this function is called!
#DON'T go over quotas!!
def access_url(url, key, arg, value):
    acc = url + "api-key=" + key + "&" + arg + "=" + value
    data = urllib2.urlopen(acc)
    d = json.loads(data.read())
    return d

#Wrapper for NYT search function
def get_movies(query):
    d = access_url(nyt_base, nyt_key, "query", query)
    
