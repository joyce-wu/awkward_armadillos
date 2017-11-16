import urllib2, json

nyt_base="https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key="

f = open("../nyt_key.txt", "r")
key = f.read()

#Keep track of how often this function is called!
#DON'T go over quotas!!

def access_url(query = ""):
    acc = nyt_base + key
    if (query = ""):
        data = urllib2.urlopen(acc)
        d = json.loads(data.read())
        return d

#Wrapper for NYT search function
def get_movies(query):
    d = access_url(nyt_base, nyt_key, "query", query)
    
