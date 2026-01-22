# ckni-search
Search the CKNI database for drug-pathway association evidence and return EN papers

**Setup**
```
pip install httpx beautifulsoup4 pydantic
```
**Example usage**
```
python -m ckni_search.main --start_date 2020-01-01 --end_date 2023-12-31
```
