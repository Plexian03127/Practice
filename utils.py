# utils.py
def print_blog_results(results):
    """
    검색 결과를 보기 좋게 출력하는 함수

    Args:
        results (list): 검색 결과 항목들의 리스트
    """
    if results:
        print("\n--- 검색 결과 ---")
        for item in results:
            # HTML 태그 제거 (예시)
            clean_title = item['title'].replace("<b>", "").replace("</b>", "")
            # clean_description = item['description'].replace("<b>", "").replace("</b>", "")

            print("제목:", clean_title)
            print("링크:", item['link'])
            print("블로거 이름:", item['bloggername'])
            print("작성일:", item['postdate'])
            print("-" * 20)
    else:
        print("검색 결과가 없습니다.")
#