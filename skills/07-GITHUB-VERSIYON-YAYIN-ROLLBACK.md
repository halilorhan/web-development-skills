# 07 — GitHub, Versiyon, Yayın ve Rollback

**Sürüm:** 1.0  
**Kapsam:** Tüm web projeleri  
**Amaç:** Tüm kod değişikliklerini GitHub üzerinden izlenebilir, geri alınabilir ve kontrollü biçimde canlıya taşımak.

## Temel İlke
GitHub kod için ana kayıt kaynağıdır. SSH erişimine bağımlı bir çalışma akışı kurulmaz.

## İş Akışı
1. Repo yapısını proje başında tanımla.
2. Üretim kodunu korunan ana branch'te tut.
3. Değişiklikleri ayrı commitlerle ve anlaşılır mesajlarla kaydet.
4. Yayın öncesi testleri çalıştır.
5. Stabil sürümü tag/release ile işaretle.
6. Projenin tanımlı GitHub → hosting yayın yöntemiyle deploy et.
7. Yayın sonrası smoke test yap.
8. Sorun varsa son stabil tag/release'e rollback uygula.
9. Veritabanı değişikliği varsa kod ve veri sürüm uyumunu ayrıca kontrol et.

## Kurallar
- Şifre, token, private key ve `.env` repoya girmez.
- Canlıda elle yapılan kod değişikliği kalıcı yöntem değildir; repo ile eşitlenir.
- Tek commit içine ilgisiz değişiklikler yığılmaz.
- Test edilmemiş ana branch doğrudan canlıya gönderilmez.
- Rollback noktası olmadan riskli yayın yapılmaz.
- WordPress veritabanı/içerik değişiklikleri Git ile otomatik geri alınmış kabul edilmez.
- Özel yazılım migration'ları geri dönüş planı olmadan canlıya uygulanmaz.
- Binary, cache, log ve gereksiz generated dosyalar `.gitignore` ile dışarıda tutulur.

## Yayın Sonrası Kontrol
- Ana sayfa ve kritik URL'ler
- Form/oturum/ödeme gibi kritik akışlar
- Asset yüklemeleri
- Uygulama hata logları
- Doğru sürümün yayında olduğu

## Tamamlanma Kriteri
Yayındaki sürüm GitHub'da açıkça tanımlanabiliyor, aynı sürüm yeniden üretilebiliyor ve gerektiğinde son stabil sürüme güvenli dönüş yolu mevcutsa tamamlanmıştır.
