# 05 — Entegrasyonlar

**Sürüm:** 1.0  
**Kapsam:** Tüm web projeleri  
**Amaç:** Harici servisleri güvenli, test edilebilir ve bağımsız biçimde siteye bağlamak.

## Kapsam Örnekleri
SMTP, WhatsApp, Google Analytics, Search Console doğrulaması, Tag Manager, Meta Pixel/CAPI, Maps, CRM, ödeme sağlayıcıları, kargo servisleri, harici API'ler.

## İş Akışı
1. Entegrasyonun amacını ve veri akışını tanımla.
2. Test/sandbox imkanı varsa önce onu kullan.
3. Anahtar ve secret değerlerini environment/secret alanında tut.
4. Entegrasyonu tek bir kontrollü katmandan bağla.
5. Başarılı ve başarısız senaryoları test et.
6. Timeout, hata ve tekrar deneme davranışını tanımla.
7. Gerekli logları oluştur; hassas veriyi loglama.
8. Canlı bilgileri yalnız test tamamlandıktan sonra etkinleştir.

## Kurallar
- Secret, token, şifre ve özel anahtar GitHub'a commit edilmez.
- Entegrasyon başarısızlığı tüm siteyi çökertmemelidir.
- Aynı servis birden fazla yöntemle paralel bağlanmaz.
- Gereksiz izleme kodu eklenmez.
- Kullanıcı verisi yalnız gerekli servislerle paylaşılır.
- Ödeme ve sipariş iş kuralları 08-ETICARET skill'inde kalır; burada yalnız bağlantı katmanı kurulur.

## Tamamlanma Kriteri
Entegrasyon gerçek senaryoda çalışıyor, hata senaryosu kontrol edilmiş, secret değerleri güvenli tutuluyor ve entegrasyon kaldırıldığında ana uygulama çalışmaya devam edebiliyorsa tamamlanmıştır.
