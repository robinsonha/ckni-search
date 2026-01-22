from pprint import pprint
from .config import CNKI_WRAPPERS, PATHWAYS, CNKI_MAX_PAGES, CNKI_TIMEOUT_SECONDS

def generate_cnki_queries(phytochemicals, pathways=PATHWAYS, start_date=None, end_date=None):
    """Generate CNKI search queries for each drug and all pathways."""
    queries = []
    for phytochem in phytochemicals:
        for pathway in pathways:
            chi_query = f"{CNKI_WRAPPERS['REGARDING']}{phytochem['chinese']}" \
                        f"{CNKI_WRAPPERS['AND']}{pathway}" \
                        f"{CNKI_WRAPPERS['PATHWAY_IN']}{CNKI_WRAPPERS['RESEARCH']}"
            queries.append({
                "phytochemical_english": phytochem["name"],
                "phytochemical_chinese": phytochem["chinese"],
                "pathway": pathway,
                "query": chi_query,
                "start_date": start_date,
                "end_date": end_date
            })
    return queries

def search_cnki_for_queries(queries, max_pages=CNKI_MAX_PAGES):
    """Search CNKI for each query using MagicCNKI."""
    from MagicCNKI import MagicCNKI
    mc = MagicCNKI()
    all_results = []

    for query_info in queries:
        try:
            results = list(mc.search(query=query_info['query'], start=max_pages))
            for result in results:
                result.update({
                    "agent": query_info['phytochemical_english'],
                    "agent_chinese": query_info['phytochemical_chinese'],
                    "pathway": query_info['pathway'],
                    "search_query": query_info['query'],
                    "paper_url": result.get('url', ''),
                    "cnki_id": {}
                })
                all_results.append(result)
                pprint(result)
        except Exception as e:
            print(f"Error searching CNKI: {e}")
            continue
    return all_results

