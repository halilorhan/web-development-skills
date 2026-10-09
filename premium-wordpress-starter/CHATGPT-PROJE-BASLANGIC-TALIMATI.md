# ChatGPT Project — Zorunlu Başlangıç Talimatı

> **Kullanım:** Bu metin, her yeni kurumsal WordPress ChatGPT Project'inin talimatlarına eklenmesi için hazırlanmıştır. Metnin GitHub'da bulunması, yeni ChatGPT Project'lerine kendiliğinden yüklendiği anlamına gelmez.

## Zorunlu ilk işlem
Bu projede herhangi bir tasarım, kod, WordPress, Elementor, yayın veya entegrasyon işi yapmadan önce şu merkezi kaynaktaki dosyaları **GitHub bağlantısı üzerinden oku ve uygula**:

**Repo:** `halilorhan/web-development-skills`
**Klasör:** `premium-wordpress-starter/`

1. `standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md`
2. `standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`
3. `starter/README.md`
4. `starter/01-PROJE-BASLANGIC.md`
5. `starter/02-PREMIUM-TASARIM.md`
6. `starter/03-WORDPRESS-MIMARI.md`
7. `starter/04-SAYFA-URETIM.md`
8. `starter/05-GORSEL-SISTEM.md`
9. `starter/06-SEO-PERFORMANS.md`
10. `starter/07-TEST-YAYIN.md`
11. `starter/08-KALITE-KONTROL.md`

Ek olarak bu repo altındaki master skill dosyaları `skills/01-PROJE-ANALIZ-MIMARI.md`, `skills/02-UIUX-TASARIM.md`, `skills/03A-WORDPRESS-GELISTIRME.md`, `skills/04-ICERIK-MEDYA-SEO.md`, `skills/05-ENTEGRASYONLAR.md`, `skills/06-TEST-GUVENLIK-PERFORMANS.md` ve `skills/07-GITHUB-VERSIYON-YAYIN-ROLLBACK.md` okunmalıdır. Kurumsal WordPress iş akışı için `03B` ve `08` kullanılmaz.

## KATI kurallar
- Önceden bağlı GitHub, WordPress MCP/WPVibe ve hosting/panel erişimini doğrulamadan kullanıcıdan yeniden bağlantı isteme.
- Daha önce başarısızlığı bildirilen SSH/terminal yöntemini tekrar dayatma.
- Mevcut Elementor sayfasına **full-page write / komple _elementor_data overwrite / tek dev HTML widget** uygulama. Bölüm/widget düzeyinde güvenli noktasal düzenleme yap.
- Kısmi yazma sağlayan güvenli araç yoksa tam sayfa overwrite'a geçme.
- Onaylı tasarımı sebepsiz değiştirme; üretim değişikliği öncesi yedek/hedef doğrulama, gerektiğinde onay, sonra doğrulama ve rollback planı.
- Projeye özel bilgileri ve en güncel kullanıcı kararlarını bu genel şablonun önüne koy. Gizli bilgiyi repoya kaydetme.
- Bitmiş iş ve kanıtlanmamış iş ayrımını açıkça belirt; tamamlanmış gibi gösterme.

## İlk oturumda oluşturulacak proje kayıtları
`PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `SITE-MAP.md`, `IMPLEMENTATION-STATE.md`, `URL-MIGRATION-MAP.csv`.

Yeni projenin özel kodu ve verileri yalnız o müşterinin reposunda tutulur. Bu merkezî klasör genel kuralların tek kaynağıdır. Birkaç sayfalık değişiklik uğruna tüm siteyi yeniden kurma.

## Erişim sınırı
GitHub deposu erişilebilir olduğu sürece bu talimatlar okunabilir. **Bütün yeni ChatGPT projelerine otomatik enjekte edilme garantisi yoktur.** Her yeni projenin Project talimatlarına bu başlangıç metni eklenmeli veya eşdeğer merkezi okuma kuralı tanımlanmalıdır.
