import requests
# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
singer = input('Input your favorite singer:')
params = {
'ct': '24',
'qqmusic_ver': '1298',
'new_json': '1',
'remoteplace': 'txt.yqq.song',
'searchid': '71893582173610281',
't': '0',
'aggr': '1',
'cr': '1',
'catZhida': '1',
'lossless': '0',
'flag_qc': '0',
'p': '1',
'n': '10',
'w': singer,
'g_tk': '5381',
'loginUin': '0',
'hostUin': '0',
'format': 'json',
'inCharset': 'utf8',
'outCharset': 'utf-8',
'notice': '0',
'platform': 'yqq.json',
'needNewCode': '0'
}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Origin':'https://y.qq.com',
'Referer':'https://y.qq.com/portal/search.html'
}
    # 将参数封装为字典，其中pagenum和lastcommentid是特殊的变量
res = requests.get(url,params=params,headers=headers)
    # 调用get方法，下载评论列表
res_1_json = res.json()
song_lists = res_1_json['data']['song']['list']

for song_list in song_lists:
	print(song_list['name'])
