# AI Pulse — Marketing Project Brief

> **Bu dosya neden var?** Bu klasördeki iş, "AI Pulse" adlı dijital ürünün pazarlama/satış
> malzemesini üretmek içindir. Farklı bir model veya sonraki bir oturum bu klasörü açtığında
> ne yaptığımızı, neden yaptığımızı ve hangi kararların alındığını tek bakışta anlasın diye
> yazılmıştır. Okumadan değişiklik yapma.

---

## 1. Ürün Nedir? (Kaynak Proje)

- **Ürün adı:** AI Pulse — Model Radar
- **Sahibi:** Ali (GitHub: `T-a-c-h-y-o-n`)
- **Kaynak kod / ürün yeri:** `/home/ali/Belgeler/OpenClaude/AI_News_Dashboard - Personal`
  (ayrıca GitHub: `https://github.com/T-a-c-h-y-o-n/aipulse`)
- **Ne olduğu:** 600+ AI modelini ve 170+ şirketi **tek bir HTML dosyasında** karşılaştıran,
  sıfır-kurulum bir dashboard. Parametre, context penceresi, fiyat, benchmark, lisans ve
  topluluk trendi tek ekranda.
- **Çekirdek özellik (gerçek ve çalışıyor):** `tools/pipeline.py` komutu HuggingFace +
  OpenRouter'dan yeni modelleri çekip dashboard'u günceller. "Kendi güncelle" iddiası
  BOŞ DEĞİL, pipeline gerçekten çalışıyor (Python 3.8+, ek paket yok).
- **Ürün tipi:** Dijital indirilebilir dosya (tek HTML + Python araçları).
- **Lisanslar:**
  - **Personal Edition** — tek kullanıcı, ömür boyu, bireysel/serbest kullanım. Gumroad'da $29 (one-time).
  - **Team Edition** — çok kullanıcı. GitHub'daki ana repo ile tanıtılıyor.
- **Satış kanalı:** Gumroad — `https://tachyon80.gumroad.com/l/aipulse-personal`
- **Canlı demo:** `https://aipulses.vercel.app/` (~50 modelle sınırlı ücretsiz demo)
- **Marka sesi / tasarım dili:** turuncu `#ff5b1f`, koyu tema, "radar / track / no subscription"
  tonu. Dashboard fontları: **JetBrains Mono** (gövde) + **Nunito** (başlık).
- **İletişim:** `Tachyonic@gmail.com`

---

## 2. Bu Projenin Amacı (Neden Varız?)

Ürün **teknik olarak sağlam** ama **satış motoru eksikti**: trafik yok, satış sayfası zayıf,
dönüşüm/tutundurma sistemi yok. Ali'nin net talimatı:

> "Trafiğim olsaydı sana yazmıyordum. Boş analiz yapma, üret. Yeni bir klasör aç, orada çalış."

Bu yüzden bu klasör (`aipulse marketing`) **saf üretim kısmıdır** — ürünü global (ABD dahil)
pazara satmak için gereken tüm pazarlama varlıklarını burada üretiyoruz.

**Global hedef:** Sayfa **İngilizce**. ABD ve uluslararası satış hedefleniyor. Türkçe değil.

**İlerleme felsefesi (Ali'nin net kuralı):** Analiz/teori üretme, somut çıktı ver. "Şu yok bu yok"
demek yok; eksikse sen üret.

---

## 3. Klasör Yapısı — `/home/ali/Belgeler/OpenClaude/aipulse marketing/`

```
aipulse marketing/
├── PROJECT.md              # Bu dosya — projenin tamamı burada
├── index.html              # ANA ÇIKTI: Landing page (Hormozi konsepti)
├── assets/                 # Tüm görseller burada
│   ├── pulse2.png          # Logo (32x32)
│   ├── dashboard-top.png   # Dashboard screenshot
│   └── aipulse.png         # Ek screenshot
└── shot.py                 # Playwright screenshot scripti
```

---

## 4. Landing Page (`index.html`) — Tasarım Kuralları

### 4.1 Sayfa Akışı (Hormozi Dönüşüm Mantığı)

Sayfa 6 section'dan oluşur (9 değil). Her section'ın amacı:

1. **Hero**: Hook + Dream Outcome + CTA + Trust
2. **Proof**: Gerçek screenshot + demo linki
3. **Offer**: Grand Slam Offer ($29 + ne alırsın + garanti + fiyat karşılaştırması)
4. **How**: 3 adım (indir → aç → güncelle)
5. **FAQ**: 4 soru
6. **CTA**: Son çağrı

### 4.2 Hormozi Konseptleri Uygulandı

- **Value Equation**: Dream Outcome (tüm modelleri gör) × Likelihood (screenshot + demo) ÷ Time (kurulum yok) ÷ Effort (tek dosya)
- **Grand Slam Offer**: Ürün + Promosyon + Garanti + Fiyat algısı
- **Hooks**: "Stop guessing which AI model to use" — acı noktası doğrudan
- **Proof**: Gerçek screenshot + canlı demo linki
- **Fiyat Karşılaştırması**: "ChatGPT Plus $20/ay, bu $29 bir kere"

### 4.3 Dil ve Fontlar

- **Dil:** İngilizce, kısa cümleler, güçlü fiiller. AI kokan ifadeler yok.
- **Başlıklar:** Nunito (font-family h1/h2/h3/.brand)
- **Gövde:** JetBrains Mono
- **Google Fonts CDN** ile yükleniyor.

### 4.4 Tema

- **Koyu tema varsayılan** (`:root` değişkenleri).
- **Açık tema** mevcut: `body.light` sınıfı ile. Sağ üstteki ☀/🌙 düğmesi (`#themeToggle`)
  temayı değiştirir, seçim `localStorage`'a kaydolur.
- Açık temada header arka planı beyaz olmalı.

### 4.5 Butonlar

- Tüm butonlar `.btn` class'ı ile: turuncu gradyan, beyazımsı yazı.
- Header'daki "Get it — $29" butonu: `.btn-buy` (siyah yazı, hover'da beyaz).
- Hero'daki iki buton da aynı `.btn` class'ını kullanır.

### 4.6 Görseller

- Tüm görseller `assets/` klasöründe.
- `pulse2.png`: Logo (32x32, header'da).
- `dashboard-top.png`: Ana screenshot (proof section'da).
- `aipulse.png`: Ek screenshot (gerekirse).

---

## 5. Kararlar / Geri Bildirimler

1. Sayfa İngilizce olmalı (global/ABD satışı).
2. Fontlar ürünle aynı: **JetBrains Mono + Nunito**.
3. Hormozi konsepti uygulandı: Grand Slam Offer, Value Equation, Hooks, Proof.
4. Section sayısı 9'dan 6'ya düşürüldü: daha temiz, daha net.
5. "Who it'sfor" ve "Before/After" çıkarıldı: tekrar, gereksiz.
6. Offer section'ı üstte: teklif hemen görünmeli.
7. Fiyat karşılaştırması eklendi: ChatGPT Plus $20/ay vs $29 bir kere.

---

## 6. Bağlantılar (Sabit — Değiştirme)

| Nedir | URL |
|---|---|
| Gumroad (satış) | `https://tachyon80.gumroad.com/l/aipulse-personal` |
| Canlı demo | `https://aipulses.vercel.app/` |
| GitHub | `https://github.com/T-a-c-h-y-o-n/aipulse` |
| İletişim | `mailto:Tachyonic@gmail.com` |

---

## 7. Sıradaki Adımlar (Yapılacaklar — Ali onaylayınca)

- [ ] Landing page'i **Vercel / GitHub Pages'e deploy** edip gerçek URL'den yayına al. ✓ Vercel'de canlı
- [ ] `dashboard-top.png`'i Ali güncelleyince sayfayı son kez kontrol et. ✓ dashboard-top2.png eklendi
- [ ] (Opsiyonel) Demo → email → Gumroad dönüşüm hunisi için lead magnet bölümü.
- [ ] (Opsiyonel) Team Edition için ayrı satış sayfası.
- [ ] (İlerisi) Trafik: LinkedIn/YouTube içerik + affiliate sistemi.

---

## 9. Yapılacaklar (Geri Kalan İşler)

### Yüksek Öncelik
- [ ] **Google Search Console'a ekle** — landing page'iGoogle'a index'let
- [ ] **Sitemap'ıGoogle'a gönder** — `sitemap.xml` dosyasınıGoogle Search Console'da test et
- [ ] **Reddit r/LocalLLaMA'da post paylaş** — post taslağı hazır (aşağıda)

### Orta Öncelik
- [ ] **GEO-SEO index'lenme kontrolü** —1-2 hafta sonraChatGPT/Perplexity'de "AI Pulse" diye ara
- [ ] **Blog/makale ekle** — "How to compare AI models" gibiSEO-friendly içerik
- [ ] **Email lead magnet** — "AI Model Comparison Guide" PDF'i

### Düşük Öncelik
- [ ] **LinkedIn post serisi** — haftalık "AI model karşılaştırma" içerikleri
- [ ] **Product Hunt momentum** — upvote kampanyası, yorum yönetimi

---

## 10. Reddit Post Taslağı (r/LocalLLaMA)

**Title:**
> I built a single HTML file that compares600+ AI models — price, benchmarks, context window, all in one screen

**Body:**
> Every time a new model drops, I was checking3-4different sites to compare pricing and benchmarks. Got tired of it.
> 
> So I built a dashboard in one HTML file — no backend, no install. Just open it. It pulls from HuggingFace and OpenRouter, so new models show up within a day.
> 
> What surprised me: [1-2ilginç bulgu, mesela "model X is3x cheaper than model Y for the same benchmark score"]
> 
> Free demo (50 models): https://aipulses.vercel.app/
> GitHub: https://github.com/T-a-c-h-y-o-n/aipulse/
> 
> Happy to answer questions about the data pipeline or what's next.

**İpuçları:**
- Post'u Salı/Çarşamba sabahı paylaş (en aktif zaman)
- Yorumlara4saat içinde cevap ver
- "What surprised me" yerine kendi deneyiminden bir şey yaz

---

## 11. GEO-SEO Uygulamaları (Tamamlandı)

| Uygulama | Durum |
|----------|-------|
| `llms.txt` | ✓ AI bot'ları için site yapısı |
| `robots.txt` | ✓ AI bot'larına izin |
| `sitemap.xml` | ✓ Oluşturuldu |
| H1/H2 başlık yapısı | ✓AI-alıntısına uygun |
| Internal linking | ✓ Navigation'a eklendi |
| Open Graph tags | ✓ Sosyal paylaşım için |
| Brand mentions | ✓ Meta description güncellendi |
| Schema markup | ✓ SoftwareApplication eklendi |

---

## 12. Bağlantılar (Sabit — Değiştirme)

| Nedir | URL |
|---|---|
| Landing Page | `https://aipulse-landing.vercel.app/` |
| Canlı demo | `https://aipulses.vercel.app/` |
| Gumroad (satış) | `https://tachyon80.gumroad.com/l/aipulse-personal` |
| Team Edition | `https://tachyon80.gumroad.com/l/aipulse-team` |
| GitHub | `https://github.com/T-a-c-h-y-o-n/aipulse` |
| Product Hunt | `https://www.producthunt.com/products/ai-pulse-model-radar` |
| R10.net Makale | `https://www.r10.net/yapay-zeka/4818865-ai-pulse-model-radar-yapay-zeka-modellerini-tek-yerden-takip-edin-kampanyali-fiyat.html` |
| İletişim | `mailto:Tachyonic@gmail.com` |

---

Son güncelleme: 2026-07-08
