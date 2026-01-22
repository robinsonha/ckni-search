# ckni-search
Search the CKNI database for drug-pathway association evidence and return EN papers

**Setup**
```
pip install httpx beautifulsoup4 pydantic
```
**Example usage**
```
from cnki_client import CNKISearch

cnki = CNKISearch()
papers = cnki.search("人工智能")
```
