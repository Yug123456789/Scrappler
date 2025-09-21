#git init
#git status => if you want to check what are the status of filess
# git diff  => if you want to check what are  th  changes 
# git add .
# git commit -m "Your message"
# copy paste git  code form github
 

import requests  
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"


def scrape_books(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to  retrieve the page")
        return
    
    # Set encoding explicitly to  handle special characters correctly
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_ = "product_pod")
    all_books = []
    for book in books:
        tittle = book.h3.a['title']
        price_text = book.find("p", class_= 'price_color').text
        currency = price_text[0]
        price  = float(price_text[1])
        print(tittle, currency, price )
        all_books.append(
            {
                "tittle": tittle,
                "currency": currency,
                "price": price
            }
        )
        return all_books

books = scrape_books(url)

with open("books.json", 'w', encoding='utf') as f:
    import json
    json.dump(books, f, indent = 2, ensure_ascii=False)