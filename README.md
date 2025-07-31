# 📄 SmartPDF - AI-Powered PDF Analysis Tool

<div align="center">

<img src="https://raw.githubusercontent.com/e500ky/smartpdf/main/assets/logo.png" alt="SmartPDF Logo" width="200" height="200" style="border-radius: 20px; margin-bottom: 20px;">

![SmartPDF Badge](https://img.shields.io/badge/SmartPDF-AI%20Analysis-blue?style=for-the-badge&logo=adobe-acrobat-reader)

[![Python](https://img.shields.io/badge/Python-3.12+-3776ab?style=flat&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?style=flat&logo=openai&logoColor=white)](https://openai.com)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Modern%20GUI-orange?style=flat)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

**🚀 Yapay zeka destekli PDF analiz ve soru-cevap sistemi**

[🇹🇷 Türkçe](#tr) | [🇺🇸 English](#en) | [🎯 Features](#features) | [📥 Installation](#installation)

</div>

---

## <a id="tr"></a>🇹🇷 SmartPDF Nedir?

SmartPDF, **OpenAI GPT-3.5** teknolojisi ile güçlendirilmiş, modern ve kullanıcı dostu bir PDF analiz uygulamasıdır. PDF dosyalarınızı yükleyerek kapsamlı analizler yapabilir, özetler çıkarabilir ve interaktif soru-cevap oturumları gerçekleştirebilirsiniz.

### ✨ Temel Özellikler

| 🌍 **Çok Dilli Destek** | 🤖 **AI Analizi** | 💬 **Soru-Cevap** | 🎨 **Modern UI** |
|:------------------------:|:------------------:|:------------------:|:-----------------:|
| 11 dil desteği | GPT-3.5 ile analiz | İnteraktif sorular | CustomTkinter GUI |

### 🎯 Ana Özellikler

- **📊 Kapsamlı PDF Analizi**: AI ile otomatik metin analizi
- **📝 Akıllı Özetleme**: Kısa ve detaylı özet seçenekleri  
- **🔑 Anahtar Kelime Çıkarma**: Önemli terimleri otomatik tespit
- **❓ Soru-Cevap Sistemi**: PDF içeriği hakkında anlık sorular
- **🌐 11 Dil Desteği**: Türkçe, İngilizce, Almanca, Fransızca ve daha fazlası
- **⚙️ Runtime Dil Değişimi**: Uygulama çalışırken dil değiştirme
- **🎨 Modern Arayüz**: Responsive ve kullanıcı dostu tasarım
- **💾 Kalıcı Ayarlar**: Dil tercihleri otomatik kaydedilir

---

## <a id="en"></a>🇺🇸 What is SmartPDF?

SmartPDF is a modern, user-friendly PDF analysis application powered by **OpenAI GPT-3.5** technology. Upload your PDF files to perform comprehensive analysis, generate summaries, and conduct interactive Q&A sessions.

### ✨ Key Features

| 🌍 **Multi-Language** | 🤖 **AI Analysis** | 💬 **Q&A System** | 🎨 **Modern UI** |
|:----------------------:|:------------------:|:------------------:|:-----------------:|
| 11 languages supported | GPT-3.5 powered | Interactive queries | CustomTkinter GUI |

### 🎯 Main Features

- **📊 Comprehensive PDF Analysis**: Automatic text analysis with AI
- **📝 Smart Summarization**: Brief and detailed summary options
- **🔑 Keyword Extraction**: Automatic detection of important terms
- **❓ Q&A System**: Instant questions about PDF content
- **🌐 11 Language Support**: Turkish, English, German, French and more
- **⚙️ Runtime Language Change**: Change language while app is running
- **🎨 Modern Interface**: Responsive and user-friendly design
- **💾 Persistent Settings**: Language preferences automatically saved

---

## <a id="features"></a>🎯 Detaylı Özellikler / Detailed Features

### 🌍 Desteklenen Diller / Supported Languages

```
🇺🇸 English    🇹🇷 Türkçe     🇩🇪 Deutsch    🇫🇷 Français
🇪🇸 Español    🇮🇹 Italiano   🇵🇹 Português  🇷🇺 Русский
🇸🇦 العربية     🇨🇳 中文        🇯🇵 日本語
```

### 🤖 AI Özellikleri / AI Capabilities

- **Analiz**: PDF içeriğinin ana konuları ve önemli noktaları
- **Özet**: Kısa (150 kelime) ve detaylı (400 kelime) özetler
- **Anahtar Kelimeler**: 5-8 önemli terim ve ifade
- **Soru-Cevap**: PDF içeriği hakkında anlık sorular ve cevaplar

### 🎨 Kullanıcı Arayüzü / User Interface

- **Modern Tasarım**: CustomTkinter ile modern, flat design
- **Responsive**: Tüm ekran boyutlarında uyumlu
- **Dark/Light Theme**: Otomatik tema desteği
- **Loading Indicators**: Analiz ve soru işleme sırasında görsel geri bildirim

---

## <a id="installation"></a>📥 Kurulum / Installation

### 🔧 Gereksinimler / Requirements

```bash
Python 3.12+
OpenAI API Key
```

### 1. Projeyi İndirin / Clone the Project

```bash
git clone https://github.com/yourusername/smartpdf.git
cd smartpdf
```

### 2. Sanal Ortam Oluşturun / Create Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin / Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Ortam Değişkenlerini Ayarlayın / Set Environment Variables

`.env` dosyası oluşturun / Create `.env` file:

```env
OPEN_AI_KEY=your_openai_api_key_here
```

### 5. Uygulamayı Çalıştırın / Run the Application

```bash
python main.py
```

veya / or

```bash
python interface/gui.py
```

---

## 🚀 Kullanım / Usage

### 1. **İlk Kurulum / First Setup**
- Uygulama ilk açılışta kurulum ekranını gösterir
- Dil seçimi yapın ve "Kur" butonuna tıklayın
- Kurulum otomatik olarak tamamlanır

### 2. **PDF Analizi / PDF Analysis**
- "Dosya Seç" butonuna tıklayarak PDF dosyanızı seçin
- "Analiz Et" butonuna tıklayın
- AI analizi başlar ve sonuçlar görüntülenir

### 3. **Soru Sorma / Ask Questions**
- Analiz sonuçlarının altındaki soru kutusunu kullanın
- PDF içeriği hakkında istediğiniz soruyu yazın
- "Sor" butonuna tıklayın ve AI'dan anında cevap alın

### 4. **Dil Değiştirme / Change Language**
- Sol üst köşedeki ⚙️ ayarlar butonuna tıklayın
- Yeni dili seçin ve "Değişiklikleri Uygula" butonuna tıklayın
- Uygulama yeni dilde yeniden başlar

---

## 📁 Proje Yapısı / Project Structure

```
smartpdf/
├── 📄 main.py                 # Ana uygulama dosyası
├── 📄 requirements.txt        # Python bağımlılıkları
├── 📄 .env                    # Ortam değişkenleri (OpenAI API key)
├── 📁 interface/             # GUI bileşenleri
│   ├── 📄 gui.py             # Ana GUI sınıfı
│   ├── 📄 theme.py           # Tema ve renk ayarları
│   ├── 📄 session.py         # Oturum yönetimi
│   └── 📄 language_manager.py # Çok dilli destek
└── 📁 utils/                 # Yardımcı modüller
    ├── 📄 pdf_reader.py      # PDF okuma işlemleri
    ├── 📄 qa_engine.py       # Soru-cevap motoru
    └── 📄 summarizer.py      # Özetleme ve anahtar kelime çıkarma
```

---

## ⚙️ Konfigürasyon / Configuration

### OpenAI API Ayarları / OpenAI API Settings

```python
# utils/qa_engine.py & utils/summarizer.py
model = "gpt-3.5-turbo"
max_tokens = {
    "analysis": 600,
    "summary_brief": 300,
    "summary_detailed": 600,
    "questions": 300,
    "keywords": 150
}
```

### Dil Ayarları / Language Settings

Dil dosyası: `~/.smartpdf/language.json`
```json
{
  "current_language": "tr",
  "tr": {
    "app_title": "SmartPDF - Yükle ve Analiz Et",
    "analyze": "Analiz Et",
    ...
  }
}
```

---

## 🤝 Katkıda Bulunma / Contributing

1. **Fork** edin
2. **Feature branch** oluşturun (`git checkout -b feature/amazing-feature`)
3. **Commit** yapın (`git commit -m 'Add amazing feature'`)
4. **Branch**'i **push** edin (`git push origin feature/amazing-feature`)
5. **Pull Request** açın

---

## 📝 Lisans / License

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 🔗 Bağlantılar / Links

- **OpenAI API**: [https://openai.com/api/](https://openai.com/api/)
- **CustomTkinter**: [https://github.com/TomSchimansky/CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **PyPDF2**: [https://github.com/py-pdf/pypdf](https://github.com/py-pdf/pypdf)

---

## 📧 İletişim / Contact

Proje ile ilgili sorularınız için:

- **Email**: firattunaarslan@gmail.com

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! / Don't forget to star the project if you like it!**

Made with ❤️ by [firatmio](https://github.com/firatmio)

</div>
