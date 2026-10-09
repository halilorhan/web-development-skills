# 01 — Proje Başlangıcı, Keşif ve Mimari

> **Bağlayıcı önkoşullar:** `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md` ve `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`. Bu iki standart diğer rehberlerin tamamından önce uygulanır. Proje özelindeki onaylı tasarım kilidi ve güvenlik kuralları korunur.
> **Kaynak:** ASGE `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`; `halilorhan/web-development-skills` master 01, 02, 03A, 04, 05, 06, 07. ASGE'ye özel metinler, ID'ler ve sayısal değerler yeni müşteriye taşınmaz.

## Amaç
Siteyi inşa etmeden önce marka, iş hedefleri, bilgi mimarisi, SEO mirası, veri modeli, bütçe/süre ve erişim sınırlarını netleştir. ASGE dersi: eski tasarımı korumak zorunda olmadan **organik URL geçmişini** korumak mümkündür.

## Gerekli girdiler
- Müşterinin resmi brief'i, logo/renk/font, mevcut site ve içerik kaynakları.
- Asıl alan adı, staging, hosting uygulamaları, DNS, SSL ve yedekleme durumu.
- Hedef müşteriler, hizmetler, dönüşüm türleri, formlar, entegrasyonlar.
- Mevcut indeksli sayfalar, sitemap, redirect ve Search Console bilgileri (yetki varsa).
- Referans siteler: örnekler benchmark'tır, doğrudan kopyalanmaz.

## Uygulama sırası
1. Önce mevcut araç erişimlerini gerçek çağrıyla denetle; önceden bağlı servisi kullanıcıya tekrar bağlatma.
2. Mevcut siteyi masaüstü/mobil, içerik, SEO ve performans açısından envanterle.
3. Yeni sitenin hedefini yaz: marka algısı, hizmet keşfi, güven, dönüşüm, hız ve yönetilebilirlik.
4. Sayfa/menü/hizmet gruplarını ve kullanıcı yolculuklarını `SITE-MAP.md` içinde karara bağla.
5. Korunacak/değişecek URL'leri `URL-MIGRATION-MAP.csv` içinde kaydet: old URL, new URL, 301, durum, gerekçe, test.
6. Veri modelini tanımla: statik sayfa, yazı, taksonomi, gerekiyorsa CPT ve yapılandırılmış alanlar.
7. Teknik sınırları ve eklenti listesini seç; kullanmayacağın modülleri ve entegrasyonları açıkla.
8. Staging / production sınırını, onaylı yayın sürecini, backup ve rollback'i tanımla.
9. `PROJECT-INSTRUCTIONS.md` ve `DECISIONS.md` ile kararları sabitle; riskleri listele.

## Çıktılar
- Tek sayfalık hedef/kapsam özeti ve onay kriteri
- Site haritası + içerik önceliklendirmesi
- URL migration tablosu
- Teknik mimari / veri yapısı / form akışı
- Repo, ortam, yedek ve test stratejisi

## Stop koşulları
Gerçek logo, kritik kurumsal iddia, alan adı sahipliği, yıkıcı taşıma ve veritabanı yedeği belirsizse riskli uygulama yapılmaz. Eksik küçük bilgiler açık varsayım olarak kaydedilir.

## Kabul
Yeni bir geliştirici repo dokümanlarına bakarak neyi, nerede, hangi sıra ve onayla yapacağını çıkarabiliyor olmalıdır.
