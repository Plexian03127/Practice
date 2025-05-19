# main.py
import os
import sys
# 다른 파일에서 정의한 함수 가져오기
from naver_api import get_blog_search_results
from utils import print_blog_results

def main():
    """
    프로그램의 메인 실행 함수
    """
    print("네이버 맛집 검색 프로그램")

    # 네이버 API 키 정보 (실제 키로 바꿔 사용하세요)
    # 이 정보는 민감할 수 있으므로 별도의 설정 파일 등으로 관리하는 것이 더 안전합니다.
    client_id = "sqWgHCKu5b3_yHTZiDUh" # 여기에 실제 클라이언트 ID를 넣어주세요
    client_secret = "JxukUX4Sba" # 여기에 실제 클라이언트 Secret을 넣어주세요

    # 사용자로부터 검색어 입력 받기
    search_query = input("검색할 맛집 지역 또는 이름을 입력하세요: ")

    # naver_api 모듈의 함수를 사용하여 검색 결과 가져오기
    blog_results = get_blog_search_results(search_query, client_id, client_secret)

    # utils 모듈의 함수를 사용하여 결과 출력하기
    print_blog_results(blog_results)

    print("프로그램을 종료합니다.")

# 스크립트가 직접 실행될 때 main 함수 호출
if __name__ == "__main__":
    main()