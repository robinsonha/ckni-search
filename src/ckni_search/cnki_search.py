from pprint import pprint
from .config import CNKI_WRAPPERS, PATHWAYS, CNKI_MAX_PAGES

from .cnki_scraper import search_cnki
from .config import CNKI_MAX_PAGES

def run_cnki_pipeline(phytochemicals, start_date=None, end_date=None, output_file=OUTPUT_RESULTS_FILE):
    queries = generate_cnki_queries(phytochemicals, start_date, end_date)

    all_search_results = []
    for q in queries:
        results = search_cnki(q["query"], max_pages=CNKI_MAX_PAGES)
        for r in results:
            r.update({
                "phytochemical": q["phytochemical_english"],
                "chinese": q["phytochemical_chinese"],
                "pathway": q["pathway"],
                "search_query": q["query"]
            })
            all_search_results.append(r)

    # always write final results
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_search_results, f, ensure_ascii=False, indent=2)

    print(f"CNKI pipeline completed. Results saved to {output_file}")
    return all_search_results
