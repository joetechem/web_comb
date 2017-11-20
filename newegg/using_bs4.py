from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# open connection, grab the page (offloading content into variable)
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

#page_soup.h1
#page_soup.p

# html parsing
page_soup = soup(page_html, "html.parser")

page_soup.h1
# grabs each product
##recipes = page_soup.findAll("div",{"class":"card recipe-thumb col-md-4"})

    # first test, return both 2-person and family
    #recipes = page_soup.findAll("div",{"class":"recipe-title"})

# len(recipes)

##recipes[0]
    # to get html

##recipe = recipes[0]
