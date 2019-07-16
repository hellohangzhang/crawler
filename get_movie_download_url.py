import requests
from bs4 import BeautifulSoup
from urllib import parse

url_part1 = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='
key_words = input("Input your favorite movies:")
url_part2 = parse.quote(key_words.encode('gb2312'))
url = url_part1 + url_part2

res = requests.get(url)
res.encoding='gb2312'
bs = BeautifulSoup(res.text,'html.parser')
movie_url_part2 = bs.find('div',class_='co_content8').select('ul table b a')[0]['href']
website_url_part1 = 'https://www.ygdy8.com'
movie_url =  website_url_part1 + movie_url_part2


res_movie = requests.get(movie_url)
res_movie.encoding = 'gb2312'
bs_movie = BeautifulSoup(res_movie.text,'html.parser')
download_url = bs_movie.select('tbody tr td a')[0]['href']
print(download_url)
