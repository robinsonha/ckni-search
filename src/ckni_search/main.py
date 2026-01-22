import argparse
from phytocnki import config
from phytocnki.translator import PhytochemicalTranslator
from phytocnki.cnki_search import generate_cnki_queries, search_cnki_for_queries

def main():
    parser = argparse.ArgumentParser(description="Run CNKI search pipeline")
    parser.add_argument(
        "--start_date",
        type=str,
        required=True,
        help="Start date for search (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--end_date",
        type=str,
        default=None,
        help="End date for search (YYYY-MM-DD). Defaults to today if omitted."
    )
    args = parser.parse_args()

    start_date = args.start_date
    end_date = args.end_date or None

    # Load phytochemicals
    import json
    with open(config.OUTPUT_TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        phytochemicals_data = json.load(f)

    # Generate CNKI queries
    queries = generate_cnki_queries(
        phytochemicals=phytochemicals_data,
        pathways=config.PATHWAYS,
        start_date=start_date,
        end_date=end_date
    )
    print(f"Generated {len(queries)} queries from {start_date} to {end_date or 'today'}")

    # Execute searches
    search_results = search_cnki_for_queries(
        queries,
        max_pages=config.CNKI_MAX_PAGES
    )

    # Save results
    with open(config.OUTPUT_RESULTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(search_results, f, ensure_ascii=False, indent=2)
    print(f"Saved search results to {config.OUTPUT_RESULTS_FILE}")


if __name__ == "__main__":
    main()
