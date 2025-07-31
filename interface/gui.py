from customtkinter import *
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter.font import *
import os
import threading
import shutil

if __name__ == "__main__":
    import theme as th
    from session import Session as session
    from language_manager import LanguageManager
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.pdf_reader import PDFReader
    from utils.qa_engine import QAEngine
    from utils.summarizer import Summarizer
else:
    from interface import theme as th
    from interface.session import Session as session
    from interface.language_manager import LanguageManager
    from utils.pdf_reader import PDFReader
    from utils.qa_engine import QAEngine
    from utils.summarizer import Summarizer
        
set_appearance_mode("light")

class GUI(CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "logo.ico"))
        
        self.session = session()
        self.pdf_text = ""
        self.pdf_path = ""
        
        self.qa_engine = QAEngine()
        self.summarizer = Summarizer()
        
        if not self.session.check():
            self.language_manager = None
            self.setup_needed = True
        else:
            self.language_manager = LanguageManager(self.session.get_app_folder(), create_folder=True)
            self.setup_needed = False
        
        if self.setup_needed:
            self.title("SmartPDF - Setup")
        else:
            self.title(self.language_manager.get_text("app_title"))
            
        self.geometry("1350x750")
        self.minsize(1350, 750)
        self.config(bg=th.MAIN_BG)
        
        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        x = (1350 // 2) - (width // 2)
        y = (750 // 2) - (height // 2)
        self.geometry(f"1350x750+{x}+{y}")
        self.after(0, self._maximize_window)

        if self.setup_needed:
            self.resizable(False, False)
            self.start_session()
        else:
            self.language_manager.load_translations()
            self.update_idletasks()
            self._maximize_window()
            self.create_widgets()
            
    def _maximize_window(self):
        try:
            self.state('zoomed')
        except Exception:
            self.attributes('-zoomed', True)
        
    def create_widgets(self):
        self.title(self.language_manager.get_text("app_title"))
        self.main_content()
        
    def main_content(self):
        self.settings_button = CTkButton(
            self, 
            text="⚙", 
            command=self.open_settings,
            font=("Arial", 20, BOLD),
            width=40,
            height=40,
            corner_radius=5,
            bg_color=th.MAIN_BG,
            fg_color=th.MAIN_FG,
            text_color=th.SETTINGS_ICON,
            hover_color=th.MAIN_FRAME_FG
        )
        self.settings_button.pack(side=TOP, anchor=NW, padx=5, pady=5)
        
        self.main_frame = CTkFrame(self, corner_radius=0, fg_color=th.MAIN_FG)
        self.main_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        
        self.results_frame = CTkFrame(self.main_frame, corner_radius=0, fg_color=th.MAIN_FG)
        self.results_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.dosya_secin_label = CTkLabel(self.results_frame, text=self.language_manager.get_text("select_pdf"), font=("Arial", 60, BOLD), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.dosya_secin_label.pack(pady=(250, 10))

        self.bilgilendirme_label = CTkLabel(self.results_frame, text=self.language_manager.get_text("analyze_info"), font=("Arial", 18), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.bilgilendirme_label.pack(pady=10)

        self.bottom_frame = CTkFrame(self.main_frame, corner_radius=0, fg_color=th.MAIN_FG)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        
        self.file_way_button = CTkButton(self.bottom_frame, text=self.language_manager.get_text("select_file"), command=self.select_file, font=("Arial", 18), height=45, width=150, corner_radius=10, bg_color=th.MAIN_BG, fg_color=th.MAIN_TC, text_color=th.MAIN_FG, hover_color=th.MAIN_TC_HOVER)
        self.file_way_button.pack(pady=10, padx=(5*2, 2.5*2), side=LEFT)

        self.file_way_input = CTkEntry(self.bottom_frame, placeholder_text=self.language_manager.get_text("file_path_placeholder"), font=("Courier New", 16, BOLD), width=800, height=45, corner_radius=10, bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC, border_width=1, border_color=th.DIVIDER)
        self.file_way_input.pack(pady=10, padx=(2.5*2, 2.5*2), side=LEFT, fill=X, expand=True)
        
        self.analyze_button = CTkButton(self.bottom_frame, text=self.language_manager.get_text("analyze"), command=self.analyze_file, font=("Arial", 18), height=45, width=150, corner_radius=10, bg_color=th.MAIN_BG, fg_color=th.MAIN_TC, text_color=th.MAIN_FG, hover_color=th.MAIN_TC_HOVER)
        self.analyze_button.pack(pady=10, padx=(2.5*2, 5*2), side=RIGHT)
        
    def select_file(self):
        file_path = fd.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.file_way_input.delete(0, END)
            self.file_way_input.insert(0, file_path)
            
    def analyze_file(self):
        file_path = self.file_way_input.get().strip()
        if not file_path:
            mb.showwarning("Warning", self.language_manager.get_text("no_pdf_selected"))
            return
        
        self.pdf_path = file_path
        self.analyze_button.configure(text="...", state="disabled")
        
        for widget in self.results_frame.winfo_children():
            widget.destroy()
            
        loading_title = CTkLabel(
            self.results_frame,
            text=self.language_manager.get_text("analyzing"),
            font=("Arial", 45, BOLD),
            text_color=th.MAIN_TC
        )
        loading_title.pack(pady=(220, 0))
        
        loading_info = CTkLabel(
            self.results_frame,
            text=self.language_manager.get_text("please_wait"),
            font=("Arial", 18),
            text_color=th.MAIN_TC_HOVER
        )
        loading_info.pack(pady=10)
        
        def analyze_in_background():
            pdf_reader = PDFReader(file_path)
            success, result = pdf_reader.extract_text()
            
            if not success:
                self.after(0, lambda: self.show_error(result))
                return
            
            self.pdf_text = result
            
            lang_code = self.language_manager.current_language
            success, analysis = self.qa_engine.analyze_pdf(self.pdf_text, lang_code)
            
            if success:
                success2, summary = self.summarizer.summarize_text(self.pdf_text, lang_code, "brief")
                success3, keywords = self.summarizer.extract_keywords(self.pdf_text, lang_code)
                
                self.after(0, lambda: self.display_results(analysis, summary if success2 else "", keywords if success3 else ""))
            else:
                self.after(0, lambda: self.show_error(analysis))
        
        thread = threading.Thread(target=analyze_in_background, daemon=True)
        thread.start()
    
    def show_error(self, error_msg):
        self.analyze_button.configure(text=self.language_manager.get_text("analyze"), state="normal")
        mb.showerror(self.language_manager.get_text("analysis_failed"), error_msg)
    
    def display_results(self, analysis, summary, keywords):
        self.analyze_button.configure(text=self.language_manager.get_text("analyze"), state="normal")
        
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        title_label = CTkLabel(
            self.results_frame, 
            text=self.language_manager.get_text("pdf_analysis"), 
            font=("Arial", 28, BOLD), 
            text_color=th.MAIN_TC
        )
        title_label.pack(pady=(25, 20))
        
        scrollable_frame = CTkScrollableFrame(
            self.results_frame, 
            fg_color=th.MAIN_FG,
            corner_radius=15
        )
        scrollable_frame.pack(fill=BOTH, expand=True, padx=25, pady=15)
        
        if analysis:
            analysis_section = CTkFrame(scrollable_frame, fg_color=th.MAIN_FRAME_FG, corner_radius=12)
            analysis_section.pack(fill=X, padx=15, pady=(15, 10))
            
            analysis_header = CTkLabel(
                analysis_section, 
                text=self.language_manager.get_text("analysis_title"), 
                font=("Arial", 20, BOLD), 
                text_color=th.MAIN_TC,
                anchor="w"
            )
            analysis_header.pack(fill=X, padx=20, pady=(20, 10))
            
            analysis_lines = analysis.count('\n') + 1
            analysis_height = max(100, min(200, analysis_lines * 60))
            
            analysis_text = CTkTextbox(
                analysis_section, 
                height=analysis_height, 
                font=("Arial", 16),
                fg_color="white",
                text_color="#2c3e50",
                corner_radius=8,
                border_width=1,
                border_color=th.DIVIDER,
                wrap="word"
            )
            analysis_text.pack(fill=X, padx=20, pady=(0, 20))
            analysis_text.insert("1.0", analysis)
            analysis_text.configure(state="disabled")
        
        if summary:
            summary_section = CTkFrame(scrollable_frame, fg_color=th.MAIN_FRAME_FG, corner_radius=12)
            summary_section.pack(fill=X, padx=15, pady=10)
            
            summary_header = CTkLabel(
                summary_section, 
                text=self.language_manager.get_text("summary"), 
                font=("Arial", 20, BOLD), 
                text_color=th.MAIN_TC,
                anchor="w"
            )
            summary_header.pack(fill=X, padx=20, pady=(20, 10))
            
            summary_lines = summary.count('\n') + 1
            summary_height = max(80, min(150, summary_lines * 25))
            
            summary_text = CTkTextbox(
                summary_section, 
                height=summary_height, 
                font=("Arial", 16),
                fg_color="white",
                text_color="#2c3e50",
                corner_radius=8,
                border_width=1,
                border_color=th.DIVIDER,
                wrap="word"
            )
            summary_text.pack(fill=X, padx=20, pady=(0, 20))
            summary_text.insert("1.0", summary)
            summary_text.configure(state="disabled")
        
        if keywords:
            keywords_section = CTkFrame(scrollable_frame, fg_color=th.MAIN_FRAME_FG, corner_radius=12)
            keywords_section.pack(fill=X, padx=15, pady=10)
            
            keywords_header = CTkLabel(
                keywords_section, 
                text=self.language_manager.get_text("keywords"), 
                font=("Arial", 20, BOLD), 
                text_color=th.MAIN_TC,
                anchor="w"
            )
            keywords_header.pack(fill=X, padx=20, pady=(20, 10))
            
            keywords_container = CTkFrame(keywords_section, fg_color="white", corner_radius=8)
            keywords_container.pack(fill=X, padx=20, pady=(0, 20))
            
            keywords_label = CTkLabel(
                keywords_container, 
                text=keywords, 
                font=("Arial", 14), 
                text_color="#34495e", 
                wraplength=1200, 
                justify=LEFT,
                anchor="w"
            )
            keywords_label.pack(fill=X, padx=15, pady=15)
        
        qa_section = CTkFrame(scrollable_frame, fg_color=th.MAIN_FRAME_FG, corner_radius=12)
        qa_section.pack(fill=X, padx=15, pady=(10, 20))
        
        qa_header = CTkLabel(
            qa_section, 
            text=self.language_manager.get_text("ask_question"), 
            font=("Arial", 20, BOLD), 
            text_color=th.MAIN_TC,
            anchor="w"
        )
        qa_header.pack(fill=X, padx=20, pady=(20, 15))
        
        question_container = CTkFrame(qa_section, fg_color="transparent")
        question_container.pack(fill=X, padx=20, pady=(0, 15))
        
        self.question_entry = CTkEntry(
            question_container, 
            placeholder_text=self.language_manager.get_text("enter_question"), 
            font=("Arial", 14), 
            height=45,
            corner_radius=8,
            fg_color="white",
            text_color="#2c3e50",
            placeholder_text_color="#7f8c8d",
            border_width=1,
            border_color=th.DIVIDER
        )
        self.question_entry.pack(fill=X, expand=True, side=LEFT, padx=(0, 15))
        
        ask_button = CTkButton(
            question_container, 
            text=self.language_manager.get_text("ask"), 
            command=self.ask_question, 
            font=("Arial", 14, BOLD), 
            height=45, 
            width=120,
            corner_radius=8,
            fg_color=th.MAIN_TC,
            text_color="white",
            hover_color=th.MAIN_TC_HOVER
        )
        ask_button.pack(side=RIGHT)
        
        self.answer_frame = CTkFrame(qa_section, fg_color="transparent")
        self.answer_frame.pack(fill=X, padx=20, pady=(0, 20))
    
    def ask_question(self):
        question = self.question_entry.get().strip()
        if not question or not self.pdf_text:
            return
        
        self.question_entry.configure(state="disabled")
        
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
            
        loading_label = CTkLabel(
            self.answer_frame,
            text=self.language_manager.get_text("thinking") + "...",
            font=("Arial", 16),
            text_color=th.MAIN_TC_HOVER
        )
        loading_label.pack(pady=20)
        
        def get_answer():
            lang_code = self.language_manager.current_language
            success, answer = self.qa_engine.answer_question(self.pdf_text, question, lang_code)
            
            self.after(0, lambda: self.show_answer(answer if success else "Error getting answer"))
        
        thread = threading.Thread(target=get_answer, daemon=True)
        thread.start()
    
    def show_answer(self, answer):
        self.question_entry.configure(state="normal")
        
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
        
        answer_header = CTkLabel(
            self.answer_frame, 
            text=self.language_manager.get_text("answer"), 
            font=("Arial", 16, BOLD), 
            text_color=th.MAIN_TC,
            anchor="w"
        )
        answer_header.pack(fill=X, pady=(15, 10))
        
        answer_lines = answer.count('\n') + 1
        answer_height = max(60, min(120, answer_lines * 25))
        
        answer_container = CTkFrame(self.answer_frame, fg_color="white", corner_radius=8)
        answer_container.pack(fill=X, pady=(0, 5))
        
        answer_text = CTkTextbox(
            answer_container, 
            height=answer_height, 
            font=("Arial", 16),
            fg_color="white",
            text_color="#2c3e50",
            corner_radius=8,
            border_width=0,
            wrap="word"
        )
        answer_text.pack(fill=X, padx=15, pady=15)
        answer_text.insert("1.0", answer)
        answer_text.configure(state="disabled")
    
    def open_settings(self):
        """Open settings window"""
        self.settings_window = CTkToplevel(self)
        self.settings_window.title(self.language_manager.get_text("settings_title"))
        self.settings_window.geometry("400x400")
        self.settings_window.config(bg=th.MAIN_BG)
        self.settings_window.resizable(False, False)
        
        self.settings_window.transient(self)
        self.settings_window.grab_set()
        
        x = self.winfo_x() + (self.winfo_width() // 2) - 200
        y = self.winfo_y() + (self.winfo_height() // 2) - 150
        self.settings_window.geometry(f"400x400+{x}+{y}")
        
        self.create_settings_content()
    
    def create_settings_content(self):
        """Create settings window content"""
        title_label = CTkLabel(
            self.settings_window,
            text=self.language_manager.get_text("settings_title"),
            font=("Arial", 24, BOLD),
            text_color=th.MAIN_TC,
            fg_color=th.MAIN_BG
        )
        title_label.pack(pady=(20, 30))

        current_lang_frame = CTkFrame(self.settings_window, fg_color=th.MAIN_BG, bg_color=th.MAIN_BG)
        current_lang_frame.pack(pady=10, padx=20, fill=X)
        
        current_lang_label = CTkLabel(
            current_lang_frame,
            text=self.language_manager.get_text("current_language"),
            font=("Arial", 16, BOLD),
            text_color=th.MAIN_TC,
            fg_color=th.MAIN_BG
        )
        current_lang_label.pack(anchor=W)
        
        current_lang_value = CTkLabel(
            current_lang_frame,
            text=self.language_manager.get_available_languages()[self.language_manager.current_language],
            font=("Arial", 14),
            text_color=th.MAIN_TC_HOVER,
            fg_color=th.MAIN_BG
        )
        current_lang_value.pack(anchor=W, pady=(5, 0))
        
        lang_frame = CTkFrame(self.settings_window, fg_color=th.MAIN_BG, bg_color=th.MAIN_BG)
        lang_frame.pack(pady=(20, 10), padx=20, fill=X)
        
        lang_label = CTkLabel(
            lang_frame,
            text=self.language_manager.get_text("change_language"),
            font=("Arial", 16, BOLD),
            text_color=th.MAIN_TC,
            fg_color=th.MAIN_BG,
            bg_color=th.MAIN_BG
        )
        lang_label.pack(anchor=W)
        
        languages = list(self.language_manager.get_available_languages().values())
        self.settings_language_var = StringVar(value=self.language_manager.get_available_languages()[self.language_manager.current_language])
        
        self.settings_language_dropdown = CTkComboBox(
            lang_frame,
            values=languages,
            variable=self.settings_language_var,
            font=("Arial", 14),
            width=350,
            height=35,
            corner_radius=8,
            fg_color="white",
            text_color=th.MAIN_TC,
            border_width=0,
            border_color=th.DIVIDER,
            dropdown_fg_color=th.MAIN_FG,
            button_color="white",
            button_hover_color="white",
            bg_color=th.MAIN_BG
        )
        self.settings_language_dropdown.pack(pady=(10, 0), fill=X)
        self.settings_language_dropdown._entry.configure(state="readonly", cursor="arrow")
        self.settings_language_dropdown._entry.bind("<Button-1>", lambda e: (self.settings_language_dropdown._open_dropdown_menu(), self.settings_language_dropdown._entry.after(10, self.settings_language_dropdown._entry.configure(state="normal"))))
        self.settings_language_dropdown._canvas.tag_bind("dropdown_arrow", "<Button-1>", lambda e: (self.settings_language_dropdown._open_dropdown_menu(), self.settings_language_dropdown._entry.after(10, self.settings_language_dropdown._entry.configure(state="normal"))))
        self.settings_language_dropdown.bind(
            "<<ComboboxSelected>>",
            lambda e: self.settings_language_dropdown._entry.configure(state="readonly")
        )
        
        button_frame = CTkFrame(self.settings_window, fg_color=th.MAIN_BG, bg_color=th.MAIN_BG)
        button_frame.pack(side=BOTTOM, pady=20, padx=20, fill=X)
        
        cancel_button = CTkButton(
            button_frame,
            text=self.language_manager.get_text("cancel"),
            command=self.close_settings,
            font=("Arial", 16),
            height=40,
            width=170,
            corner_radius=8,
            fg_color=th.MAIN_FRAME_FG,
            text_color=th.MAIN_TC,
            hover_color=th.DIVIDER,
            bg_color=th.MAIN_BG
        )
        cancel_button.pack(side=LEFT)
        
        apply_button = CTkButton(
            button_frame,
            text=self.language_manager.get_text("apply_changes"),
            command=self.apply_language_change,
            font=("Arial", 16),
            height=40,
            width=170,
            corner_radius=8,
            fg_color=th.MAIN_TC,
            text_color=th.MAIN_FG,
            hover_color=th.MAIN_TC_HOVER,
            bg_color=th.MAIN_BG
        )
        apply_button.pack(side=RIGHT)
    
    def close_settings(self):
        """Close settings window"""
        self.settings_window.destroy()
    
    def apply_language_change(self):
        """Apply language change and restart setup"""
        selected_language_name = self.settings_language_var.get()
        selected_language_code = None
        
        for code, name in self.language_manager.get_available_languages().items():
            if name == selected_language_name:
                selected_language_code = code
                break
        
        if not selected_language_code or selected_language_code == self.language_manager.current_language:
            self.close_settings()
            return
        
        confirm = mb.askyesno(
            self.language_manager.get_text("confirm_language_change"),
            self.language_manager.get_text("language_changed")
        )
        
        if confirm:
            self.settings_window.destroy()
            
            for widget in self.winfo_children():
                widget.destroy()
            
            try:
                if os.path.exists(self.session.get_app_folder()):
                    shutil.rmtree(self.session.get_app_folder())
            except Exception as e:
                print(f"Error removing app folder: {e}")
            
            temp_folder = os.path.join(os.path.expanduser("~"), ".smartpdf_temp")
            self.language_manager = LanguageManager(temp_folder, create_folder=False)
            
            self.geometry("1350x750")
            self.state('normal')
            self.resizable(False, False)
            self.config(bg=th.MAIN_BG)
            self.start_installation_directly(selected_language_code)
        else:
            self.close_settings()
    
    def start_installation_directly(self, selected_language_code):
        """Start installation directly without showing language selection"""
        self.title(self.language_manager.get_text("setup_title"))
        
        self.header = CTkLabel(self, text="SmartPDF", font=("Arial", 125, BOLD), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.header.pack(pady=(200, 20))

        selected_language_name = "English"

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
        
        selected_language_name = self.available_languages.get(selected_language_code, "English")

        self.hakkinda = CTkLabel(
            self,
            text=f"Installing SmartPDF for {selected_language_name}...",
            font=("Arial", 20),
            bg_color=th.MAIN_BG,
            fg_color=th.MAIN_FG,
            text_color=th.MAIN_TC
        )
        self.hakkinda.pack(pady=10)

        self.progress_bar = CTkProgressBar(self, width=400, height=10, corner_radius=10, progress_color=th.MAIN_TC, fg_color=th.PROGRESS_BAR_FG)
        self.progress_bar.pack(pady=(10, 25), side=BOTTOM)
        self.progress_bar.set(0)

        self.progress_label = CTkLabel(self, text="Installing...", font=("Arial", 20), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.progress_label.pack(pady=10, side=BOTTOM)
        
        def on_installation_complete():
            self.session.create_session()
            
            self.language_manager = LanguageManager(self.session.get_app_folder(), create_folder=True)
            
            self.language_manager.set_language(selected_language_code)
            if selected_language_code in self.language_manager.predefined_translations:
                self.language_manager.translations[selected_language_code] = self.language_manager.predefined_translations[selected_language_code].copy()
            else:
                self.language_manager.translations[selected_language_code] = self.language_manager.default_texts.copy()
            self.language_manager.save_translations()
            
            self.after(500, lambda: self.progress_label.configure(text=self.language_manager.get_text("installation_complete")))
            self.after(1500, lambda: self.progress_label.configure(text=self.language_manager.get_text("starting_app")))
            self.after(2000, self.start_app)
        
        def update_progress(progress):
            self.after(0, lambda: self.progress_bar.set(progress / 100))
        
        def simulate_installation():
            for i in range(101):
                self.after(i * 20, lambda p=i: update_progress(p))
            self.after(2100, on_installation_complete)
        
        simulate_installation()
    
    def start_session(self):
        if self.language_manager is None:
            temp_folder = os.path.join(os.path.expanduser("~"), ".smartpdf_temp")
            self.language_manager = LanguageManager(temp_folder, create_folder=False)
        
        self.title(self.language_manager.get_text("setup_title"))
        self.header = CTkLabel(self, text="SmartPDF", font=("Arial", 125, BOLD), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.header.pack(pady=(150, 20))
        
        
        self.download_button = CTkButton(self, text=self.language_manager.get_text("install"), command=self.start_download, font=("Arial", 25), height=50, width=150, corner_radius=12.5, bg_color=th.MAIN_BG, fg_color=th.MAIN_TC, text_color=th.MAIN_FG, hover_color=th.MAIN_TC_HOVER)
        self.download_button.pack(pady=20)
        
        self.aciklama = CTkLabel(self, text=self.language_manager.get_text("setup_info"), font=("Arial", 20), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.aciklama.pack(pady=(10, 40), side=BOTTOM)
        
        self.language_frame = CTkFrame(self, fg_color=th.MAIN_FG, corner_radius=10, bg_color=th.MAIN_BG)
        self.language_frame.pack(pady=(0, 0), side=BOTTOM)
        
        self.language_label = CTkLabel(self.language_frame, text=self.language_manager.get_text("language_selection"), font=("Arial", 18, BOLD), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.language_label.pack(pady=(0, 0), padx=10, side=LEFT)
        
        languages = list(self.language_manager.get_available_languages().values())
        
        default_language = "English"
        if hasattr(self, 'selected_language_for_setup'):
            default_language = self.language_manager.get_available_languages().get(self.selected_language_for_setup, "English")
        
        self.language_var = StringVar(value=default_language)
        self.language_dropdown = CTkComboBox(
            self.language_frame,
            values=languages,
            variable=self.language_var,
            font=("Arial", 16),
            width=200,
            height=35,
            corner_radius=8,
            bg_color=th.MAIN_BG,
            fg_color="white",
            text_color=th.MAIN_TC,
            border_width=0,
            dropdown_fg_color=th.MAIN_FG,
            button_color="white",  
            button_hover_color="white",  
        )
        self.language_dropdown.pack(pady=(15, 15), padx=0, side=RIGHT)
        
    def start_download(self):
        selected_language_name = self.language_var.get()
        selected_language_code = None
        for code, name in self.language_manager.get_available_languages().items():
            if name == selected_language_name:
                selected_language_code = code
                break
        
        if not selected_language_code:
            selected_language_code = "en"
        
        self.download_button.pack_forget()
        self.aciklama.pack_forget()
        self.language_frame.pack_forget()
        
        self.title("SmartPDF - Setup")

        self.hakkinda = CTkLabel(
            self,
            text=f"Installing SmartPDF for {selected_language_name}...",
            font=("Arial", 20),
            bg_color=th.MAIN_BG,
            fg_color=th.MAIN_FG,
            text_color=th.MAIN_TC
        )
        self.hakkinda.pack(pady=10)

        self.progress_bar = CTkProgressBar(self, width=400, height=10, corner_radius=10, progress_color=th.MAIN_TC, fg_color=th.PROGRESS_BAR_FG)
        self.progress_bar.pack(pady=(10, 25), side=BOTTOM)
        self.progress_bar.set(0)

        self.progress_label = CTkLabel(self, text="Installing...", font=("Arial", 20), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.progress_label.pack(pady=10, side=BOTTOM)
        
        def on_installation_complete():
            self.session.create_session()
            
            self.language_manager = LanguageManager(self.session.get_app_folder(), create_folder=True)
            
            self.language_manager.set_language(selected_language_code)
            if selected_language_code in self.language_manager.predefined_translations:
                self.language_manager.translations[selected_language_code] = self.language_manager.predefined_translations[selected_language_code].copy()
            else:
                self.language_manager.translations[selected_language_code] = self.language_manager.default_texts.copy()
            self.language_manager.save_translations()
            
            self.after(500, lambda: self.progress_label.configure(text=self.language_manager.get_text("installation_complete")))
            self.after(1500, lambda: self.progress_label.configure(text=self.language_manager.get_text("starting_app")))
            self.after(2000, self.start_app)
        
        def update_progress(progress):
            self.after(0, lambda: self.progress_bar.set(progress / 100))
        
        def simulate_installation():
            for i in range(101):
                self.after(i * 20, lambda p=i: update_progress(p))
            self.after(2100, on_installation_complete)
        
        simulate_installation()
        
    def start_app(self):
        self.header.pack_forget()
        self.progress_bar.pack_forget()
        self.progress_label.pack_forget()
        self.hakkinda.pack_forget()
        self.resizable(True, True)
        
        self.language_manager.load_translations()
        
        self.qa_engine = QAEngine()
        self.summarizer = Summarizer()
        
        self.create_widgets()

def start():
    gui = GUI()
    gui.mainloop()
    
if __name__ == "__main__":
    start()
