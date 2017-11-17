import urllib2, json
import data_scraper as scraper

nyt_base="https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key="

f = open("../key.txt", "r")
txt = f.read()
key = txt.split('\n')[0]

#Keep track of how often this function is called!
#DON'T go over quotas!!

def access_url(query):
    acc = nyt_base + key
    if (query == ""):
        try:
            data = urllib2.urlopen(acc)
            d = json.loads(data.read())
            return d
        except:
            print "your key is wrong or you have reached your monthy quota"
    
    else:
       try:
           acc += "&query="
           q = query.replace(' ', "+")
           acc += q
           data = urllib2.urlopen(acc)
           d = json.loads(data.read())
           return d
       except:
           print "your key is wrong or you have reached your monthy quota"
           

def get_title(query=""):
    d = access_url(query)
    print  d['results'][0]["display_title"]
    return d['results'][0]["display_title"]

def get_review(query):
    if query =="":
        print "give me a title"
    else:
        try:
            d = access_url(query)
            links = []
            reviews=[]
            for each in d['results']:
                links.append(each['link']['url'])
            for link in links:
                reviews.append(scraper.scrape(link))
            return reviews
        except:
            print "No review found"


#TESTING...
print get_review('silence of the lambs')
#works
