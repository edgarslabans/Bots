from selenium import webdriver
import bs4 as bs
import pandas as pd
import urllib.request



source = urllib.request.urlopen('https://www.aircomnet.lv/index.php?categoryID=896').read()
soup = bs.BeautifulSoup(source,'lxml')

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)

#for h2 in soup.find_all('h2', class_ ='product-name item-title'):
#    print(h2.text)


for div in soup.find_all('div', class_='prdbrief_name'):
    print(div.text)

for div in soup.find_all('div', class_='prdbrief_price'):
    print(div.text)


