from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713](https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# 아래 빈 칸('')을 채워보세요
for tr in trs:
    ##body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    rank = tr.select_one('td.number').text[0:2].strip()
    # body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.albumtitle.ellipsis
    title = tr.select_one('td.info > a.albumtitle.ellipsis').text.strip()
    ##body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
    artist = tr.select_one('td.info > a.artist.ellipsis').text

    doc = {
        'rank' : rank,
        'title' : title,
        'artist' : artist
    }

    db. genie.insert_one(doc)