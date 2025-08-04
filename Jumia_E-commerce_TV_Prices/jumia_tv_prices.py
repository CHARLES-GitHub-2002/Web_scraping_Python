import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

base_url = 'https://www.jumia.co.ke/televisions/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

product_names = []
product_prices = []

for page in range(1, 6):
    print(f'Scraping page {page}...')
    url = f"{base_url}?page={page}"  # Fixed space in URL
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('article', class_='prd')  # Try with just 'prd'
    for product in products:
        name_tag = product.find('h3', class_='name')
        price_tag = product.find('div', class_='prc')
        if name_tag and price_tag:
            product_names.append(name_tag.text.strip())
            product_prices.append(price_tag.text.strip())
    time.sleep(2)

df = pd.DataFrame({
    'product name': product_names,
    'price': product_prices
})

df.to_csv("jumia_televisions3.csv", index=False)