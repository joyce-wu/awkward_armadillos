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
        
        #if there are links in the result, it won't scrape properly.
        if "href=" in lxml.html.tostring(match):
            index1 = lxml.html.tostring(match).index('<a href=')
            index2 = lxml.html.tostring(match).index('</a>')
            a = lxml.html.tostring(match)[index1+1:index2+1].index('>')
            b = lxml.html.tostring(match)[index1+1:index2+1].index('<')
            #stuff before the link + stuff inside the link + stuff after the link
            result = lxml.html.tostring(match)[0:index1] + lxml.html.tostring(match)[index1+2:index2][a:b] + lxml.html.tostring(match)[index2:-1]
            results[num] = lxml.html.fromstring(result)
            
    # get the text out of all the results
    data = [result.text for result in results]
    #returns a list of text
    return data

scrape('https://www.nytimes.com/2017/11/16/movies/review-big-sonia-review-holocaust-survivor.html')
