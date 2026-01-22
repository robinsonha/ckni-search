from bs4 import BeautifulSoup
from .models import CNKIArticle

def parse_search_results(html: str) -> list[CNKIArticle]:
    soup = BeautifulSoup(html, "lxml")
    results = []

    for row in soup.select(".result-table-list tr"):
        cols = row.select("td")
        if len(cols) < 4:
            continue

        results.append(
            CNKIArticle(
                title=cols[0].get_text(strip=True),
                authors=cols[1].get_text(strip=True),
                source=cols[2].get_text(strip=True),
                year=cols[3].get_text(strip=True)
            )
        )

    return results
