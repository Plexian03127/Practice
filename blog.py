import os
import sys
from naver_api import get_blog_search_results
from utils import print_blog_results

def main():
    print("네이버 맛집 검색 프로그램")

    search_query = input("검색할 맛집 지역 또는 이름을 입력하세요: ")

    blog_results = get_blog_search_results(search_query, client_id, client_secret)

    print_blog_results(blog_results)

    print("프로그램을 종료합니다.")

if __name__ == "__main__":
    main()