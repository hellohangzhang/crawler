import requests
import openpyxl

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

res = requests.get(url,params=params,headers=headers)

res_1_json = res.json()
song_lists = res_1_json['data']['song']['list']
song_infos= []
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['歌曲名','所属专辑','播放时长'])

for song_list in song_lists:
	m,s = divmod(int(song_list['interval']),60)
	time_interval = str(m)+':'+str(s)
	sheet.append([song_list['name'],song_list['album']['name'],time_interval])

wb.save('周杰伦的歌曲信息.xlsx')
