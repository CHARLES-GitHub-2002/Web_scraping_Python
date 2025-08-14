import requests
from bs4 import BeautifulSoup
import pandas as pd

main_url='https://books.toscrape.com/catalogue/'
base_url='https://books.toscrape.com/catalogue/page-{}.html'

linkss=[]
prices=[]
books_name=[]
available=[]
Universal_Product_Code=[]
for page_number in range(1,50):
    url=base_url.format(page_number)
    #print(f"Scraping: {url}")
    
    results=requests.get(url)
    scr=results.content
    soup=BeautifulSoup(scr, "html.parser")

    if results.status_code != 200:
        print('Page not Found,Stopping')
        break
    
    items=soup.find_all('li','col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for item in items:
        links=item.find('a').get('href')
        full_links=main_url+links
        linkss.append(full_links)
for link in linkss:
    results=requests.get(link)
    soup=BeautifulSoup(results.text,'html.parser')  
    name=soup.find('h1').get_text()    
    books_name.append(name) 
    table=soup.find('table')
    # Loop through rows and find the one with the 'Price (excl. tax)' header
    for row in table.find_all('tr'):
        header = row.find('th').get_text(strip=True)
        if header == "Price (excl. tax)":
            price = row.find('td').get_text(strip=True)
            clean_price = price.replace("Â£", "")
            prices.append(clean_price)
    for row in table.find_all('tr'):
        header = row.find('th').get_text(strip=True)
        if header == "Availability":
            availabity = row.find('td').get_text(strip=True)
            available.append(availabity)
    
    for row in table.find_all('tr'):
        header = row.find('th').get_text(strip=True)
        if header == "UPC":
            upc = row.find('td').get_text(strip=True)
            Universal_Product_Code.append(upc)
df=pd.DataFrame({
    'Name':books_name,
    'Universal product code':Universal_Product_Code,
    'Availability':availabity,
    'Prices':prices,
    'Links':linkss,
})
    
df.to_csv('Books.csv',index=False)
print('All completed and the data is saved ')
 