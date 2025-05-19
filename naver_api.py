# naver_api.py
import urllib.request
import urllib.parse
import json

def get_blog_search_results(query, client_id, client_secret):
    """
    네이버 블로그 검색 API를 호출하여 결과를 가져와 파싱하는 함수

    Args:
        query (str): 검색어
        client_id (str): 네이버 API 클라이언트 ID
        client_secret (str): 네이버 API 클라이언트 Secret

    Returns:
        list: 추출된 검색 결과 항목들의 리스트. 오류 발생 시 빈 리스트 반환.
    """
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    extracted_list = []
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            response_body = response.read()
            json_data = response_body.decode('utf-8')
            data = json.loads(json_data)

            if 'items' in data:
                for item in data['items']:
                    extracted_item = {
                        "title": item.get("title", ""),
                        "link": item.get("link", ""),
                        "description": item.get("description", ""),
                        "bloggername": item.get("bloggername", ""),
                        "postdate": item.get("postdate", "")
                    }
                    extracted_list.append(extracted_item)
        else:
            print(f"API 호출 실패. Error Code: {rescode}")
            extracted_list = []
    except Exception as e:
        print(f"API 호출 또는 데이터 처리 중 오류 발생: {e}")
        extracted_list = []

    return extracted_list