import os
import json
import requests
import re
import html

class SearchService:
    def __init__(self, data_source=None):
        # data_source가 없으면 기본 샘플 데이터 사용
        if data_source is None:
            self.data = [
                {"title": "파이썬 튜토리얼", "url": "/tutorial/python", "snippet": "파이썬 기초 문법 소개"},
                {"title": "Flask 시작하기", "url": "/tutorial/flask", "snippet": "Flask로 웹앱 만드는 법"},
                {"title": "데이터 과학 입문", "url": "/tutorial/data-science", "snippet": "Pandas와 NumPy 기초"},
            ]
        # data_source가 파일 경로(문자열)이면 JSON으로 로드
        elif isinstance(data_source, str) and os.path.exists(data_source):
            with open(data_source, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            # 리스트 등 직접 전달된 데이터 사용
            self.data = data_source

        # 네이버 API 자격증명 감지 (환경변수)
        self.naver_id = os.getenv("NAVER_CLIENT_ID")
        self.naver_secret = os.getenv("NAVER_CLIENT_SECRET")
        self.use_naver_by_default = bool(self.naver_id and self.naver_secret)

    def _strip_tags(self, text):
        if not text:
            return ""
        return re.sub(r"<[^>]*>", "", text)

    def _naver_search(self, query, display=10, start=1, sort="sim"):
        # 입력 검사
        query = (query or "").strip()
        if not query:
            print("빈 검색어로 API 호출을 시도하지 않습니다.")
            return []

        # credential: 환경변수 우선, 없으면 폴백(대화에서 제공한 값)
        client_id = self.naver_id or "sqWgHCKu5b3_yHTZiDUh"
        client_secret = self.naver_secret or "JxukUX4Sba"

        # 파라미터 유효성 검사 (네이버 API 제한 고려)
        try:
            display = int(display)
            if display <= 0 or display > 100:
                display = 10
        except Exception:
            display = 10
        try:
            start = int(start)
            if start < 1:
                start = 1
            if start > 1000:
                start = 1000
        except Exception:
            start = 1

        url = "https://openapi.naver.com/v1/search/blog.json"
        headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret
        }
        params = {
            "query": query,
            "display": display,
            "start": start,
            "sort": sort
        }

        try:
            resp = requests.get(url, headers=headers, params=params, timeout=7)
            # 디버깅 정보 출력
            try:
                print("요청 URL:", resp.request.url)
            except Exception:
                pass
            print("응답 상태 코드:", resp.status_code)

            if resp.status_code != 200:
                # 가능한 상세 오류 메세지 출력
                try:
                    err = resp.json()
                except Exception:
                    err = resp.text
                print("네이버 API 오류 응답:", err)
                return []

            data = resp.json()
            items = []
            for item in data.get("items", []):
                items.append({
                    "title": html.unescape(self._strip_tags(item.get("title", ""))),
                    "url": item.get("link", ""),
                    "snippet": html.unescape(self._strip_tags(item.get("description", "")))
                })
            return items

        except requests.exceptions.RequestException as e:
            print("네트워크/요청 예외:", str(e))
            return []
        except Exception as e:
            print("검색 중 알 수 없는 오류:", str(e))
            return []

    def search(self, query, use_naver=None):
        """
        query: 검색어
        use_naver: True/False/None. None이면 환경변수로 결정(use_naver_by_default).
        """
        if not query:
            return []
        if use_naver is None:
            use_naver = self.use_naver_by_default
        if use_naver:
            return self._naver_search(query)
        # 로컬 검색(기존 방식)
        q = query.lower()
        results = []
        for item in (self.data or []):
            title = item.get("title", "").lower()
            snippet = item.get("snippet", "").lower()
            if q in title or q in snippet:
                results.append(item)
        return results

    def get_suggestions(self, query):
        if not query:
            return []
        suggestions = []
        q = query.lower()
        for item in (self.data or []):
            title = item.get("title", "").lower()
            if title.startswith(q):
                suggestions.append(item.get("title"))
        return suggestions