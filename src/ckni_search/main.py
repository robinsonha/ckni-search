import argparse
import json
from .config import OUTPUT_TRANSLATIONS_FILE, OUTPUT_RESULTS_FILE, PATHWAYS
from .translator import PhytochemicalTranslator
from .cnki_search import generate_cnki_queries, search_cnki_for_queries

def main():
    parser = argparse.ArgumentParser(description="Run ckni_search pipeline")
    parser.add_argument("--start_date", type=str, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end_date", type=str, default=None, help="End date (YYYY-MM-DD). Defaults to today if omitted.")
    args = parser.parse_args()

    start_date = args.start_date
    end_date = args.end_date

    # Load phytochemicals
    with open(OUTPUT_TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
        phytochemicals_data = json.load(f)

    # Generate CNKI queries
    queries = generate_cnki_queries(phytochemicals_data, pathways=PATHWAYS, start_date=start_date, end_date=end_date)
    print(f"Generated {len(queries)} queries from {start_date} to {end_date or 'today'}")

    # Execute searches
    search_results = search_cnki_for_queries(queries)

    # Save results
    with open(OUTPUT_RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(search_results, f, ensure_ascii=False, indent=2)
    print(f"Saved search results to {OUTPUT_RESULTS_FILE}")


if __name__ == "__main__":
    main()

