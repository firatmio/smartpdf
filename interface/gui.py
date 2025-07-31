from customtkinter import *
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter.font import *
import theme as th
import os
from session import Session as session

set_appearance_mode("light")

class GUI(CTk):
    def __init__(self):
        super().__init__()
        self.title("SmartPDF - Yükle ve Analiz Et")
        self.geometry("1350x750")
        self.config(bg=th.MAIN_BG)

        if not session().check():
            self.resizable(False, False)
            self.start_session()

        else:
            self.create_widgets()
        
    def create_widgets(self):
        self.title("SmartPDF - Yükle ve Analiz Et")
        self.sidebar()
        self.main_content()
        
    def main_content(self):
        self.main_frame = CTkFrame(self, corner_radius=0, fg_color=th.MAIN_FRAME_FG)
        self.main_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.title_label = CTkLabel(self.main_frame, text="SmartPDF", font=("Arial", 30, BOLD), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.title_label.pack(pady=(20, 10))
        
    def sidebar(self):
        self.sidebar_frame = CTkFrame(self, width=250, corner_radius=0, bg_color=th.MAIN_BG, fg_color=th.MAIN_FG)
        self.sidebar_frame.pack(side=LEFT, fill=Y)
        
        self.title_label = CTkLabel(self.sidebar_frame, width=200, anchor="w", text="SmartPDF", font=("Arial", 30, BOLD), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.title_label.pack(pady=(20, 10), padx=25)

        self.divider = CTkFrame(self.sidebar_frame, height=2, corner_radius=10, bg_color=th.MAIN_BG, fg_color=th.DIVIDER)
        self.divider.pack(fill=X, padx=25, pady=(15, 15))
        
        self.analyze_button = CTkButton(
            self.sidebar_frame,
            text="Analiz Et",
            font=("Arial", 18, BOLD),
            height=45,
            width=200,
            corner_radius=8,
            bg_color=th.MAIN_BG,
            fg_color=th.MAIN_FRAME_FG,
            hover_color=th.MAIN_BG,
            text_color=th.MAIN_TC_HOVER,
            anchor="w"
        )
        self.analyze_button.pack(pady=(10, 5), padx=25)

        self.speak_button = CTkButton(
            self.sidebar_frame,
            text="Seslendir",
            font=("Arial", 18, BOLD),
            height=45,
            width=200,
            corner_radius=8,
            bg_color=th.MAIN_BG,
            fg_color=th.MAIN_FRAME_FG,
            hover_color=th.MAIN_BG,
            text_color=th.MAIN_TC_HOVER,
            anchor="w"
        )
        self.speak_button.pack(pady=5, padx=25)

        self.settings_button = CTkButton(
            self.sidebar_frame,
            text="Ayarlar",
            font=("Arial", 18, BOLD),
            height=45,
            width=200,
            corner_radius=8,
            bg_color=th.MAIN_BG,
            fg_color=th.MAIN_FRAME_FG,
            hover_color=th.MAIN_BG,
            text_color=th.MAIN_TC_HOVER,
            anchor="w"
        )
        self.settings_button.pack(pady=5, padx=25)
    
    def start_session(self):
        self.header = CTkLabel(self, text="SmartPDF", font=("Arial", 125, BOLD), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.header.pack(pady=(200, 20))
        
        self.download_button = CTkButton(self, text="Kur", command=self.start_download, font=("Arial", 25), height=50, width=150, corner_radius=10, bg_color=th.MAIN_BG, fg_color=th.MAIN_TC, text_color=th.MAIN_FG, hover_color=th.MAIN_TC_HOVER)
        self.download_button.pack(pady=20)
        
        self.aciklama = CTkLabel(self, text="SmartPDF uygulaması ilk kez başlatılıyor.\nLütfen yükleme işlemini başlatmak için 'Kur' butonuna tıklayın.", font=("Arial", 20), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.aciklama.pack(pady=40, side=BOTTOM)
        
    def start_download(self):
        self.download_button.pack_forget()
        self.aciklama.pack_forget()
        
        self.title("SmartPDF - Kurulum")

        self.hakkinda = CTkLabel(
            self,
            text="PDF dosyalarınızı yükleyin ve analiz edin.",
            font=("Arial", 20),
            bg_color=th.MAIN_BG,
            fg_color=th.MAIN_FG,
            text_color=th.MAIN_TC
        )
        self.hakkinda.pack(pady=10)

        self.progress_bar = CTkProgressBar(self, width=400, height=10, corner_radius=10, progress_color=th.MAIN_TC, fg_color=th.PROGRESS_BAR_FG)
        self.progress_bar.pack(pady=(10, 25), side=BOTTOM)
        self.progress_bar.set(0)

        self.progress_label = CTkLabel(self, text="Kuruluyor...", font=("Arial", 20), bg_color=th.MAIN_BG, fg_color=th.MAIN_FG, text_color=th.MAIN_TC)
        self.progress_label.pack(pady=10, side=BOTTOM)
        
        self.progress = 0
        self.max_progress = 100
        self.duration = 1875 // 2 # 15 seconds in ms / 2
        self.step_time = self.duration // self.max_progress

        def update_progress():
            if self.progress < self.max_progress:
                self.progress += 0.25
                self.progress_bar.set(self.progress / self.max_progress)
                self.after(self.step_time, update_progress)
            else:
                self.progress_bar.after(15, self.progress_label.configure(text="Kurulum tamamlandı!"))
                self.progress_bar.after(1000, self.progress_label.configure(text="Uygulama başlatılıyor..."))
                self.progress_bar.after(1500, self.start_app)
                s = session()
                s.create_session()

        update_progress()
        
    def start_app(self):
        self.header.pack_forget()
        self.progress_bar.pack_forget()
        self.progress_label.pack_forget()
        self.hakkinda.pack_forget()
        self.resizable(True, True)
        self.state('zoomed')
        
        self.create_widgets()

def start():
    gui = GUI()
    gui.mainloop()
    
if __name__ == "__main__":
    start()