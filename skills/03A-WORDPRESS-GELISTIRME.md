# 03A — WordPress Geliştirme

**Sürüm:** 1.0  
**Kapsam:** WordPress projeleri  
**Amaç:** WordPress sitesini minimum bağımlılık, temiz yapı ve yönetilebilir içerik modeliyle geliştirmek.

## Ön Koşul
01 ve 02 numaralı skill çıktıları hazır olmalıdır.

## Girdiler
- Sayfa ve veri mimarisi
- Onaylı tasarım sistemi
- Kullanılacak tema/child theme
- Gerekli eklentiler ve entegrasyonlar

## İş Akışı
1. WordPress çekirdeğine doğrudan müdahale etme.
2. Tema özelleştirmelerini child theme veya kontrollü özel kod alanında tut.
3. Projeye özel iş mantığını mümkünse ayrı özel eklentide tut.
4. Global header/footer/component yapısını kur.
5. İçerik tipleri, alanlar, kategoriler ve gerekiyorsa özel post type yapılarını oluştur.
6. Sayfaları tasarım sistemine göre geliştir.
7. Form ve dinamik alanları gerçek veriyle bağla.
8. Gereksiz eklentileri kaldır.
9. Değişiklikleri GitHub'da sürümle.

## Kurallar
- WordPress core dosyaları değiştirilmez.
- Aynı işi yapan birden fazla eklenti kullanılmaz.
- Salt görsel ihtiyaç için ağır eklenti eklenmez.
- Eklenti güncellemesi öncesi uyumluluk ve rollback düşünülür.
- API anahtarları, şifreler ve environment değerleri repoya girmez.
- Veritabanında elle ve iz bırakmadan kritik değişiklik yapılmaz.
- Çalışan rezervasyon, ödeme, üyelik veya form mantığı tasarım değişikliği sırasında bozulmaz.
- Kod değişikliği ile içerik değişikliği mümkün olduğunca ayrılır.

## Tamamlanma Kriteri
Site yönetim panelinden sürdürülebilir biçimde yönetilebiliyor, özel geliştirmeler core'dan ayrılmış ve tüm değişiklikler GitHub üzerinden izlenebiliyorsa tamamlanmıştır.
