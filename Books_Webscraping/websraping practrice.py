import pandas as pd 
import numpy as np
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

base_url='https://books.toscrape.com/catalogue/'
relative_url='https://books.toscrape.com/catalogue/category/books/romance_8/page-1.html'

results=requests.get(relative_url)
src=results.content
soup=BeautifulSoup(src,"html.parser")

products=soup.find_all('article',class_='product_pod')

cleaned_links=[]
for product in products:
    links=product.find('a').get('href').lstrip('./')
    cleaned_links.append(links)

prices=[]
name=[]
stock=[]
for link in cleaned_links:
    full_links=urljoin(base_url,link)
    results=requests.get(full_links)
    soup=BeautifulSoup(results.text,"html.parser")
    title=soup.find('h1').getText(strip=True)
    price=soup.find('p',class_='price_color').get_text(strip=True)
    clean_price=re.sub(r'[^\d.]', '', price)
    in_stock=soup.find('p',class_='instock availability').get_text(strip=True)
    prices.append(clean_price)
    name.append(title)
    stock.append(in_stock)

df = pd.DataFrame({
    'Name': name,
    'Price': prices,
    'Stock': stock
})

print(df)

df.to_csv('output data.csv',index=False)