import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')
books_categories = bs.select('ul li a')
for i in books_categories[2:-1]:
	print(i.text.strip())
