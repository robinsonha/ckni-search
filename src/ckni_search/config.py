# Default configuration and constants for ckni_search

START_DATE = "2015-01-01"
END_DATE = None  # None = up to today
ENABLE_DATE_FILTERING = True

TRANSLATION_SOURCE_LANGUAGE = "en"
TRANSLATION_TARGET_LANGUAGE = "zh-cn"
TRANSLATION_MAX_RETRIES = 3
TRANSLATION_RETRY_SLEEP_SECONDS = 1.0
TRANSLATION_RATE_LIMIT_SECONDS = 0.5
TRANSLATION_FAILURE_TOKEN = "TRANSLATION_FAILED"

SUFFIXES_TO_REMOVE = [
    " extract", " extract standardized", " standardized extract", " powder", 
    " oil", " essential oil", " leaf extract", " root extract", " bark extract", 
    " purified", " concentrate"
]

CNKI_WRAPPERS = {
    "REGARDING": "关于",
    "AND": "与",
    "PATHWAY_IN": "通路在",
    "RESEARCH": "的研究",
}

PATHWAYS = [
    "PI3K/Akt信号通路",
    "MAPK信号通路",
    "Wnt/β-连环蛋白通路",
    "NF-κB信号通路",
    "p53信号通路",
    "细胞凋亡通路",
    "血管生成通路",
    "上皮间质转化通路",
    "JAK/STAT信号通路",
    "TGF-β信号通路",
    "Notch信号通路",
    "Hedgehog信号通路",
    "mTOR信号通路",
    "HIF-1α信号通路",
    "DNA损伤修复通路",
    "细胞周期通路",
    "自噬通路",
    "代谢通路",
    "炎症通路",
    "氧化应激通路",
    "雌激素受体通路",
    "雄激素受体通路",
    "HER2信号通路",
    "VEGF信号通路",
    "RAS信号通路",
]

CNKI_MAX_PAGES = 2
CNKI_TIMEOUT_SECONDS = 20
OUTPUT_TRANSLATIONS_FILE = "phytochemicals.json"
OUTPUT_RESULTS_FILE = "cnki_search_results.json"
