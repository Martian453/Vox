from slang_translator import translate_slang

text = "can you send me the documents"
target_lang = "Hindi"

translated = translate_slang(text, target_lang)
print("Translated message: ", translated)