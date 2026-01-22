import argparse
import json
from .config import OUTPUT_TRANSLATIONS_FILE, OUTPUT_RESULTS_FILE, PATHWAYS, START_DATE, END_DATE
from .translator import PhytochemicalTranslator
from .cnki_search import generate_cnki_queries, search_cnki_for_queries

def main():
    parser = argparse.ArgumentParser(description="Run ckni_search pipeline")
    parser.add_argument(
        "--start_date", type=str, default=START_DATE,
        help="Start date for CNKI search (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--end_date", type=str, default=END_DATE,
        help="End date for CNKI search (YYYY-MM-DD). Default is None (up to today)."
    )
    parser.add_argument(
        "--drugs", type=str, nargs="+", required=True,
        help="List of drug/phytochemical names in English"
    )
    args = parser.parse_args()
    start_date = args.start_date
    end_date = args.end_date
    drug_list = args.drugs

    translator = PhytochemicalTranslator()
    phytochemicals_data = translator.process_list(drug_list)

    with open(OUTPUT_TRANSLATIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(phytochemicals_data, f, ensure_ascii=False, indent=2)
    print(f"Saved translated phytochemicals to {OUTPUT_TRANSLATIONS_FILE}")

    queries = generate_cnki_queries(
        phytochemicals=phytochemicals_data,
        pathways=PATHWAYS,
        start_date=start_date,
        end_date=end_date
    )
    print(f"Generated {len(queries)} queries for {len(phytochemicals_data)} drugs across {len(PATHWAYS)} pathways")

    search_results = search_cnki_for_queries(queries)

    with open(OUTPUT_RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(search_results, f, ensure_ascii=False, indent=2)
    print(f"Saved search results to {OUTPUT_RESULTS_FILE}")

if __name__ == "__main__":
    main()
