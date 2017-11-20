from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.blueapron.com/pages/sample-recipes'
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
recipes = page_soup.findAll("div",{"class":"tab-content js-initialMenu"})

####### Write the data to a file #########
filename = "next_week_recipes.csv"
f = open(filename, "w")

headers = "title\n"

f.write(headers)

###########################################

for recipe in recipes:
    title = recipe.findAll("div", {"class":"recipe-title"}) #**
    #title[0].encode("ascii")

for name in title:
    titles = name.text
    print titles

    f.write(titles)

f.close()


    


