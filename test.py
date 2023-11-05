from bs4 import BeautifulSoup as bs
import requests

results = requests.get('https://books.toscrape.com')
soup = bs(results.text, 'html.parser')

for bookName in soup.find_all('h3'):
    print(bookName.text)