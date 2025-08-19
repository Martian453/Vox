# slang_translator.py

import cohere
from config import COHERE_API_KEY

co = cohere.Client(COHERE_API_KEY)

def translate_slang(text: str, target_lang: str) -> str:
    """
    Translates slang-heavy English text into the target language
    while preserving the slang context.
    """
    prompt = f"Translate this slang-heavy English message to {target_lang}. Preserve slang:\n'{text}'"
    
    try:
        response = co.chat(model="command-r", message=prompt)
        return response.text.strip()
    except Exception as e:
        return f"Translation failed: {e}"
    