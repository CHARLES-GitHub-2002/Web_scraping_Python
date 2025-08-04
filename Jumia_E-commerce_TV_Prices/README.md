# 📺 Jumia TV Prices Scraper

This Python script scrapes television names and their current prices from the [Jumia Kenya Televisions](https://www.jumia.co.ke/televisions/) section. It's useful for price monitoring, market research, or personal budgeting.

## 🔍 What It Does

- Visits multiple pages of Jumia's TV listings
- Extracts each product's name and price
- Stores the data in a structured CSV file
- Handles pagination (up to a specified number of pages)

## 🛠️ Tech Stack

- Python 3
- BeautifulSoup4
- Requests
- Pandas

## 📁 Files
jumia_tv_prices.py # Main script for scraping

requirements.txt # List of Python dependencies

jumia_televisions3.csv # Output CSV file (auto-generated after run)

README.md # Project documentation

###Sample of Output

| Product Name                             | Price       |
| ---------------------------------------- | ----------- |
| Skyworth 55G6500G, 55" 4K UHD Android TV | KSh 47,999  |
| Vision Plus 32 Inch Frameless HD LED TV  | KSh 13,499  |
| Samsung 65" UHD 4K Smart TV              | KSh 102,999 |


