# 03 — WordPress Yazılım Mimarisi

> **Bağlayıcı önkoşullar:** `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md` ve `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`. Bu iki standart diğer rehberlerin tamamından önce uygulanır. Proje özelindeki onaylı tasarım kilidi ve güvenlik kuralları korunur.
> **Kaynak:** ASGE `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`; `halilorhan/web-development-skills` master 01, 02, 03A, 04, 05, 06, 07. ASGE'ye özel metinler, ID'ler ve sayısal değerler yeni müşteriye taşınmaz.

## Referans teknoloji
WordPress + Hello Elementor + Elementor Pro + Rank Math; kontrollü child theme; yalnız gerektiğinde hafif özel eklenti. WP core ve üçüncü taraf eklenti dosyalarına doğrudan müdahale yok. Bu yığın ASGE referansıdır; yeni projede gerçek gereksinim ve lisans uyumu doğrulanır.

## Sorumluluk ayrımı
- **Core:** WordPress çekirdeği güncellenebilir kalır.
- **Tema/child theme:** Görünüm, scoped CSS, gerekli theme hooks.
- **Elementor:** Görsel component, editable içerik, global layout; her widget/container ayrı düzenlenebilir.
- **Özel plugin:** CPT, REST endpoint, form routing, validasyon ve iş mantığı; tema değişiminden bağımsız.
- **Rank Math:** Başlık, meta, schema, canonical, sitemap, robots ve yönlendirme kurgusu.
- **GitHub:** Geliştirilen kodlar, tasarım kararları, güvenli dağıtım kaydı; DB/media otomatik olarak repoda var sayılmaz.

## ASGE'den öğrenilen teknik model
ASGE `IMPLEMENTATION-STATE.md` içinde wrapper sayfalarının Elementor template kaynaklarına bağlandığı bir model kayıtlıdır. Örnek: homepage kaynak ID 1410, global header 1443, footer 1477; bazı yayımlanan sayfalar içerik kaynağı template ID'sini çağırır. Bu ID'ler yalnız ASGE içindir. Yeni projede ortak header/footer global tek kaynak, diğer sayfalar bağımsız editlenebilir component olmalı; wrapper yaklaşımı zorunlu değildir.
ASGE `asge-core` plugin'i dinamik destek programı CPT, alanlar, REST filtreleri ve ortak single template için; `asge-leads` form/lead mantığı için kullanıldı. Bu müşteri özelindeki iş mantığı başka projeye kopyalanmaz, yalnız **CPT + service-layer + form pipeline** örneği olarak incelenir.

## Güvenli değişiklik politikası — kritik
1. Mevcut Elementor sayfasının gerçek kaynak ID ve revision bilgilerini oku; wrapper ile kaynak template'i karıştırma.
2. Bölüm/widget düzeyinde küçük değişiklik yap. `_elementor_data`, post body veya tüm Elementor ağacı overwrite edilmez.
3. Global component'e müdahale, onu kullanan her sayfayı etkiler: bağımlılık envanteri ve kapsam testi yap.
4. Araç kısmi güncellemeyi desteklemiyorsa full-page write'a geçme; güvenli alternatif yoksa durdur ve gerekçeyi açıkla.
5. WordPress içeriğinin export'u ile gerçek tam-site backup aynı değildir. Medya, DB, plugin, tema, ayar ve gerekli lisans ayrımı yapılır.

## Veri ve API kriterleri
- CPT ve taksonomi yalnız gerçek veri gereksinimi varsa.
- Field validate/sanitize, output escape, capability/nonce kontrolleri.
- REST izin callback'i, sayfalama, boş durum, hata/timeout ve cache stratejisi.
- Formlar için spam önleme, gizlilik bildirimi, loglarda veri minimizasyonu, SMTP teslim kontrolü.
- Secret ve token kodda, GitHub'da ya da ekran raporunda tutulmaz.

## Kabul
Yönetilebilir içerik, izolasyonlu iş mantığı, global bileşen tutarlılığı, güvenli kısmi Elementor düzenlemeleri, izlenebilir kod ve geri dönüş yöntemi doğrulanmıştır.
