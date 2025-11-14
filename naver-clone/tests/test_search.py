import pytest
from app.services.search_service import SearchService

@pytest.fixture
def search_service():
    return SearchService()

def test_search_valid_query(search_service):
    query = "Flask"
    results = search_service.search(query)
    assert isinstance(results, list)
    assert len(results) > 0

def test_search_empty_query(search_service):
    query = ""
    results = search_service.search(query)
    assert results == []

def test_search_no_results(search_service):
    query = "nonexistentquery"
    results = search_service.search(query)
    assert results == []