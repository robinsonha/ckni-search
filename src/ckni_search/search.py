from .client import CNKIClient
from .parser import parse_search_results
from .models import CNKIArticle

class CNKISearch:
    SEARCH_URL = "https://kns.cnki.net/kns8/defaultresult/index"

    def __init__(self, client: CNKIClient | None = None):
        self.client = client or CNKIClient()

    def search(self, keyword: str, page: int = 1) -> list[CNKIArticle]:
        params = {
            "kw": keyword,
            "page": page
        }
        response = self.client.get(self.SEARCH_URL, params=params)
        return parse_search_results(response.text)
