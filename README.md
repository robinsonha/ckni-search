# ckni-search
Allows API search of CNKI which is a multilingual portal to the largest Chinese academic literature database, searches the CKNI database for drug-pathway association evidence and returns papers in English- the API is currently in Chinese only
We use the google translate API to translate pathway names of interest and phytopharmaceuticals

**Setup**
```bash
python -m venv venv
venv\Scripts\activate      # windows

pip install -e .
```
**Example usage**
```
from ckni_search.translator import PhytochemicalTranslator
from ckni_search.cnki_search import generate_cnki_queries

drugs = ["Curcumin", "Resveratrol", "Quercetin"]

translator = PhytochemicalTranslator()
phytochemicals_data = translator.process_list(drugs)

queries = generate_cnki_queries(
    phytochemicals=phytochemicals_data,
    start_date="2020-01-01",
    end_date="2023-12-31"
)

for q in queries[:5]:
    print(q)
```
--end_date is optional; defaults to today.

--All default paths and constants are in config.py.
