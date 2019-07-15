'''
Python小课，课后练习，获取网页里的所有评论内容。
'''


import requests
from bs4 import BeautifulSoup
url = 'https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/'
res = requests.get(url)
text = res.text
bs = BeautifulSoup(text,'html.parser')
comments = bs.find_all('div',class_='comment-content')
comments_list = []
for comment in comments:
	comments_list.append(comment.text)
	

print(len(comments_list))
for comment_content in comments_list:
	print(comment_content)


