# naver_api.py
import urllib.request
import urllib.parse
import json

def get_blog_search_results(query, client_id, client_secret):
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