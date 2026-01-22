# ckni-search
Allows API search of CNKI which is a multilingual portal to the largest Chinese academic literature database, searches the CKNI database for drug-pathway association evidence and returns papers in English- the API is currently in Chinese only
We use the google translate API to translate pathway names of interest and phytopharmaceuticals

**Setup**
```
pip install httpx beautifulsoup4 pydantic
```
**Example usage**
```
python -m ckni_search.main --start_date 2020-01-01 --end_date 2023-12-31 \
    --drugs Curcumin Resveratrol "Sodium Phenyl Butyrate"
```
--end_date is optional; defaults to today.

--All default paths and constants are in config.py.
