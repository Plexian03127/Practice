import requests
from bs4 import BeautifulSoup
import random
import time

url = 'https://www.melon.com/chart/index.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)


print("==========================")
print("| 1. 멜론 차트 TOP 100곡 |")
print("| 2. 멜론 차트 TOP 50곡  |")
print("| 3. 멜론 차트 TOP 10곡  |")
print("| 4. 멜론 차트 AI 추천곡 |")
print("| 5. 가수 이름 검색      |")
print("==========================")

a = "<멜론 차트 TOP 100곡>"
b = "<멜론 차트 TOP 50곡>"
c = "<멜론 차트 TOP 10곡>"
d = "<멜론 차트 AI 추천곡>"
e = "<가수 이름 검색>"

n = input("[원하시는 서비스에 해당하는 번호를 입력하세요.]: ")
if n == "1":
    print(a)
    time.sleep(1)
    if response.status_code == 200:
     soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 100:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

elif n == "2":
    print(b)
    time.sleep(1)
    if response.status_code == 200:
     soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 50:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. | 상태 코드: {response.status_code}]')

elif n == "3":
    print(c)
    time.sleep(1)
    if response.status_code == 200:
     soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 10:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')

elif n == "4":
    print(d)
    time.sleep(1)
    print("[좋아요! 제가 열심히 찾아서 사용자님께 노래를 한 곡 추천할게요.]")
    time.sleep(1)
    print(f"[두구두구둥...]")

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
        time.sleep(1)
        print(f"[이 노래가 좋을 거 같아요!]")
        time.sleep(1)
        print(f'\n[추천 곡: {random_song[1]} | 아티스트: {random_song[2]}]')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')

elif n == "5":
    print(e)
    time.sleep(1)
    s = input("[검색하고 싶은 가수의 이름을 입력하세요.]: ")
    print("[죄송해요. 해당 서비스는 아직 준비 중이에요.]")
else:
    print(f"[<{n}>번에 해당하는 서비스가 없어요. 1~5번 중에 선택해 주세요.]")