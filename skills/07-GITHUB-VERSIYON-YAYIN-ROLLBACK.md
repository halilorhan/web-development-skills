# 07 — GitHub, Versiyon, Yayın ve Rollback

**Sürüm:** 1.4  
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

**İlgili dosyayı aç → minimum patch uygula → commit/push → mevcut deploy'u tetikle/çalışmasını kontrol et → yalnız etkilenen alanı smoke test et.**

Bu tür değişikliklerde, değişiklik gerektirmiyorsa:
- tüm repo yeniden taranmaz,
- ilgisiz asset'ler işlenmez,
- görseller yeniden encode edilmez,
- AVIF/WebP/Base64 üretimi yapılmaz,
- workflow dosyaları yeniden analiz edilmez,
- gereksiz PR/branch/tag/release zinciri oluşturulmaz,
- tüm site testleri tekrar çalıştırılmaz,
- aynı CI durumu gereksiz aralıklarla tekrar tekrar sorgulanmaz.

Görselin yalnız yerleşimi, boyutu veya konumu değişiyorsa **görsel dosyasının kendisine dokunma**. Binary/Base64 işlemi yalnız gerçek görsel dosyasının değiştirilmesi zorunluysa kullanılır.

## CI / Deploy Polling Sınırı
- Aynı workflow/deploy durumu değişmeden art arda en fazla **2 kez** kontrol edilir.
- `sleep`, bekleme süresi simülasyonu veya yalnız zaman geçirmek için araç çağrısı yapılmaz.
- İkinci kontrolde hâlâ aynı durum varsa yeni polling döngüsü başlatma; mevcut gerçek durumu raporla ve yalnız anlamlı başka bir işlem varsa devam et.
- Aynı job/step iki kez aynı şekilde başarısız olursa aynı komutu tekrar etme; log/kök neden incelemesine geç veya alternatif yöntem kullan.
- Küçük işte CI hatasının sebebi ilgisiz bir asset/workflow problemi ise önce bunun gerçekten yapılan değişiklikten kaynaklanıp kaynaklanmadığını doğrula; kanıt olmadan hero görseli, AVIF, Base64 veya workflow zincirini yeniden üretme.
- Sonucu belirsiz bir write/merge/deploy işleminde tekrar denemeden önce repo/PR/workflow durumunu oku.

## Hızlı Yol Koruma Eşiği
Küçük/lokal bir istek sırasında aşağıdakilerden biri oluşursa ağır işleme otomatik geçme; önce kapsamı yeniden doğrula:
- beklenenden fazla dosya değişmesi,
- workflow dosyasına müdahale ihtiyacı,
- asset pipeline veya binary/Base64 parçalama ihtiyacı,
- aynı adımda ikinci başarısızlık,
- değişiklikle ilgisiz test hataları.

Hedef: **minimum dosya → minimum commit → mevcut deploy → minimum smoke test**.

## GitHub Erişim Sürekliliği ve Yetenek Keşfi
- “GitHub/repo/deploy erişimim yok” demeden önce GitHub connector/tool fonksiyonlarını gerçekten keşfet ve ilgili repoyu metadata veya dosya okuma çağrısıyla doğrula.
- İlk bakışta görünen “aktif araç seti” GitHub yeteneklerinin tamamı olarak kabul edilmez. Connector keşfi yapılmadan “GitHub aracı yok” denmez.
- Repo okuma erişimi, repo yazma erişimi, branch/commit yetkisi, Actions yetkisi ve hosting deploy yetkisi birbirinden farklıdır; yalnız başarısız olan katmanı belirt.
- Aynı oturumda repo üzerinde commit, dosya değişikliği, workflow veya deploy başarıyla yapıldıysa sonraki istekte erişimi otomatik olarak yok sayma; önce aynı repo ve gerekli yetkiyi yeniden kontrol et.
- Kullanıcı repo/deploy erişiminin açık olduğunu belirtiyorsa, bunu gerçek araç çağrısıyla doğrula; doğrulamadan reddetme.
- Belirli bir GitHub fonksiyonunun ilk keşifte görünmemesi “GitHub erişimi yok” anlamına gelmez. İlgili eylem için uygun fonksiyonu yeniden keşfet veya mevcut alternatif GitHub işlemini kullan.
- Dosya değişikliği isteniyorsa mümkün olduğunda sıra: **repo doğrula → dosyayı fetch et → mevcut SHA'yı al → update/create işlemini yap → sonucu doğrula**.
- Bir GitHub çağrısı geçici hata verirse, sonucu belirsiz bir yazma işlemini körlemesine tekrarlama; önce repo durumunu okuyup işlemin gerçekleşip gerçekleşmediğini doğrula.
- GitHub ile yapılabilecek bir işlem mevcutken kullanıcıdan terminal/SSH komutu çalıştırmasını isteme.
- “GitHub/deploy aracı açıldığı anda yaparım” veya “bu konuşmada araç görünmüyor” diyerek işi erteleme. Önce connector keşfi ve gerçek doğrulama yap.
- Gerçek yetki engeli varsa genel mazeret verme: hangi repo, hangi işlem, hangi araç/fonksiyon denendi, hangi yetki eksik ve kullanıcının yapması gereken tek adım nedir açıkça belirt.

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
