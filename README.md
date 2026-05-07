# 🚀 Lara-Bot: Profesyonel Epic Games Telegram Bildirim Sistemi

> **"Sadece bir kod değil, güvenli ve ölçeklenebilir bir ürün."**
Lara-Bot, Epic Games platformundaki ücretsiz oyunları takip eden, kullanıcıları anlık bilgilendiren ve kişiselleştirilmiş bir bildirim deneyimi sunan gelişmiş bir Telegram botudur. 

Bu proje, **İdeal Repo Anatomisi (Clean Architecture)** ve **Üst Düzey Güvenlik Standartlarına** uygun olarak sıfırdan revize edilmiştir.

---

## 📌 Vizyon ve Problem Tanımı
Epic Games her hafta ücretsiz oyunlar sunmasına rağmen, kullanıcılar genellikle bu oyunları takip etmeyi unutur veya ilgi alanlarına girmeyen oyun bildirimleri arasında boğulurlar. Lara-Bot, bu süreci tamamen otomatikleştirerek kullanıcıları doğru zamanda doğru oyunla buluşturmayı hedefler.

## 🎯 Projenin Amacı (Ürün Sahipliği)
Lara-Bot'un amacı sadece bir script olarak çalışmak değil, uçtan uca bir hizmet sunmaktır:
- **İlgi Alanı Filtreleme:** Kullanıcıların sadece sevdikleri türlerde (Aksiyon, RPG, Strateji) bildirim almasını sağlamak.
- **Global Çözüm:** Çoklu dil (TR, EN, ES, DE, RU) desteği ile evrensel bir ürün ortaya koymak.
- **Admin Kontrolü:** Yöneticilere kullanıcı ve kullanım istatistiklerini sağlayan profesyonel bir panel sunmak.

---

## 🛡️ Güvenlik ve Mimari Standartlar (Öne Çıkanlar)

Hocamızın belirttiği profesyonel standartlara tam uyum sağlanmıştır:
- **Çevre Değişkenleri (Environment Variables):** API Anahtarları, Token'lar ve hassas veriler asla koda gömülmez. Tüm gizli bilgiler `python-dotenv` kütüphanesi ve `os.environ.get()` yöntemi ile `.env` dosyasından güvenle çekilir.
- **Klasör İzolasyonu (İdeal Repo Anatomisi):** Kaynak kod (`src/`), veritabanı dosyaları (`data/`) ve dokümantasyon (`docs/`) net bir şekilde birbirinden ayrılmıştır.
- **Git Güvenliği (`.gitignore`):** Log dosyaları, çevresel değişkenler (`.env`), önbellekler (`__pycache__`) ve lokal veritabanı kayıtları izole edilmiş, böylece repository'nin temiz ve güvenli kalması garantilenmiştir.

---

## 🚀 Temel Özellikler
- **Asenkron ve Hızlı:** `httpx` ve `asyncio` altyapısıyla API çağrıları bloklama yapmadan gerçekleşir.
- **Otomatik Takip:** `apscheduler` yerine entegre JobQueue (Telegram'ın kendi altyapısı) ile periyodik kontroller yapılır.
- **Yerelleştirme:** Kullanıcı bazlı dinamik metin çevirisi (Google Translator API entegrasyonu).
- **Yönetici Paneli & Duyuru:** Sistem metriklerinin takibi ve anlık kitle iletişim imkanı.

---

## 🛠 Kullanılan Teknolojiler
- **Ana Dil:** Python 3.10+
- **Telegram Altyapısı:** `python-telegram-bot` (v20+)
- **HTTP ve Çeviri:** `httpx`, `deep-translator`
- **Güvenlik ve Konfigürasyon:** `python-dotenv`
- **Veri Saklama:** Lokal JSON (Hafif ve portatif)

---

## 📁 Dosya Yapısı (İdeal Repo Anatomisi)
```text
/lara_bot
│
├── src/                    # 🚀 Ana Kaynak Kodlar
│   ├── app.py              # Botun giriş ve çalıştırma noktası
│   ├── test_logic.py       # Birim testler ve hata ayıklama
│   └── debug_api.py        # Epic Games API mock / test scripti
│
├── data/                   # 💾 Yerel Veritabanı (Git'e eklenmez)
│   ├── database.json       # Kullanıcı ve metrik verileri
│   └── stats.txt           # Ek lokal istatistikler
│
├── docs/                   # 📚 Dokümantasyonlar ve medya
│
├── .env                    # 🔑 GİZLİ: Çevresel değişkenler (Git'e eklenmez)
├── .gitignore              # 🛑 Git istisnaları
├── requirements.txt        # 📦 Bağımlılık listesi
└── README.md               # 📖 Proje vitrini ve kurulum yönergeleri
```

---

## ⚙️ Kurulum ve Kullanım

1. **Repoyu Klonlayın:**
   ```bash
   git clone <repo-url>
   cd lara_bot
   ```

2. **Gereksinimleri Yükleyin:**
   Sanal bir ortam (virtualenv) kullanmanız önerilir.
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Güvenlik Dosyalarını Oluşturun:**
   Proje kök dizininde `.env` isimli bir dosya oluşturun ve hassas verilerinizi ekleyin:
   ```env
   TOKEN=123456789:ABCDEF_GHIJKLMNOPQRSTUVWXYZ
   ADMIN_ID=123456789
   ```

4. **Botu Başlatın:**
   ```bash
   python src/app.py
   ```

## 📜 Lisans
Bu proje, akademik bir portfolyo çalışması olarak geliştirilmiş olup kişisel kullanım için tamamen uygundur.
