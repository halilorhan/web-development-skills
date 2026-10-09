# Yeni Kurumsal Site Başlatma Prosedürü

1. **ChatGPT Project talimatlarına** `CHATGPT-PROJE-BASLANGIC-TALIMATI.md` dosyasını ekle veya aynı kapsamda merkezî GitHub okuma yükümlülüğünü belirle. Bu işlem uygulanmadan otomatik okunduğunu varsayma.
2. Yeni müşteri için ayrı GitHub repo; ASGE'nin kişisel medya/içerik verisini asla taşımadan proje kayıtlarını oluştur.
3. Bağlı GitHub, WordPress MCP, hosting/panel araçlarını **asistan önce kendisi gerçek çağrılarla doğrulasın**; yetki eksikliğini ancak somut testten sonra raporlasın.
4. Merkezî kuralları oku, başlangıçta erişilen SHA/branch, proje talimatı ve tarih kaydını sabitle. İleride değişen master kuralları müşteri projesine sessizce uygulama.
5. İçerik ve URL envanteri, bilgi mimarisi, tasarım sistemi, WordPress mimarisi, medyalar ve entegrasyonlar sırayla üretilsin.
6. Elementor mevcut sayfalarına full-page write uygulanmasın. Kısmi widget/container değişikliği dışında sessiz alternatif kullanılmasın.
7. Staging test, yedek doğrulama, SEO migrasyonu, domain/SSL/WordPress URL kontrolü, üretim kabul ve rollback ile tamamla.
8. Teslimatta değişiklik kayıtları, açık riskler, test kanıtları ve üretim durumu net ayrılsın.

## Merkez kaynak
- GitHub repo: `halilorhan/web-development-skills`
- Genel kurallar: `premium-wordpress-starter/standards/`
- 8 geliştirme rehberi: `premium-wordpress-starter/starter/`
- Master WordPress skill'leri: `skills/01`, `02`, `03A`, `04`, `05`, `06`, `07`.

## Değişiklik yönetimi
Yeni bir genel kural önce merkezî dosyada değiştirilir, belirli proje için etkisi ve test gereksinimi incelenir. Her müşterinin proje-özel kararları ayrı repoda kalır.

## Kontrol senaryosu
Yeni bir müşteri projesinde "WordPress siteyi başlat" talebi üzerine asistan kullanıcıya önce SSH/bağlantı istemek yerine bağlı araçları denetlemeli, merkezî belgeleri okumalı, repo ve WordPress hedeflerini bulmalıdır. Mevcut Elementor sayfasında tek başlık değişimi istenirse yalnız ilgili öğeyi güncellemeli; full-page write yapmayı reddetmelidir.

## Bilinen sınır
Buradaki dosyalar GitHub üzerinde doğrulanabilir. Ancak farklı ChatGPT Project'lerine dosyaların otomatik eklenmesi, bu GitHub klasörünün oluşturulmasıyla gerçekleşmez; bir kez proje özelinde bağlanması gerekir.
