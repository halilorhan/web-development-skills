# 03B — Özel Yazılım Geliştirme

**Sürüm:** 1.0  
**Kapsam:** Özel yazılım web projeleri  
**Amaç:** Yönetim paneli bulunan, modüler, güvenli ve sürdürülebilir özel web uygulaması geliştirmek.

## Ön Koşul
01 ve 02 numaralı skill çıktıları hazır olmalıdır.

## Girdiler
- Teknik mimari
- Veri modeli
- Tasarım sistemi
- Kullanıcı rolleri
- İş kuralları ve entegrasyon gereksinimleri

## İş Akışı
1. Proje iskeletini ve environment yapısını oluştur.
2. Veritabanı şemasını migration ile tanımla.
3. Kimlik doğrulama ve yetki katmanını kur.
4. Yönetim panelinin temel modüllerini oluştur.
5. API/servis katmanı ile arayüzü ayır.
6. Tekrarlanan UI componentlerini oluştur.
7. İş kurallarını modüler servislerde uygula.
8. Hata yönetimi ve loglamayı ekle.
9. Testleri çalıştır ve GitHub'da sürümle.

## Kurallar
- Secret ve environment değerleri repoya yazılmaz.
- Veritabanı değişiklikleri migration dışı yapılmaz.
- Input doğrulaması yalnız frontend'e bırakılmaz.
- Yetki kontrolü yalnız arayüzde yapılmaz; backend zorunludur.
- Aynı iş kuralı farklı dosyalarda kopyalanmaz.
- Route/controller içine gereksiz iş mantığı yığılmaz.
- Yönetim paneli veri yapısını doğrudan ve kontrolsüz değiştiremez.
- Kritik işlemler hata halinde tutarlı duruma geri dönebilmelidir.

## Tamamlanma Kriteri
Uygulama temiz kurulumda ayağa kalkıyor, migration ile veritabanını oluşturuyor, yetkiler doğru çalışıyor, yönetim paneli temel verileri yönetiyor ve kod GitHub üzerinden yeniden üretilebiliyorsa tamamlanmıştır.
