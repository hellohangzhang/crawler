import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')
book_infos = bs.find_all('article',class_='product_pod')

for book_info in book_infos:
	print('book name:',book_info.find('h3').find('a')['title'])
	print('book rating:',book_info.find('p')['class'][1].strip())
	print('book price:',book_info.find('div',class_='product_price').find('p',class_='price_color').text.strip())
	print('\n')
