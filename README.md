# ckni-search
Allows API search of CNKI which is a multilingual portal to the largest Chinese academic literature database, searches the CKNI database for evidence of associations between a phytopharmaceutical and a specific gene pathway, to return links to the papers in English
As the API is currently in Chinese only, we will use the google translate API to translate names of phytopharmaceuticals that we want to query into Chinese
There is then a wrapper template to create a full query in Chinese
This is part of Envita's work to look for drug-gene associations for precision cancer medicine

### Still to do

This code has been drafted but I have not had time to test it and get it working, it likely needs major revision

We know that mining the database was previously feasible, there is an old python package called magicCKNI that did this: https://github.com/1049451037/MagicCNKI
magicCKNI no longer works which implies the page setup or field names changed

Possibly what we want is now at https://oversea.cnki.net/ rather than at https://cnki.net/index/
It may be that we need to use a VPN with Chinese positioning

I have looked into webscraping with rvest and RSelenium in R, both seem deprecated or unsuitable (RSelenium only works with very old versions of Chrome and rvest will only scrape the start of html from pages) so we definitely need to use python

The authors of the original magicCKNI package may be interested in helping to create an open source update, I have not yet reached out to them

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
