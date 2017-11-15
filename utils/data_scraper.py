import lxml.html
from lxml.cssselect import CSSSelector

import requests

r = requests.get('https://www.nytimes.com/2017/11/15/movies/rebels-on-pointe-review.html')

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
