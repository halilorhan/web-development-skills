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

## Kapanış protokolü
1. FAIL/BLOCKED maddeleri, konum/etki/çözümle raporlanır.
2. Düzeltmeler yalnız etkilenen alanlara minimum patch ile uygulanır.
3. Yeniden test kapsamı değişiklik riskine göre ayarlanır.
4. Final kabulde site URL'si, commit/release, tarih, yedek referansı, açık risk ve son test kanıtı bulunur.

## Kabul kuralı
Kritik başarısızlık varsa “tamamlandı” denmez. Belge listesinin GitHub'a kaydı **dokümantasyonun tamamlanmasıdır**, gerçek web sitesinin otomatik test edildiği anlamına gelmez.
