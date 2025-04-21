import requests
from bs4 import BeautifulSoup
import random
import time

url = 'https://www.melon.com/chart/index.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

def fetch(limit):
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')
        song_list = []
        for index, song in enumerate(songs):
            if index >= limit:
                break
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            song_list.append((rank, title, artist))
        return song_list
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. | 상태 코드: {response.status_code}]')
        return []

def display(songs):
    for song in songs:
        print(f'{song[0]}위 | 제목: {song[1]} | 아티스트: {song[2]}')

def ai():
    print("[좋아요! 제가 열심히 찾아서 사용자님께 노래를 한 곡 추천할게요.]")
    time.sleep(1)
    print(f"[두구두구둥...]")
    time.sleep(1)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')
        song_list = [(song.select_one('span.rank').text.strip(),
                      song.select_one('div.ellipsis.rank01 a').text.strip(),
                      song.select_one('div.ellipsis.rank02 a').text.strip()) for song in songs]
        
        random_song = random.choice(song_list)
        print(f"[이 노래가 좋을 거 같아요!]")
        time.sleep(1)
        print(f'\n[추천 곡: {random_song[1]} | 아티스트: {random_song[2]}]')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')

def search():
    s = input("[검색하고 싶은 가수의 이름을 입력하세요.]: ")
    print(f"[<{s}>의 노래를 검색 중이에요...]")
    time.sleep(1)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')
        found_songs = []
        
        for song in songs:
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            if s.lower() in artist.lower():
                rank = song.select_one('span.rank').text.strip()
                title = song.select_one('div.ellipsis.rank01 a').text.strip()
                found_songs.append((rank, title, artist))

        if found_songs:
            print(f"[<{s}>의 노래 목록이에요.]")
            time.sleep(1)
            display(found_songs)
        else:
            print(f"[TOP 100곡 내 <{s}>의 노래가 없어요.]")
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')

def save():
    num_songs = input("[저장할 곡의 수를 입력하세요.(예: 100, 50, 10)]: ")
    songs = fetch(int(num_songs))
    
    file_name = input("[저장할 파일 이름을 입력하세요.(예: songs.txt)]: ")
    with open(file_name, 'w', encoding='utf-8') as f:
        for song in songs:
            f.write(f"{song[0]}위 | 제목: {song[1]} | 아티스트: {song[2]}\n")
    
    print(f"[노래 리스트가 {file_name}에 저장되었어요.]")