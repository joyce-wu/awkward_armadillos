'''
Python file for handling the NYT Movie Reviews API
Utilized in the: 
 * Search Bar
 * Reviews on a movie's page (data scraping)
'''
import urllib2, json
import data_scraper as scraper

nyt_base="https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key="

#read NYT API Key from the 'keys.txt' file
f = open("key.txt", "r")
txt = f.read()
key = txt.split('\n')[0]

'''
access_url(query) - Function to pull data from the NYT API
 * query parameter is used to access specific information in API
 * Used in search bar, and later for extracting the movie review
KEEP TRACK OF HOW OFTEN THIS FXN IS CALL TO NOT GO OVER QUOTAS.
'''
def access_url(query):
    acc = nyt_base + key
    if (query == ""):
        try:
            data = urllib2.urlopen(acc)
            d = json.loads(data.read())
            return d
        except:
            print "Your key is wrong or you have reached your monthy quota.(1)"
    
    else:
       try:
           acc += "&query="
           q = query.replace(' ', "+")
           acc += q
           data = urllib2.urlopen(acc)
           d = json.loads(data.read())
           return d
       except:
           print "Your key is wrong or you have reached your monthy quota.(2)"
           

'''
search_results(query): Gets a list of movies from a searched keyword
 * Wrapper for NYT API's search functionality
 * Pulls .json object string after searching query
 * Used in display of search results
 * Sublist Schema: [0]-Movie Title, [1]-Review URL, [2]-Short Summary
KEEP TRACK OF HOW MANY TIMES THIS IS CALLED, AS IT USES access_url().
'''
def search_results(query=""):
    d = access_url(query)
    results = []
    l = []
    try:
        for a in d['results']:
            #append movie title and review url
            title = a["display_title"].replace(" ", "_")
            l.append(title)
            l.append(a["link"]["url"])
            l.append(a["summary_short"])
            #append sublist to main result list
            results.append(l)
            l = []
        return results
    except:
        return "No results."
    

'''
get_review(query): Uses data scraping to retrieve the text of review on the NYT API matching a certain search criteria (query). 
 * Used when movie is clicked on within the search results/homepage.
 * Based on full movie name, gets reviews from site.
- Jen: rethinking this, we probably want to get the review url in the search, and then scrape that later when the user clicks the link...
'''
def get_review(url):
    try:
        return scraper.scrape(url)
    except:
        print "No Review."
    '''
    if query =="":
        print "No movie title given."
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
    '''
