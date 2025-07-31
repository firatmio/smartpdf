import os
import json
import threading
from tkinter import messagebox as mb

class LanguageManager:
    def __init__(self, app_folder, create_folder=True):
        self.app_folder = app_folder
        self.language_file = os.path.join(app_folder, "language.json")
        
        if create_folder:
            if not os.path.exists(app_folder):
                os.makedirs(app_folder, exist_ok=True)
                
            if not os.path.exists(self.language_file):
                try:
                    with open(self.language_file, 'w', encoding='utf-8') as f:
                        json.dump({}, f)
                except Exception as e:
                    print(f"Error creating language file: {e}")
        
        self.current_language = "en"
        self.translations = {}
        
        self.available_languages = {
            "en": "English", 
            "tr": "Türkçe",
            "de": "Deutsch",
            "fr": "Français",
            "es": "Español",
            "it": "Italiano",
            "pt": "Português",
            "ru": "Русский",
            "ar": "العربية",
            "zh": "中文",
            "ja": "日本語"
        }
        
        self.default_texts = {
            "app_title": "SmartPDF - Load and Analyze",
            "setup_title": "SmartPDF - Setup",
            "select_pdf": "Select PDF File",
            "analyze_info": "Upload PDF file and analyze it.\nAnalysis results will be displayed here.",
            "select_file": "Select File",
            "file_path_placeholder": "PDF file path",
            "analyze": "Analyze",
            "install": "Install",
            "setup_info": "SmartPDF application is starting for the first time.\nPlease click the 'Install' button to start the setup process.",
            "installing": "Installing...",
            "installation_complete": "Installation completed!",
            "starting_app": "Starting application...",
            "about_text": "Upload your PDF files and analyze them.",
            "language_selection": "Language:",
            "select_language": "Select Language",
            "settings": "Settings",
            "settings_title": "Settings",
            "change_language": "Change Language",
            "current_language": "Current Language:",
            "apply_changes": "Apply Changes",
            "cancel": "Cancel",
            "language_changed": "Language will be changed. The application will restart.",
            "confirm_language_change": "Confirm Language Change",
            "analyzing": "Analyzing PDF...",
            "analysis_complete": "Analysis Complete",
            "analysis_failed": "Analysis Failed",
            "summary": "Summary",
            "keywords": "Keywords",
            "ask_question": "Ask Question",
            "enter_question": "Enter your question about the PDF...",
            "ask": "Ask",
            "answer": "Answer",
            "no_pdf_selected": "Please select a PDF file first",
            "pdf_analysis": "PDF Analysis Results",
            "analysis_title": "Analysis",
            "thinking": "Thinking",
            "please_wait": "Please wait..."
        }
        
        self.predefined_translations = {
            "tr": {
                "app_title": "SmartPDF - Yükle ve Analiz Et",
                "setup_title": "SmartPDF - Kurulum",
                "select_pdf": "PDF Dosyası Seç",
                "analyze_info": "PDF dosyasını yükleyin ve analiz edin.\nAnaliz sonuçları burada görüntülenecektir.",
                "select_file": "Dosya Seç",
                "file_path_placeholder": "PDF dosya yolu",
                "analyze": "Analiz Et",
                "install": "Kur",
                "setup_info": "SmartPDF uygulaması ilk kez başlatılıyor.\nKurulum işlemini başlatmak için 'Kur' butonuna tıklayın.",
                "installing": "Kuruluyor...",
                "installation_complete": "Kurulum tamamlandı!",
                "starting_app": "Uygulama başlatılıyor...",
                "about_text": "PDF dosyalarınızı yükleyin ve analiz edin.",
                "language_selection": "Dil:",
                "select_language": "Dil Seç",
                "settings": "Ayarlar",
                "settings_title": "Ayarlar",
                "change_language": "Dil Değiştir",
                "current_language": "Mevcut Dil:",
                "apply_changes": "Değişiklikleri Uygula",
                "cancel": "İptal",
                "language_changed": "Dil değiştirilecek. Uygulama yeniden başlatılacak.",
                "confirm_language_change": "Dil Değişikliğini Onayla",
                "analyzing": "PDF Analiz Ediliyor...",
                "analysis_complete": "Analiz Tamamlandı",
                "analysis_failed": "Analiz Başarısız",
                "summary": "Özet",
                "keywords": "Anahtar Kelimeler",
                "ask_question": "Soru Sor",
                "enter_question": "PDF hakkında sorunuzu yazın...",
                "ask": "Sor",
                "answer": "Cevap",
                "no_pdf_selected": "Lütfen önce bir PDF dosyası seçin",
                "pdf_analysis": "PDF Analiz Sonuçları",
                "analysis_title": "Analiz",
                "thinking": "Düşünüyor",
                "please_wait": "Lütfen bekleyin..."
            },
            "de": {
                "app_title": "SmartPDF - Laden und Analysieren",
                "setup_title": "SmartPDF - Einrichtung",
                "select_pdf": "PDF-Datei Auswählen",
                "analyze_info": "PDF-Datei hochladen und analysieren.\nAnalyseergebnisse werden hier angezeigt.",
                "select_file": "Datei Auswählen",
                "file_path_placeholder": "PDF-Dateipfad",
                "analyze": "Analysieren",
                "install": "Installieren",
                "setup_info": "SmartPDF-Anwendung wird zum ersten Mal gestartet.\nBitte klicken Sie auf 'Installieren', um den Einrichtungsprozess zu starten.",
                "installing": "Installiere...",
                "installation_complete": "Installation abgeschlossen!",
                "starting_app": "Anwendung wird gestartet...",
                "about_text": "Laden Sie Ihre PDF-Dateien hoch und analysieren Sie sie.",
                "language_selection": "Sprache:",
                "select_language": "Sprache Auswählen",
                "settings": "Einstellungen",
                "settings_title": "Einstellungen",
                "change_language": "Sprache Ändern",
                "current_language": "Aktuelle Sprache:",
                "apply_changes": "Änderungen Übernehmen",
                "cancel": "Abbrechen",
                "language_changed": "Sprache wird geändert. Die Anwendung wird neu gestartet.",
                "confirm_language_change": "Sprachänderung Bestätigen",
                "analyzing": "PDF wird analysiert...",
                "analysis_complete": "Analyse abgeschlossen",
                "analysis_failed": "Analyse fehlgeschlagen",
                "summary": "Zusammenfassung",
                "keywords": "Stichwörter",
                "ask_question": "Frage stellen",
                "enter_question": "Geben Sie Ihre Frage zum PDF ein...",
                "ask": "Fragen",
                "answer": "Antwort",
                "no_pdf_selected": "Bitte wählen Sie zuerst eine PDF-Datei aus",
                "pdf_analysis": "PDF-Analyseergebnisse",
                "analysis_title": "Analyse",
                "thinking": "Denken",
                "please_wait": "Bitte warten..."
            },
            "fr": {
                "app_title": "SmartPDF - Charger et Analyser",
                "setup_title": "SmartPDF - Configuration",
                "select_pdf": "Sélectionner un Fichier PDF",
                "analyze_info": "Téléchargez un fichier PDF et analysez-le.\nLes résultats d'analyse seront affichés ici.",
                "select_file": "Sélectionner un Fichier",
                "file_path_placeholder": "Chemin du fichier PDF",
                "analyze": "Analyser",
                "install": "Installer",
                "setup_info": "L'application SmartPDF démarre pour la première fois.\nVeuillez cliquer sur 'Installer' pour commencer le processus de configuration.",
                "installing": "Installation...",
                "installation_complete": "Installation terminée!",
                "starting_app": "Lancement de l'application...",
                "about_text": "Téléchargez vos fichiers PDF et analysez-les.",
                "language_selection": "Langue:",
                "select_language": "Sélectionner la Langue",
                "settings": "Paramètres",
                "settings_title": "Paramètres",
                "change_language": "Changer de Langue",
                "current_language": "Langue Actuelle:",
                "apply_changes": "Appliquer les Modifications",
                "cancel": "Annuler",
                "language_changed": "La langue va être changée. L'application va redémarrer.",
                "confirm_language_change": "Confirmer le Changement de Langue",
                "analyzing": "Analyse du PDF...",
                "analysis_complete": "Analyse terminée",
                "analysis_failed": "Échec de l'analyse",
                "summary": "Résumé",
                "keywords": "Mots-clés",
                "ask_question": "Poser une question",
                "enter_question": "Entrez votre question sur le PDF...",
                "ask": "Demander",
                "answer": "Réponse",
                "no_pdf_selected": "Veuillez d'abord sélectionner un fichier PDF",
                "pdf_analysis": "Résultats de l'analyse PDF",
                "analysis_title": "Analyse",
                "thinking": "Réflexion en cours",
                "please_wait": "Veuillez patienter..."
            },
            "es": {
                "app_title": "SmartPDF - Cargar y Analizar",
                "setup_title": "SmartPDF - Configuración",
                "select_pdf": "Seleccionar Archivo PDF",
                "analyze_info": "Subir archivo PDF y analizarlo.\nLos resultados del análisis se mostrarán aquí.",
                "select_file": "Seleccionar Archivo",
                "file_path_placeholder": "Ruta del archivo PDF",
                "analyze": "Analizar",
                "install": "Instalar",
                "setup_info": "La aplicación SmartPDF se está iniciando por primera vez.\nPor favor, haga clic en 'Instalar' para comenzar el proceso de configuración.",
                "installing": "Instalando...",
                "installation_complete": "¡Instalación completada!",
                "starting_app": "Iniciando aplicación...",
                "about_text": "Suba sus archivos PDF y analícelos.",
                "language_selection": "Idioma:",
                "select_language": "Seleccionar Idioma",
                "settings": "Configuración",
                "settings_title": "Configuración",
                "change_language": "Cambiar Idioma",
                "current_language": "Idioma Actual:",
                "apply_changes": "Aplicar Cambios",
                "cancel": "Cancelar",
                "language_changed": "El idioma será cambiado. La aplicación se reiniciará.",
                "confirm_language_change": "Confirmar Cambio de Idioma",
                "analyzing": "Analizando PDF...",
                "analysis_complete": "Análisis completo",
                "analysis_failed": "Análisis fallido",
                "summary": "Resumen",
                "keywords": "Palabras clave",
                "ask_question": "Hacer una pregunta",
                "enter_question": "Escriba su pregunta sobre el PDF...",
                "ask": "Preguntar",
                "answer": "Respuesta",
                "no_pdf_selected": "Por favor, seleccione un archivo PDF primero",
                "pdf_analysis": "Resultados del análisis del PDF",
                "analysis_title": "Análisis",
                "thinking": "Pensando",
                "please_wait": "Por favor espere..."

            },
            "it": {
                "app_title": "SmartPDF - Carica e Analizza",
                "setup_title": "SmartPDF - Configurazione",
                "select_pdf": "Seleziona File PDF",
                "analyze_info": "Carica file PDF e analizzalo.\nI risultati dell'analisi verranno visualizzati qui.",
                "select_file": "Seleziona File",
                "file_path_placeholder": "Percorso del file PDF",
                "analyze": "Analizza",
                "install": "Installa",
                "setup_info": "L'applicazione SmartPDF si sta avviando per la prima volta.\nFai clic su 'Installa' per iniziare il processo di configurazione.",
                "installing": "Installazione...",
                "installation_complete": "Installazione completata!",
                "starting_app": "Avvio dell'applicazione...",
                "about_text": "Carica i tuoi file PDF e analizzali.",
                "language_selection": "Lingua:",
                "select_language": "Seleziona Lingua",
                "settings": "Impostazioni",
                "settings_title": "Impostazioni",
                "change_language": "Cambia Lingua",
                "current_language": "Lingua Attuale:",
                "apply_changes": "Applica Modifiche",
                "cancel": "Annulla",
                "language_changed": "La lingua verrà cambiata. L'applicazione si riavvierà.",
                "confirm_language_change": "Conferma Cambio Lingua",
                "analyzing": "Analizando PDF...",
                "analysis_complete": "Análisis completo",
                "analysis_failed": "Análisis fallido",
                "summary": "Resumen",
                "keywords": "Palabras clave",
                "ask_question": "Hacer una pregunta",
                "enter_question": "Escriba su pregunta sobre el PDF...",
                "ask": "Preguntar",
                "answer": "Respuesta",
                "no_pdf_selected": "Por favor, seleccione un archivo PDF primero",
                "pdf_analysis": "Resultados del análisis del PDF",
                "analysis_title": "Análisis",
                "thinking": "Pensando",
                "please_wait": "Por favor espere..."

            },
            "pt": {
                "app_title": "SmartPDF - Carregar e Analisar",
                "setup_title": "SmartPDF - Configuração",
                "select_pdf": "Selecionar Arquivo PDF",
                "analyze_info": "Carregue arquivo PDF e analise-o.\nOs resultados da análise serão exibidos aqui.",
                "select_file": "Selecionar Arquivo",
                "file_path_placeholder": "Caminho do arquivo PDF",
                "analyze": "Analisar",
                "install": "Instalar",
                "setup_info": "O aplicativo SmartPDF está iniciando pela primeira vez.\nClique em 'Instalar' para começar o processo de configuração.",
                "installing": "Instalando...",
                "installation_complete": "Instalação concluída!",
                "starting_app": "Iniciando aplicativo...",
                "about_text": "Carregue seus arquivos PDF e analise-os.",
                "language_selection": "Idioma:",
                "select_language": "Selecionar Idioma",
                "settings": "Configurações",
                "settings_title": "Configurações",
                "change_language": "Alterar Idioma",
                "current_language": "Idioma Atual:",
                "apply_changes": "Aplicar Alterações",
                "cancel": "Cancelar",
                "language_changed": "O idioma será alterado. O aplicativo será reiniciado.",
                "confirm_language_change": "Confirmar Alteração de Idioma",
                "analyzing": "Analisando PDF...",
                "analysis_complete": "Análise completa",
                "analysis_failed": "Falha na análise",
                "summary": "Resumo",
                "keywords": "Palavras-chave",
                "ask_question": "Fazer pergunta",
                "enter_question": "Digite sua pergunta sobre o PDF...",
                "ask": "Perguntar",
                "answer": "Resposta",
                "no_pdf_selected": "Por favor, selecione um arquivo PDF primeiro",
                "pdf_analysis": "Resultados da análise do PDF",
                "analysis_title": "Análise",
                "thinking": "Pensando",
                "please_wait": "Por favor, aguarde..."     
            },
            "ru": {
                "app_title": "SmartPDF - Загрузить и Анализировать",
                "setup_title": "SmartPDF - Настройка",
                "select_pdf": "Выберите PDF файл",
                "analyze_info": "Загрузите PDF файл и проанализируйте его.\nРезультаты анализа будут отображены здесь.",
                "select_file": "Выбрать файл",
                "file_path_placeholder": "Путь к PDF файлу",
                "analyze": "Анализировать",
                "install": "Установить",
                "setup_info": "Приложение SmartPDF запускается впервые.\nНажмите 'Установить', чтобы начать процесс настройки.",
                "installing": "Установка...",
                "installation_complete": "Установка завершена!",
                "starting_app": "Запуск приложения...",
                "about_text": "Загрузите ваши PDF файлы и анализируйте их.",
                "language_selection": "Язык:",
                "select_language": "Выбрать язык",
                "settings": "Настройки",
                "settings_title": "Настройки",
                "change_language": "Изменить язык",
                "current_language": "Текущий язык:",
                "apply_changes": "Применить изменения",
                "cancel": "Отмена",
                "language_changed": "Язык будет изменен. Приложение будет перезапущено.",
                "confirm_language_change": "Подтвердить изменение языка",
                "analyzing": "Анализ PDF...",
                "analysis_complete": "Анализ завершён",
                "analysis_failed": "Не удалось провести анализ",
                "summary": "Резюме",
                "keywords": "Ключевые слова",
                "ask_question": "Задать вопрос",
                "enter_question": "Введите ваш вопрос о PDF...",
                "ask": "Спросить",
                "answer": "Ответ",
                "no_pdf_selected": "Пожалуйста, сначала выберите PDF файл",
                "pdf_analysis": "Результаты анализа PDF",
                "analysis_title": "Анализ",
                "thinking": "Обработка",
                "please_wait": "Пожалуйста, подождите..."
            },
            "ar": {
                "app_title": "SmartPDF - تحميل وتحليل",
                "setup_title": "SmartPDF - الإعداد",
                "select_pdf": "اختر ملف PDF",
                "analyze_info": "قم بتحميل ملف PDF وتحليله.\nستظهر نتائج التحليل هنا.",
                "select_file": "اختر ملف",
                "file_path_placeholder": "مسار ملف PDF",
                "analyze": "تحليل",
                "install": "تثبيت",
                "setup_info": "تطبيق SmartPDF يبدأ للمرة الأولى.\nانقر على 'تثبيت' لبدء عملية الإعداد.",
                "installing": "جارٍ التثبيت...",
                "installation_complete": "اكتمل التثبيت!",
                "starting_app": "بدء التطبيق...",
                "about_text": "قم بتحميل ملفات PDF الخاصة بك وتحليلها.",
                "language_selection": "اللغة:",
                "select_language": "اختر اللغة",
                "settings": "الإعدادات",
                "settings_title": "الإعدادات",
                "change_language": "تغيير اللغة",
                "current_language": "اللغة الحالية:",
                "apply_changes": "تطبيق التغييرات",
                "cancel": "إلغاء",
                "language_changed": "سيتم تغيير اللغة. سيتم إعادة تشغيل التطبيق.",
                "confirm_language_change": "تأكيد تغيير اللغة",
                "analyzing": "جارٍ تحليل PDF...",
                "analysis_complete": "اكتمل التحليل",
                "analysis_failed": "فشل التحليل",
                "summary": "الملخص",
                "keywords": "الكلمات المفتاحية",
                "ask_question": "اطرح سؤالاً",
                "enter_question": "أدخل سؤالك حول ملف PDF...",
                "ask": "اسأل",
                "answer": "الإجابة",
                "no_pdf_selected": "يرجى اختيار ملف PDF أولاً",
                "pdf_analysis": "نتائج تحليل PDF",
                "analysis_title": "التحليل",
                "thinking": "يفكر...",
                "please_wait": "يرجى الانتظار..."
            },
            "zh": {
                "app_title": "SmartPDF - 加载和分析",
                "setup_title": "SmartPDF - 设置",
                "select_pdf": "选择PDF文件",
                "analyze_info": "上传PDF文件并分析。\n分析结果将在此处显示。",
                "select_file": "选择文件",
                "file_path_placeholder": "PDF文件路径",
                "analyze": "分析",
                "install": "安装",
                "setup_info": "SmartPDF应用程序首次启动。\n请点击'安装'开始配置过程。",
                "installing": "正在安装...",
                "installation_complete": "安装完成！",
                "starting_app": "启动应用程序...",
                "about_text": "上传您的PDF文件并分析它们。",
                "language_selection": "语言：",
                "select_language": "选择语言",
                "settings": "设置",
                "settings_title": "设置",
                "change_language": "更改语言",
                "current_language": "当前语言：",
                "apply_changes": "应用更改",
                "cancel": "取消",
                "language_changed": "语言将被更改。应用程序将重新启动。",
                "confirm_language_change": "确认语言更改",
                "analyzing": "正在分析PDF...",
                "analysis_complete": "分析完成",
                "analysis_failed": "分析失败",
                "summary": "摘要",
                "keywords": "关键词",
                "ask_question": "提出问题",
                "enter_question": "输入您关于PDF的问题...",
                "ask": "提问",
                "answer": "回答",
                "no_pdf_selected": "请先选择一个PDF文件",
                "pdf_analysis": "PDF分析结果",
                "analysis_title": "分析",
                "thinking": "思考中",
                "please_wait": "请稍候..."
            },
            "ja": {
                "app_title": "SmartPDF - ロードと分析",
                "setup_title": "SmartPDF - セットアップ",
                "select_pdf": "PDFファイルを選択",
                "analyze_info": "PDFファイルをアップロードして分析します。\n分析結果はここに表示されます。",
                "select_file": "ファイルを選択",
                "file_path_placeholder": "PDFファイルのパス",
                "analyze": "分析",
                "install": "インストール",
                "setup_info": "SmartPDFアプリケーションが初回起動しています。\n設定プロセスを開始するには「インストール」をクリックしてください。",
                "installing": "インストール中...",
                "installation_complete": "インストール完了！",
                "starting_app": "アプリケーション起動中...",
                "about_text": "PDFファイルをアップロードして分析してください。",
                "language_selection": "言語：",
                "select_language": "言語を選択",
                "settings": "設定",
                "settings_title": "設定",
                "change_language": "言語を変更",
                "current_language": "現在の言語：",
                "apply_changes": "変更を適用",
                "cancel": "キャンセル",
                "language_changed": "言語が変更されます。アプリケーションが再起動されます。",
                "confirm_language_change": "言語変更の確認",
                "analyzing": "PDFを分析中...",
                "analysis_complete": "分析完了",
                "analysis_failed": "分析に失敗しました",
                "summary": "要約",
                "keywords": "キーワード",
                "ask_question": "質問する",
                "enter_question": "PDFに関する質問を入力してください...",
                "ask": "質問",
                "answer": "回答",
                "no_pdf_selected": "最初にPDFファイルを選択してください",
                "pdf_analysis": "PDF分析結果",
                "analysis_title": "分析",
                "thinking": "考え中",
                "please_wait": "しばらくお待ちください..."
            }
        }
        
        self.load_translations()
    
    def load_translations(self):
        """Load translations from file if exists"""
        if os.path.exists(self.language_file):
            try:
                with open(self.language_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content: 
                        data = json.loads(content)
                        self.current_language = data.get('current_language', 'en')
                        self.translations = data.get('translations', {})
                    else:
                        self.current_language = "en"
                        self.translations = {}
            except (json.JSONDecodeError, Exception) as e:
                print(f"Error loading translations: {e}")
                self.current_language = "en"
                self.translations = {}
        else:
            self.current_language = "en"
            self.translations = {}
    
    def save_translations(self):
        """Save translations to file"""
        try:
            os.makedirs(os.path.dirname(self.language_file), exist_ok=True)
            
            data = {
                'current_language': self.current_language,
                'translations': self.translations
            }
            
            temp_file = self.language_file + '.tmp'
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            if os.path.exists(self.language_file):
                os.remove(self.language_file)
            os.rename(temp_file, self.language_file)
            
            
        except Exception as e:
            print(f"Error saving translations: {e}")
            temp_file = self.language_file + '.tmp'
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except:
                    pass
    
    def translate_texts(self, target_language, progress_callback=None):
        if target_language == "en":
            self.translations[target_language] = self.default_texts.copy()
            self.current_language = target_language
            self.save_translations()
            if progress_callback:
                progress_callback(100)
            return
        
        if target_language in self.translations:
            self.current_language = target_language
            self.save_translations()
            if progress_callback:
                progress_callback(100)
            return
        
        if target_language in self.predefined_translations:
            self.translations[target_language] = self.predefined_translations[target_language].copy()
            self.current_language = target_language
            self.save_translations()
            if progress_callback:
                progress_callback(100)
            return
        
        self.translations[target_language] = self.default_texts.copy()
        self.current_language = target_language
        self.save_translations()
        if progress_callback:
            progress_callback(100)
    
    def get_text(self, key):
        """Get translated text for current language"""
        if self.current_language in self.translations:
            return self.translations[self.current_language].get(key)
        return self.default_texts.get(key, key)
    
    def set_language(self, language_code):
        """Set current language"""
        if language_code in self.available_languages:
            self.current_language = language_code
            self.save_translations()
    
    def get_available_languages(self):
        """Get list of available languages"""
        return self.available_languages
    
    def translate_in_background(self, target_language, progress_callback=None, completion_callback=None):
        """Translate texts in background thread"""
        def translate_worker():
            self.translate_texts(target_language, progress_callback)
            if completion_callback:
                completion_callback()
        
        thread = threading.Thread(target=translate_worker, daemon=True)
        thread.start()
        return thread
