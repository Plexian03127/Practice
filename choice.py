import requests
from bs4 import BeautifulSoup
import random
import time

i = input("입력:")
print("알겠습니다. 제가 열심히 분석해서 고객님께 노래를 한 곡 추천합니다.")
t = time.sleep(1)
print("두구두구둥...")
t = time.sleep(3)
print(f"다음 노래를 추천합니다.")

url = 'https://www.melon.com/chart/index.htm'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


response = requests.get(url, headers=headers)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')


    songs = soup.select('tr[data-song-no]')
    song_list = []

    for song in songs:
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        song_list.append((rank, title, artist))


    random_song = random.choice(song_list)
    print(f'\n추천 곡: {random_song[1]} / 아티스트: {random_song[2]} (순위: {random_song[0]})')
else:
    print(f'웹 페이지를 가져오는 데 실패했습니다. 상태 코드: {response.status_code}')