# 07 — GitHub, Versiyon, Yayın ve Rollback

**Sürüm:** 1.1  
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

## GitHub Erişim Sürekliliği
- “GitHub/repo/deploy erişimim yok” demeden önce ilgili repoyu gerçek bir metadata veya dosya okuma çağrısıyla doğrula.
- Aynı oturumda repo üzerinde commit, dosya değişikliği, workflow veya deploy başarıyla yapıldıysa sonraki istekte erişimi otomatik olarak yok sayma; önce aynı repo ve gerekli yetkiyi yeniden kontrol et.
- Repo okuma erişimi, repo yazma erişimi, GitHub Actions yetkisi ve hosting deploy yetkisi birbirinden farklıdır. Yalnız başarısız olan katmanı belirt.
- Belirli bir GitHub fonksiyonunun araçta bulunmaması “GitHub erişimi yok” anlamına gelmez. Gerekirse uygun GitHub fonksiyonunu keşfet ve mevcut yeteneklerle devam et.
- Bir GitHub çağrısı geçici hata verirse, sonucu belirsiz bir yazma işlemini körlemesine tekrarlama; önce repo durumunu okuyup işlemin gerçekleşip gerçekleşmediğini doğrula.
- GitHub ile yapılabilecek bir işlem mevcutken kullanıcıdan terminal/SSH komutu çalıştırmasını isteme.
- Gerçek yetki engeli varsa genel mazeret verme: hangi repo, hangi işlem, hangi yetki/fonksiyon eksik ve kullanıcının yapması gereken tek adım nedir açıkça belirt.

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
