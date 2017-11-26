import lxml.html
from lxml.cssselect import CSSSelector

import requests

def scrape(url):
    r = requests.get(url)

    # build the DOM Tree
    tree = lxml.html.fromstring(r.text)

    # print the parsed DOM Tree
    
    # construct a CSS Selector
    sel = CSSSelector('p')

    # Apply the selector to the DOM tree.
    results = sel(tree)

    # get the text out of all the results
    data = [result.text for result in results]
    print data
    #returns a list of text
    return data

scrape('http://www.nytimes.com/2017/11/23/movies/bombshell-the-hedy-lamarr-story-review-.html')
