import re
import time
from typing import List, Dict, Optional
from googletrans import Translator
from .config import (
    SUFFIXES_TO_REMOVE, TRANSLATION_SOURCE_LANGUAGE, TRANSLATION_TARGET_LANGUAGE,
    TRANSLATION_MAX_RETRIES, TRANSLATION_RETRY_SLEEP_SECONDS, TRANSLATION_FAILURE_TOKEN
)

class PhytochemicalTranslator:
    def __init__(self):
        self.translator = Translator()
        self.common_aliases = {}
        self.suffixes_to_remove = SUFFIXES_TO_REMOVE

    def clean_name(self, name: str) -> str:
        name = name.lower().strip()
        for suffix in self.suffixes_to_remove:
            if name.endswith(suffix):
                name = name[:-len(suffix)]
        name = re.sub(r'\([^)]*\)', '', name).strip()
        name = re.sub(r'\d+%\s*', '', name).strip()
        return name.title()

    def get_aliases(self, name: str) -> List[str]:
        return self.common_aliases.get(name.lower(), [])

    def translate_to_chinese(self, text: str, max_retries: int = TRANSLATION_MAX_RETRIES) -> Optional[str]:
        for attempt in range(max_retries):
            try:
                clean_text = self.clean_name(text)
                translation = self.translator.translate(
                    clean_text,
                    src=TRANSLATION_SOURCE_LANGUAGE,
                    dest=TRANSLATION_TARGET_LANGUAGE
                )
                if translation and translation.text:
                    return translation.text
            except Exception:
                if attempt < max_retries - 1:
                    time.sleep(TRANSLATION_RETRY_SLEEP_SECONDS)
                else:
                    return TRANSLATION_FAILURE_TOKEN
        return TRANSLATION_FAILURE_TOKEN

    def process_list(self, phytochemicals: List[str]) -> List[Dict]:
        results = []
        for phytochem in phytochemicals:
            clean_name = self.clean_name(phytochem)
            chinese_name = self.translate_to_chinese(phytochem)
            aliases = self.get_aliases(clean_name)
            results.append({
                "name": clean_name,
                "chinese": chinese_name or TRANSLATION_FAILURE_TOKEN,
                "aliases": aliases,
                "original_name": phytochem
            })
        return results
