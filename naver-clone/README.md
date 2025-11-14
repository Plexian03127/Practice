# naver-clone 프로젝트

이 프로젝트는 Flask를 사용하여 네이버와 유사한 검색 사이트를 구현한 것입니다. 사용자는 검색어를 입력하고, 관련된 검색 결과를 확인할 수 있습니다.

## 프로젝트 구조

```
naver-clone
├── app
│   ├── __init__.py          # Flask 애플리케이션 초기화
│   ├── routes.py            # 애플리케이션의 라우트 정의
│   ├── models.py            # 데이터베이스 모델 정의
│   ├── services
│   │   └── search_service.py # 검색 기능 구현
│   ├── templates
│   │   ├── base.html        # 기본 HTML 템플릿
│   │   ├── index.html       # 메인 페이지
│   │   ├── search_results.html # 검색 결과 페이지
│   │   └── partials
│   │       └── _search_form.html # 검색 폼 부분 템플릿
│   └── static
│       ├── css
│       │   └── styles.css   # 스타일 정의
│       └── js
│           └── main.js      # JavaScript 기능 정의
├── tests
│   ├── test_search.py       # 검색 서비스 단위 테스트
│   └── conftest.py          # 테스트 환경 설정
├── requirements.txt          # 필요한 Python 패키지 목록
├── config.py                 # 애플리케이션 설정
├── run.py                    # 애플리케이션 실행 스크립트
├── .env                      # 환경 변수 정의
└── README.md                 # 프로젝트 문서화
```

## 설치 방법

1. 이 저장소를 클론합니다.
   ```
   git clone <repository-url>
   cd naver-clone
   ```

2. 가상 환경을 생성하고 활성화합니다.
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. 필요한 패키지를 설치합니다.
   ```
   pip install -r requirements.txt
   ```

4. 환경 변수를 설정합니다. `.env` 파일을 수정하여 필요한 값을 입력합니다.

## 사용법

1. 애플리케이션을 실행합니다.
   ```
   python run.py
   ```

2. 웹 브라우저에서 `http://127.0.0.1:5000`에 접속합니다.

3. 검색어를 입력하고 검색 버튼을 클릭하여 결과를 확인합니다.

## 기여

기여를 원하시는 분은 이 저장소를 포크한 후, 변경 사항을 커밋하고 풀 리퀘스트를 제출해 주세요.

## 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다.