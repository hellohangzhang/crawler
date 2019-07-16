import requests
import html

song_list_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=71893582173610281&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
headers_1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Origin':'https://y.qq.com',
'Referer':'https://y.qq.com/portal/search.html'
}

res_1 = requests.get(song_list_url,headers=headers_1)
res_1_json = res_1.json()
song_lists = res_1_json['data']['song']['list']
song_id = ''
params = {
'nobase64': '1',
'musicid': song_id,
'-': 'jsonp1',
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

song_lirics = []
for song_list in song_lists:
	print(song_list['name'])
	song_id = song_list['id']
	url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
	params['musicid'] = song_id
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Origin':'https://y.qq.com',
'Referer':'https://y.qq.com/n/yqq/song/001xd0HI0X9GNq.html'}
	res = requests.get(url,headers=headers,params=params)
	res_json = res.json()
	song_liric = res_json['lyric']
	song_lirics.append(song_liric)
	print(html.unescape(song_liric))
