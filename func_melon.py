import requests
from bs4 import BeautifulSoup
import random
import time
import func

print("==========================")
print("| 1. 멜론 차트 TOP 100곡   |")
print("| 2. 멜론 차트 TOP 50곡    |")
print("| 3. 멜론 차트 TOP 10곡    |")
print("| 4. 멜론 차트 AI 추천곡   |")
print("| 5. 가수 이름 검색        |")
print("| 6. 노래 리스트 파일 저장 |")
print("==========================")

n = input("[원하시는 서비스에 해당하는 번호를 입력하세요.]: ")

if n == "1":
    print("<멜론 차트 TOP 100곡>")
    time.sleep(1)
    func.display(func.fetch(100))

elif n == "2":
    print("<멜론 차트 TOP 50곡>")
    time.sleep(1)
    func.display(func.fetch(50))

elif n == "3":
    print("<멜론 차트 TOP 10곡>")
    time.sleep(1)
    func.display(func.fetch(10))

elif n == "4":
    print("<멜론 차트 AI 추천곡>")
    time.sleep(1)
    print("[좋아요! 제가 열심히 찾아서 사용자님께 노래를 한 곡 추천할게요.]")
    time.sleep(1)
    print(f"[두구두구둥...]")
    time.sleep(1)
    func.ai()

elif n == "5":
    print("<가수 이름 검색>")
    time.sleep(1)
    s = input("[검색하고 싶은 가수의 이름을 입력하세요.]: ")
    print(f"[<{s}>의 노래를 검색 중이에요...]")
    time.sleep(1)
    func.search(s)

elif n == "6":
    func.save()

else:
    print(f"[<{n}>번에 해당하는 서비스가 없어요. 1~6번 중에 선택해 주세요.]")