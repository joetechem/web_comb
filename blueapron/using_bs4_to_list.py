from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.blueapron.com/pages/sample-recipes'
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
recipes = page_soup.findAll("div",{"class":"tab-content js-initialMenu"})

title_list = []

for recipe in recipes:
    title = recipe.findAll("div", {"class":"recipe-title"})

for name in title:
    titles = name.text
    #print titles
    title_list.append(titles)
    print(title_list)

# creates a list, but returns u' tags



    


