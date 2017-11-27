import urllib2, json
import nyt_process as nyt

omdb_base="http://www.omdbapi.com/?apikey="

#retrieves key from key.txt
f = open("key.txt", "r")
txt = f.read()
key = txt.split('\n')[1]

#Keep track of how often this function is called!
#DON'T go over quotas!!

#access url with api key
def access_url(query):
    acc = omdb_base + key
    if (query == ""):
        print "give me something to search for"

    else:
       try:
           acc += "&t="
           q = query.replace(' ', "+")
           acc += q
           data = urllib2.urlopen(acc)
           d = json.loads(data.read())
           return d
       except:
           print "your key is wrong or you have reached your monthy quota!"

#retrieves information from movies using the OMDb api
def get_info(query):
    d = access_url(query)
    info = {} #creates dictionary of information needed
    info["Title"] = d["Title"]
    info["Year"] = d["Year"]
    info["Genre"] = d["Genre"]
    info["Plot"] = d["Plot"]
    info["Poster"] = d["Poster"]
    info["Director"] = d["Director"]
    return info

#Wrapper for OMDB search function
def get_movie_data(query):
    q = nyt.get_title(query)
    for name in q:
        #print name
        d = access_url(name)
        '''
        for key in d:
            print key
            print d[key]
        '''
    return d

#testing
#print get_info('silence of the lambs')
