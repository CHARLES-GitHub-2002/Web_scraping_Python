import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://www.scrapethissite.com/pages/simple/'
response=requests.get(url)
src=response.content
soup=BeautifulSoup(src,"html.parser")
country_names=soup.findclear
country_names = [tag.get_text(strip=True) for tag in soup.find_all(class_='country-name')]
#print(country_names)

capital=[tag.get_text(strip=True) for tag in soup.find_all(class_='country-capital')]
#print(capital)

population=[tag.get_text(strip=True) for tag in soup.find_all(class_='country-population')]
#print(population)

area=[tag.get_text(strip=True) for tag in soup.find_all(class_='country-area')]
#print(area)

df=pd.DataFrame({
    'country':country_names,
    'Capital City':capital,
    'Population':population,
    'Area(km2)':area
})

df.to_csv('Countries of the world2.csv',index=False)
print('CSV File Saved Successfully')