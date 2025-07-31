from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class QAEngine:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPEN_AI_KEY'))
        self.model = "gpt-3.5-turbo"
    
    def analyze_pdf(self, text, language_code="en"):
        language_names = {
            "en": "English", "tr": "Türkçe", "de": "Deutsch", "fr": "Français",
            "es": "Español", "it": "Italiano", "pt": "Português", "ru": "Русский", 
            "ar": "العربية", "zh": "中文", "ja": "日本語"
        }
        
        if language_code == "tr":
            prompt = f"Bu PDF metnini kısaca Türkçe analiz et. Şunları ver: 1) Ana konu 2) Önemli noktalar 3) Özet (max 200 kelime):\n\n{text[:3000]}"
        else:
            lang_name = language_names.get(language_code, "English")
            prompt = f"Analyze this PDF text briefly in {lang_name}. Provide: 1) Main topic 2) Key points 3) Summary (max 200 words):\n\n{text[:3000]}"
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=600,
                temperature=0.3
            )
            return True, response.choices[0].message.content
        except Exception as e:
            return False, f"Analysis error: {str(e)}"
    
    def answer_question(self, text, question, language_code="en"):
        language_names = {
            "en": "English", "tr": "Türkçe", "de": "Deutsch", "fr": "Français",
            "es": "Español", "it": "Italiano", "pt": "Português", "ru": "Русский",
            "ar": "العربية", "zh": "中文", "ja": "日本語"
        }
        
        if language_code == "tr":
            prompt = f"Bu soruyu PDF metnine dayanarak Türkçe cevapla (cevabı 100 kelime altında tut):\n\nSoru: {question}\n\nMetin: {text[:2000]}"
        else:
            lang_name = language_names.get(language_code, "English")
            prompt = f"Answer this question in {lang_name} based on the PDF text (keep answer under 100 words):\n\nQuestion: {question}\n\nText: {text[:2000]}"
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.2
            )
            return True, response.choices[0].message.content
        except Exception as e:
            return False, f"Question error: {str(e)}"