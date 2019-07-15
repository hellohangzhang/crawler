import requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.forc.work/'
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')
article_infos = bs.find_all('header',class_='entry-header')


for article_info in article_infos:
	print('The publish time is:',article_info.find('time',class_='entry-date published').text)
	print('The title is :',article_info.find('h2',class_='entry-title').text)
	print('The url is :',article_info.find('h2',class_='entry-title').find('a')['href'])
	print('\n')
