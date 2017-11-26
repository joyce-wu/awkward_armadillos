import lxml.html
from lxml.cssselect import CSSSelector

import requests

def scrape(url):
    r = requests.get(url)

    # build the DOM Tree
    tree = lxml.html.fromstring(r.text)

    # print the parsed DOM Tree
    #print lxml.html.tostring(tree)
    
    # construct a CSS Selector
    sel = CSSSelector('p')

    # Apply the selector to the DOM tree.
    results = sel(tree)
    
    #print match.text
    for num in range (0, len(results)):
        match = results[num]
        
        if "<a href" in lxml.html.tostring(match):
            index1 = lxml.html.tostring(match).index('<a href')
            print index1
            print lxml.html.tostring(match)[0:index1]
            index2 = lxml.html.tostring(match).index('</a>')
            print index2
            print lxml.html.tostring(match)[index2:-1]
            print "HELLLLLLLLLLOOOOOOOOOOOOOO"
            result = lxml.html.tostring(match)[0:index1] + lxml.html.tostring(match)[index2:-1]
            results[num] = lxml.html.fromstring(result)
            print result
            
    # get the text out of all the results
    data = [result.text for result in results]
    print data
    #returns a list of text
    return data

scrape('https://www.nytimes.com/2017/11/16/movies/review-big-sonia-review-holocaust-survivor.html')
