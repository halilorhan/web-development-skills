# Premium WordPress Starter — ASGE'den Öğrenilen Çalışma Sistemi

Bu dizin, ASGE deneyiminden türetilen ve tüm kurumsal WordPress projelerinde uyarlanarak kullanılan **merkezî, markadan bağımsız çalışma standardıdır**. GitHub merkezi: `halilorhan/web-development-skills`, klasör: `premium-wordpress-starter/`. Yeni proje için `../CHATGPT-PROJE-BASLANGIC-TALIMATI.md` ve `../NEW-PROJECT-README.md` kullanılır.

## Öncelik sırası
1. Güvenlik, kullanıcı onayı, proje özelindeki açık ve son kararlar.
2. `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md`: var olan GitHub / WordPress / sunucu bağlantılarını önce keşfet ve doğrula; gereksiz kullanıcı işlemi isteme.
3. `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`: mevcut Elementor sayfasına **full-page write kesinlikle yasak**; yalnız hedefli bölüm/widget düzenlemesi.
4. Bu klasördeki 01–08 rehberleri, görev sırasıyla.
5. `halilorhan/web-development-skills` master skill'leri 01, 02, 03A, 04, 05, 06 ve 07; genel WordPress kurumsal projeler için 03B ve 08 kapsam dışıdır.

## Rehberler
- [01 Proje Başlangıcı](01-PROJE-BASLANGIC.md) — kapsam, marka, rakip, site ve SEO envanteri
- [02 Premium Tasarım](02-PREMIUM-TASARIM.md) — tasarım sistemi, görsel hiyerarşi, responsive
- [03 WordPress Mimari](03-WORDPRESS-MIMARI.md) — teknik yığın, kontrollü bileşenler, özel plugin
- [04 Sayfa Üretimi](04-SAYFA-URETIM.md) — sayfa bazlı güvenli üretim ve noktasal düzenleme
- [05 Görsel Sistemi](05-GORSEL-SISTEM.md) — görsel brief, üretim, gerçekçilik, performans
- [06 SEO ve Performans](06-SEO-PERFORMANS.md) — eski URL mirası, arama, hız
- [07 Test ve Yayın](07-TEST-YAYIN.md) — staging, yedek, hosting, domain, SSL, rollback
- [08 Kalite Kontrol](08-KALITE-KONTROL.md) — teslim ve regresyon kapıları

## Proje başlangıç iş akışı
1. Önce repo, WordPress MCP ve hosting erişimini **gerçekten** denetle; erişimi olmayan katmanı yalnız somut testle belirt.
2. Yeni müşteri için ayrı repo ve özel proje kayıtları aç: `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`.
3. 01–02 tamamlanmadan tasarım/kod uygulamasına geçme. Önce tasarım sistemi, sonra ortak bileşenler, sonra sayfalar.
4. Mevcut sayfaya değişiklik yapılırken `_elementor_data` tamamına, tam HTML'ye ve `post_content` bütününe overwrite yapma; güvenli kısmi API yoksa işlemi durdur.
5. Gerçek içerik ve işlevleri doğrula, yalnız etkilenen alanı test et; kritik yayında regresyon kapsamını genişlet.
6. Yedek, URL kontrolü, kullanıcı onayı ve rollback planıyla canlıya al.

## Yeniden kullanım sınırları
ASGE'nin kendine özgü danışmanlık metinleri, müşteri logoları, kişi görselleri, site/şablon ID'leri, alan adları, özel lead ve teşvik veri modeli başka müşteriye kopyalanmaz. Genel tasarım sistemi prensipleri, çalışma sırası, güvenli modüler WordPress yaklaşımı yeniden kullanılır.

## Tamamlanmışlık tanımı
Dokümantasyonun GitHub'da varlığı bir sitenin teknik olarak üretime hazır olduğunu kanıtlamaz. Her yeni projenin kabul kriterleri ayrıca tamamlanır.
