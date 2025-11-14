from flask import Blueprint, render_template, request, jsonify, current_app
from .services.search_service import SearchService

bp = Blueprint('main', __name__)
search_service = SearchService()

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search')
def search():
    q = request.args.get('q', '').strip()
    results = search_service.search(q, use_naver=True)  # 네이버 검색 강제 활성화
    
    # 디버그 출력
    print(f"검색어: {q}")
    print(f"검색 결과: {results}")
    
    return render_template('search_results.html', query=q, results=results)

@bp.route('/suggest')
def suggest():
    q = request.args.get('q', '').strip()
    suggestions = search_service.get_suggestions(q)
    return jsonify(suggestions)