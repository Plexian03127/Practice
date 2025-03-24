import requests
from bs4 import BeautifulSoup

# 멜론 차트 100위 URL
url = 'https://www.melon.com/chart/index.htm'

# User-Agent 헤더 추가
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # 페이지 내용 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 차트 데이터 추출 (예: 순위, 곡 제목, 아티스트)
    songs = soup.select('tr[data-song-no]')  # 곡 정보를 포함하는 tr 태그 선택
    
    for song in songs:
        rank = song.select_one('span.rank').text.strip()  # 순위
        title = song.select_one('div.ellipsis.rank01 a').text.strip()  # 곡 제목
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()  # 아티스트 이름
        print(f'{rank}위 / 제목: {title} / 아티스트: {artist}')
else:
    print(f'웹 페이지를 가져오는 데 실패했습니다. 상태 코드: {response.status_code}')