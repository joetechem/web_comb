from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.blueapron.com/pages/sample-recipes'

uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

recipes = page_soup.findAll("div",{"class":"tab-content js-initialMenu"})

for recipe in recipes:
    title = recipe.findAll("div", {"class":"recipe-title"}) #**
    title[0].encode("ascii")

for name in title:
    print(name.text)




