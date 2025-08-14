# 📚 Book Store Web Scraper

## 📌 Project Overview
This project is a **web scraping** script built using **BeautifulSoup** and **Requests** in Python.  
It targets an online book store, extracts details of each book, and saves the collected data into a **CSV file** for analysis.

---

## 🎯 Features
- Scrapes **book name**
- Scrapes **book price**
- Scrapes **UPC (Unique Product Code)**
- Retrieves **direct link to the book** in the store
- Converts scraped data into a **pandas DataFrame**
- Saves the data to a **CSV file**

---

## 🛠️ Tools & Libraries Used
- **Python 3**
- **BeautifulSoup4** – for parsing HTML
- **Requests** – for making HTTP requests
- **pandas** – for structuring data and saving to CSV

---

## 📂 Project Workflow
1. **Send a request** to the target book store webpage using `requests`.
2. **Parse the HTML content** using `BeautifulSoup`.
3. **Extract book details**:
   - Book title
   - Price
   - UPC
   - Book link
4. Store all extracted details into **Python lists**.
5. Convert lists into a **pandas DataFrame**.
6. **Save the DataFrame** as a `.csv` file for later use.

---

## 📋 Example Output
| Book Name        | Price  | UPC         | Link                                |
|------------------|--------|-------------|-------------------------------------|
| Book Title 1     | 51.33  | 1234567890  | http://example.com/book-title-1     |
| Book Title 2     | 45.00  | 0987654321  | http://example.com/book-title-2     |

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/bookstore-webscraper.git
   cd bookstore-webscraper
