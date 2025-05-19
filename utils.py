# utils.py
def print_blog_results(results):
    if results:
        print("\n--- 검색 결과 ---")
        for item in results:
            clean_title = item['title'].replace("<b>", "").replace("</b>", "")

            print("제목:", clean_title)
            print("링크:", item['link'])
            print("블로거 이름:", item['bloggername'])
            print("작성일:", item['postdate'])
            print("-" * 20)
    else:
        print("검색 결과가 없습니다.")