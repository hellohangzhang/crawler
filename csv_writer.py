import csv

with open('test.csv','w',newline='',encoding='gbk') as file_name:
	writer = csv.writer(file_name) 
	writer.writerow(['电影','豆瓣评分'])
	writer.writerow(['银河护卫队','8.0'])
	writer.writerow(['复仇者联盟','8.1'])
