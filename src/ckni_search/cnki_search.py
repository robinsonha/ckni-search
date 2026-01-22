from typing import List, Dict
from datetime import datetime
from .config import PATHWAYS, CNKI_WRAPPERS, CNKI_MAX_PAGES
from .magic_cnki import MagicCNKI

def generate_cnki_queries(phytochemicals: List[Dict], pathways=PATHWAYS, start_date=None, end_date=None) -> List[Dict]:
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")

    queries = []
    for phytochem in phytochemicals:
        for pathway in pathways:
            query_text = f"{CNKI_WRAPPERS['REGARDING']}{phytochem['chinese']}{CNKI_WRAPPERS['AND']}{pathway}{CNKI_WRAPPERS['RESEARCH']}"
            queries.append({
                "phytochemical_english": phytochem["name"],
                "phytochemical_chinese": phytochem["chinese"],
                "pathway": pathway,
                "query": query_text,
                "start_date": start_date,
                "end_date": end_date
            })
    return queries

def search_cnki_for_queries(queries: List[Dict], max_pages=CNKI_MAX_PAGES) -> List[Dict]:
    mc = MagicCNKI()
    all_results = []
    for query_info in queries:
        try:
            results = list(mc.search(query=query_info['query']))
            for result in results:
                result.update({
                    "agent": query_info['phytochemical_english'],
                    "agent_chinese": query_info['phytochemical_chinese'],
                    "pathway": query_info['pathway'],
                    "search_query": query_info['query'],
                })
                all_results.append(result)
        except Exception:
            continue
    return all_results
