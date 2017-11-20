from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.blueapron.com/pages/sample-recipes'


# open connection, grab the page (offloading content into variable)
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

#page_soup.h1
#page_soup.p

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
recipes = page_soup.findAll("div",{"class":"tab-content js-initialMenu"})



    # first test, return both 2-person and family
    #recipes = page_soup.findAll("div",{"class":"recipe-title"})

    # another test
    # recipes = page_soup.findAll("div",{"class":"card recipe-thumb col-md-4"})

# len(recipes)

#recipes[0]
    # to get html

#recipe = recipes[0]

for recipe in recipes:
    title = recipe.findAll("div", {"class":"recipe-title"}) #**
    title[0].encode("ascii")
    #print title[0].text

    for name in title:
        print(name.text)

##    for titles, descriptions in title.items():
##        print(titles)
##        print(descriptions)
    


