from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class Summarizer:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPEN_AI_KEY'))
        self.model = "gpt-3.5-turbo"
    
    def summarize_text(self, text, language_code="en", summary_type="brief"):
        language_names = {
            "en": "English", "tr": "Türkçe", "de": "Deutsch", "fr": "Français", 
            "es": "Español", "it": "Italiano", "pt": "Português", "ru": "Русский",
            "ar": "العربية", "zh": "中文", "ja": "日本語"
        }
        
        if summary_type == "brief":
            max_tokens = 300
            if language_code == "tr":
                instruction = "kısa özet (150 kelime altı) Türkçe olarak"
            else:
                lang_name = language_names.get(language_code, "English")
                instruction = f"brief summary (under 150 words) in {lang_name}"
        else:
            max_tokens = 600
            if language_code == "tr":
                instruction = "detaylı özet (400 kelime altı) Türkçe olarak"
            else:
                lang_name = language_names.get(language_code, "English")
                instruction = f"detailed summary (under 400 words) in {lang_name}"
        
        if language_code == "tr":
            prompt = f"Bu metnin {instruction} hazırla:\n\n{text[:4000]}"
        else:
            prompt = f"Create a {instruction} of this text:\n\n{text[:4000]}"
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.3
            )
            return True, response.choices[0].message.content
        except Exception as e:
            return False, f"Summary error: {str(e)}"
    
    def extract_keywords(self, text, language_code="en"):
        language_names = {
            "en": "English", "tr": "Türkçe", "de": "Deutsch", "fr": "Français",
            "es": "Español", "it": "Italiano", "pt": "Português", "ru": "Русский",
            "ar": "العربية", "zh": "中文", "ja": "日本語"
        }
        
        if language_code == "tr":
            prompt = f"Bu metinden 5-8 anahtar kelime/cümle çıkar Türkçe olarak (virgülle ayır):\n\n{text[:2000]}"
        else:
            lang_name = language_names.get(language_code, "English")
            prompt = f"Extract 5-8 key words/phrases from this text in {lang_name} (comma separated):\n\n{text[:2000]}"
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.2
            )
            return True, response.choices[0].message.content
        except Exception as e:
            return False, f"Keywords error: {str(e)}"