from calendar import c
from msilib.schema import Error
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.amazon.com/-/es/Los-ms-vendidos-Libros-Bibliografa-de-Industria-Editorial/zgbs/books/9996/ref=zg_bs_nav_books_4_118922'
request = Request(url, headers={'User-agent': 'Mozilla/5.0'})
html = urlopen(request)


soup = BeautifulSoup(html, 'html.parser')

books = soup.find_all('div', id="gridItemRoot")

for book in books:
    try:
        rank = book.find('span', class_="zg-bdg-text").get_text().replace('#', '')
        print(rank)
        title = book.find(
            'div',
            class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"
        ).get_text(strip=True)

        print(f"Titulo Libro: {title}")
        author = book.find('div', class_="a-row a-size-small").get_text(strip=True)
        print(f"Author: {author}")
        precio = book.find('span', class_="_cDEzb_p13n-sc-price_3mJ9Z").get_text()
        print(f"Price: {precio}")

    
    except:
        print('Precio not assigned')
        pass



    



   







