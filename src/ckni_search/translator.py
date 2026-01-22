import re
import time
from typing import List, Dict, Optional
from googletrans import Translator
from .config import (
    TRANSLATION_SOURCE_LANGUAGE,
    TRANSLATION_TARGET_LANGUAGE,
    TRANSLATION_MAX_RETRIES,
    TRANSLATION_RETRY_SLEEP_SECONDS,
    TRANSLATION_RATE_LIMIT_SECONDS,
    TRANSLATION_FAILURE_TOKEN,
    SUFFIXES_TO_REMOVE
)

class PhytochemicalTranslator:
    def __init__(self):
        self.translator = Translator()
        self.suffixes_to_remove = SUFFIXES_TO_REMOVE
        self.failure_token = TRANSLATION_FAILURE_TOKEN
        self.retry_sleep = TRANSLATION_RETRY_SLEEP_SECONDS
        self.rate_limit = TRANSLATION_RATE_LIMIT_SECONDS
        self.max_retries = TRANSLATION_MAX_RETRIES

    def clean_name(self, name: str) -> str:
        name = name.lower().strip()
        for suffix in self.suffixes_to_remove:
            if name.endswith(suffix):
                name = name[:-len(suffix)]
        # Remove content in parentheses and percentages
        name = re.sub(r'\([^)]*\)', '', name).strip()
        name = re.sub(r'\d+%\s*', '', name).strip()
        return name.title()

    def translate_to_chinese(self, text: str) -> Optional[str]:
        for attempt in range(self.max_retries):
            try:
                clean_text = self.clean_name(text)
                translation = self.translator.translate(
                    clean_text,
                    src=TRANSLATION_SOURCE_LANGUAGE,
                    dest=TRANSLATION_TARGET_LANGUAGE
                )
                if translation and translation.text:
                    time.sleep(self.rate_limit)
                    return translation.text
            except Exception:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_sleep)
                else:
                    return self.failure_token
        return self.failure_token

    def process_list(self, phytochemicals: List[str]) -> List[Dict]:
        results = []
        
        print(f"Processing {len(phytochemicals)} phytochemicals...")
        print("=" * 60)

        for i, phytochem in enumerate(phytochemicals, 1):
            clean_name = self.clean_name(phytochem)
            chinese_name = self.translate_to_chinese(phytochem)
            aliases = self.get_aliases(clean_name)

            if not chinese_name and clean_name != phytochem.lower():
                chinese_name = self.translate_to_chinese(clean_name)

            result = {
                "name": clean_name,
                "chinese": chinese_name or "TRANSLATION_FAILED",
                "aliases": aliases,
                "original_name": phytochem
            }
            results.append(result)

            print(f"[{i}/{len(phytochemicals)}] {phytochem} -> {chinese_name or 'FAILED'}")
            if i < len(phytochemicals):
                time.sleep(0.5)  # rate limiting

        print("=" * 60)
        print(f"Processing complete! {len([r for r in results if r['chinese'] != 'TRANSLATION_FAILED'])}/{len(results)} successfully translated.")
        return results
