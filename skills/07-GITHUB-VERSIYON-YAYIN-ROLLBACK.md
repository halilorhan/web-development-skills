# 07 — GitHub, Versiyon, Yayın ve Rollback

**Sürüm:** 1.2  
**Kapsam:** Tüm web projeleri  
**Amaç:** Tüm kod değişikliklerini GitHub üzerinden izlenebilir, geri alınabilir ve kontrollü biçimde canlıya taşımak.

## Temel İlke
GitHub kod için ana kayıt kaynağıdır. SSH erişimine bağımlı bir çalışma akışı kurulmaz.

## İş Akışı
1. Repo yapısını proje başında tanımla.
2. Üretim kodunu korunan ana branch'te tut.
3. Değişiklikleri ayrı commitlerle ve anlaşılır mesajlarla kaydet.
4. Değişiklik kapsamına uygun testleri çalıştır.
5. Büyük/riskli veya kilometre taşı sürümlerini gerektiğinde tag/release ile işaretle; küçük lokal değişikliklerde gereksiz tag/release üretme.
6. Projenin tanımlı GitHub → hosting yayın yöntemiyle deploy et.
7. Yayın sonrası değişiklik kapsamına uygun smoke test yap.
8. Sorun varsa son stabil sürüme rollback uygula.
9. Veritabanı değişikliği varsa kod ve veri sürüm uyumunu ayrıca kontrol et.

## Küçük Değişiklik Hızlı Yayın Yolu
Tek component, metin, görsel yerleşimi, spacing, CSS veya benzeri lokal değişikliklerde varsayılan akış:

**İlgili dosyayı aç → minimum patch uygula → commit/push → mevcut deploy'u tetikle/çalışmasını bekle → yalnız etkilenen alanı smoke test et.**

Bu tür değişikliklerde, değişiklik gerektirmiyorsa:
- tüm repo yeniden taranmaz,
- ilgisiz asset'ler işlenmez,
- görseller yeniden encode edilmez,
- AVIF/WebP/Base64 üretimi yapılmaz,
- workflow dosyaları yeniden analiz edilmez,
- gereksiz PR/branch/tag/release zinciri oluşturulmaz,
- tüm site testleri tekrar çalıştırılmaz,
- aynı CI durumu gereksiz aralıklarla tekrar tekrar sorgulanmaz.

Mevcut CI/CD pipeline otomatik olarak daha geniş test çalıştırıyorsa pipeline'ın tamamlanması beklenir; ancak asistan bunun yanında gereksiz ek kontrol zinciri oluşturmaz.

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
- Test edilmemiş ana branch doğrudan canlıya gönderilmez; test kapsamı değişiklik riskine göre belirlenir.
- Rollback noktası olmadan riskli yayın yapılmaz; küçük lokal ve kolay geri alınabilir değişikliklerde mevcut son stabil commit yeterli rollback noktası olabilir.
- WordPress veritabanı/içerik değişiklikleri Git ile otomatik geri alınmış kabul edilmez.
- Özel yazılım migration'ları geri dönüş planı olmadan canlıya uygulanmaz.
- Binary, cache, log ve gereksiz generated dosyalar `.gitignore` ile dışarıda tutulur.

## Yayın Sonrası Kontrol
Değişiklik kapsamına göre yalnız gerekli maddeleri kontrol et:
- Etkilenen sayfa/component
- Gerekliyse kritik URL
- Gerekliyse form/oturum/ödeme akışı
- Değişen asset'in doğru yüklenmesi
- Kritik hata oluşmadığı
- Doğru commit/sürümün yayında olduğu

## Tamamlanma Kriteri
Yayındaki değişiklik GitHub'da açıkça tanımlanabiliyor, gerekli smoke test geçmiş ve gerektiğinde son stabil sürüme güvenli dönüş yolu mevcutsa tamamlanmıştır.
