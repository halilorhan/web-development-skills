# 08 — Premium Web Proje Kalite Kontrolü

> **Bağlayıcı önkoşullar:** `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md` ve `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`. Bu iki standart diğer rehberlerin tamamından önce uygulanır. Proje özelindeki onaylı tasarım kilidi ve güvenlik kuralları korunur.
> **Kaynak:** ASGE `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`; `halilorhan/web-development-skills` master 01, 02, 03A, 04, 05, 06, 07. ASGE'ye özel metinler, ID'ler ve sayısal değerler yeni müşteriye taşınmaz.

## Teslimat kapıları
Her maddenin durumu `PASS / FAIL / BLOCKED / N/A` olarak belgelenir; `BLOCKED` ve `N/A` gerekçelendirilir. “Hatasız” etiketi test kanıtı olmadan verilmez.

### A — Erişim ve proje yönetimi
- [ ] GitHub repo ve gerçek okuma/yazma erişimi uygun araç çağrılarıyla doğrulandı.
- [ ] WordPress staging/production site URL ve erişimleri karıştırılmadan ayrı kontrol edildi.
- [ ] Hosting/panel, SSL, DB ve yedek yöntemi doğrulandı; kullanıcıya gereksiz bağlantı talebi iletilmedi.
- [ ] `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `SITE-MAP.md`, URL map güncel.

### B — Tasarım ve UX
- [ ] Gerçek marka kimliği, logo, font ve görsel tutarlılık var.
- [ ] Header, sticky davranış, dropdown konumu, mobil menü ve footer çalışıyor.
- [ ] Hero mesajı, hizmet gezinimi, güven unsurları ve CTA görünür.
- [ ] Desktop/tablet/mobile kontrol edildi; taşma, kırpılma ve responsive anormalliği yok.
- [ ] Hareket/animasyon klavye ve `prefers-reduced-motion` ile uyumlu.

### C — Elementor güvenliği
- [ ] Mevcut sayfalarda **full-page write yapılmadı**.
- [ ] Her düzenleme öncesi gerçek kaynak ID ve bağımlı template'ler okundu.
- [ ] Kısmi düzenleme ve öncesi/sonrası hedefli diff yapıldı.
- [ ] Wrapper, header/footer, element ID, siblings ve responsive ayarlar korundu.
- [ ] Birden çok sayfaya etki eden global değişikliklerde kapsam testi yapıldı.

### D — Yazılım ve veri
- [ ] WordPress core değişmedi; özel iş mantığı child theme veya eklentide.
- [ ] Gereksiz/çift eklenti yok; CMS içerik modeli yönetilebilir.
- [ ] Form validasyonları, boş ve hatalı API durumları testli.
- [ ] Gizli anahtar/token GitHub'da veya loglarda yok.
- [ ] Eklenti/tema güncellemeleri için rollback planı mevcut.

### E — İçerik, medya ve SEO
- [ ] Sahte referans, sertifika, başarı, rakam veya güncel olmayan iddia yok.
- [ ] Görseller tutarlı, optimize, doğru alt metinli; kırık resim ve placeholder yok.
- [ ] URL migration tablosu tamam; önemli eski URL aynı adres veya doğru 301.
- [ ] Canonical, title, description, robots/index, sitemap ve structured data doğrulandı.
- [ ] Staging noindex, production indeksleme ayarları bilinçli ve doğru.

### F — Performans, güvenlik ve yayın
- [ ] LCP/CLS/INP ölçümleri mümkün olduğu durumda raporlandı.
- [ ] HTTPS, mixed content, erişim rolleri, hassas veri ve hata sayfaları kontrol edildi.
- [ ] Production dosya+DB ve staging kaynak yedekleri doğrulandı.
- [ ] Ana sayfa, hizmetler, iletişim, kritik CTA, formlar, header/footer ve mobil akışlar test edildi.
- [ ] Domain/SSL, WP home/siteurl, medya, 301/404, Search Console/sitemap kontrol edildi.
- [ ] Kullanılabilir rollback, yayın kaydı ve müşteri onayı var.

## K1–K4 premium kanıt kapısı — tamamlanmış proje için

Her yeni müşteri reposunda `PROJECT-QUALITY-GATE.json` tutulur. Örnek şema `../templates/PROJECT-QUALITY-GATE.example.json`; kontrol betiği `../templates/check_quality_gate.py`. Bu dosya mevcut A–F kontrol maddelerinin **yerine geçmez**, faz onaylarının doğrulanabilir özetidir.

| Kapı | PASS için asgari delil | FAIL/BLOCKED ise |
| --- | --- | --- |
| **K1 Kaynak** | Marka/referans kaydı, gerçek varlık durumu, ilgili kaynak bağlantısı veya dosya referansı | Kritik marka/içerik bilinmiyorsa uydurma veya yayın yok |
| **K2 Pilot** | Gerçek desktop/mobil pilot görüntü referansı, referansla somut karşılaştırma, müşterinin tasarım onay kaydı | Seri sayfa üretimi ve canlı yayın yok |
| **K3 Kalite** | Desktop/tablet/mobile kanıtı, menü/CTA ve gerçek içerik kontrolleri, sıfır kritik görsel/işlev hatası | Hedefli düzeltme, etkileneni yeniden kontrol |
| **K4 Yayın** | Production hedefi, dosya+DB yedek/rollback referansı, kullanıcının yayın onayı, kayıtlı dağıtım yöntemi | Production publish/deploy yok |

**Delil standardı:** Dosya adı, gerçek URL veya onay/talimat referansı kullan; “test edildi”, “müşteri onayladı”, “premium” ifadeleri tek başına PASS olamaz. Bot, kanıt alanlarının varlığını ve durum değerlerini denetleyebilir; estetik kaliteyi veya kullanıcının gerçekten onay verdiğini **tek başına teyit edemez**. Görsel karşılaştırma ve onayın asıl doğrulanması insan/görsel incelemedir.

**İki ayrı yayımlama hattı:** GitHub workflow üzerinden deploy varsa CI kontrolü + branch/environment koruması yayın önkoşulu olarak uygulanabilir. Orange MCP/panel üzerinden WordPress'e doğrudan yazılıyorsa GitHub workflow bunu otomatik engellemez; aynı kapılara uymak asistanın zorunlu operasyon davranışıdır. Teknik kontrol kurulmadıysa kurulmuş gibi raporlama.

**Kapsam istisnası:** Daha önce onaylı sitedeki küçük, noktasal bir metin/görsel düzeltmesi yeni pilot ve yeni kullanıcı yayını gerektirmeyebilir. Bu durumda yalnız değişen alanın gerekli testi ve geri dönüşü yapılır; mevcut tasarım kilidi korunur.

## Kapanış protokolü
1. FAIL/BLOCKED maddeleri, konum/etki/çözümle raporlanır.
2. Düzeltmeler yalnız etkilenen alanlara minimum patch ile uygulanır.
3. Yeniden test kapsamı değişiklik riskine göre ayarlanır.
4. Final kabulde site URL'si, commit/release, tarih, yedek referansı, açık risk ve son test kanıtı bulunur.

## Kabul kuralı
Kritik başarısızlık varsa “tamamlandı” denmez. Belge listesinin GitHub'a kaydı **dokümantasyonun tamamlanmasıdır**, gerçek web sitesinin otomatik test edildiği anlamına gelmez.
