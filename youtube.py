import requests
from bs4 import BeautifulSoup

# 대상 URL
url = "https://playboard.co/youtube-ranking/most-popular-all-channels-in-south-korea-daily"

# User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# 페이지 요청
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"페이지에 접근할 수 없습니다. 상태 코드: {response.status_code}")
    exit()

# BeautifulSoup으로 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 결과 저장용 리스트
data_list = []

# 1부터 100까지 순회
for i in range(1, 101):
    # i가 6의 배수이면 건너뛰기
    if i % 6 == 0:
        continue

    # 각 순위(행)에 대한 CSS 셀렉터
    rank_selector = f"#app > div.root > main > div:nth-child(2) > div.container.container--mfit > table > tbody > tr:nth-child({i}) > td.rank.rank.rank--ko > div.current"
    channel_selector = f"#app > div.root > main > div:nth-child(2) > div.container.container--mfit > table > tbody > tr:nth-child({i}) > td.name > a > h3"
    views_selector = f"#app > div.root > main > div:nth-child(2) > div.container.container--mfit > table > tbody > tr:nth-child({i}) > td:nth-child(4) > span > span"

    rank_tag = soup.select_one(rank_selector)
    channel_tag = soup.select_one(channel_selector)
    views_tag = soup.select_one(views_selector)
    
    # 구조가 예상과 다르거나 없는 경우는 무시
    if not (rank_tag and channel_tag and views_tag):
        break

    rank = rank_tag.get_text(strip=True)
    channel = channel_tag.get_text(strip=True)
    views = views_tag.get_text(strip=True)

    data_list.append({
        "rank": rank,
        "channel": channel,
        "views": views
    })

# 결과 출력
for item in data_list:
    print(f"Rank: {item['rank']}, Channel: {item['channel']}, Views: {item['views']}")