# 01 — Proje Analizi ve Mimari

**Sürüm:** 1.4  
**Kapsam:** Tüm web projeleri  
**Amaç:** Geliştirmeye başlamadan önce projenin ne yapılacağını, hangi teknolojiyle yapılacağını ve hangi sınırlar içinde kalacağını kesinleştirmek.

## Girdiler
- Müşteri briefi, mevcut site ve referanslar
- Marka/kurumsal kimlik dosyaları
- İstenen sayfalar, özellikler ve entegrasyonlar
- İçerik/ürün kaynakları
- Alan adı, hosting ve mevcut teknik durum
- Projenin WordPress mi özel yazılım mı olacağı

## Zorunlu Çıktılar
1. Proje amacı ve kapsamı
2. Kullanılacak teknoloji
3. Sayfa/menü/kategori haritası
4. Gerekli veri yapıları
5. Gerekli entegrasyonlar
6. Repo ve ortam yapısı
7. Uygulama sırası
8. Kapsam dışı işler ve kritik riskler

## İş Akışı
1. Kaynakları incele.
2. Eksik ama çalışmayı engellemeyen konularda güvenli varsayımı açıkça kaydet; kritik belirsizlik varsa geliştirmeyi o noktada kilitle.
3. WordPress veya özel yazılım yolunu seç.
4. Sayfa ve veri mimarisini çıkar.
5. Gerekli modül ve entegrasyonları belirle.
6. GitHub repo/branch yapısını tanımla.
7. Geliştirme sırasını bağımlılıklara göre oluştur.
8. Kararları proje ana dokümanına kaydet.

## İş Ölçeği ve Hızlı Yol
- Her istekte önce değişikliğin gerçek kapsamını belirle: küçük/lokal, orta veya yüksek riskli.
- Tek component, metin, görsel yerleşimi, spacing, stil veya benzeri lokal değişikliklerde **minimum müdahale** uygula.
- Küçük değişiklikte tüm repo taraması, ilgisiz dosya analizi, asset yeniden üretimi, format dönüşümü, Base64 işlemi, geniş regresyon veya uzun CI incelemesi yapma; yalnız değişiklik gerçekten bunları gerektiriyorsa yap.
- Değişiklik için gerekli dosya zaten biliniyorsa yeniden keşif/tarama yapma.
- Aynı doğrulamayı sonuç değiştirmeden tekrar tekrar yapma.
- Hız uğruna güvenliği atlama; ancak güvenlik adına değişiklik kapsamıyla ilgisiz işlem üretme.
- Amaç: **en küçük güvenli değişiklik → gerekli doğrulama → yayın → sonuç kontrolü**.

## Zaman Bütçesi ve Döngü Kesme
- Küçük/lokal bir işte ilerleme sağlamayan uzun analiz zinciri oluşturma.
- Aynı düşük seviyeli işlem en fazla **2 kez** başarısız denenebilir. İkinci başarısızlıktan sonra aynı yöntemi tekrar etme; hedef durumu oku, kök nedeni belirle ve farklı yöntem seç.
- Aynı CI/workflow durumu değişmeden art arda en fazla **2 kez** kontrol edilir. Daha fazla polling, bekleme simülasyonu veya yapay süre doldurma yapılmaz.
- `sleep`, “bekleme süresini simüle etme” veya yalnız zaman geçirmek için terminal/araç çağrısı kullanma.
- Küçük bir değişiklik beklenmedik biçimde asset pipeline, workflow düzenleme, çoklu binary/Base64 parçalama veya geniş repo değişikliği gerektiriyorsa **kapsamı yeniden değerlendir**; kanıt olmadan ağır yönteme geçme.
- Görselin kendisi değişmiyorsa görsel dosyasının byte içeriğine dokunma; yalnız yerleşim/kod/CSS değiştir.
- Bir araç çağrısı sonucu belirsizse aynı yazma işlemini tekrar etmeden önce hedef durumu oku.
- Uzayan işlemde amaç “bir şeyler yapmaya devam etmek” değil, en kısa güvenli yoldan sonucu üretmektir.

## Araç ve Erişim Doğrulama Protokolü
- Bir işlemi yapamayacağını söylemeden önce mevcut araç/connector durumunu gerçekten kontrol et.
- Ekranda veya ilk bakışta görünen araç listesini **nihai yetenek listesi olarak kabul etme**. İlgili servis in-scope/bağlıysa connector fonksiyonlarını keşfetmeden “araç yok” sonucuna varma.
- GitHub, dosya sistemi, deploy veya başka bağlı servis için önce ilgili connector/tool şemasını keşfet; ardından hedef repo/kaynak üzerinde gerçek bir okuma veya metadata çağrısı yap.
- Gerekli yazma işlemi için okuma erişimi ile yazma yetkisini ayrı doğrula. Bir fonksiyonun görünmemesi, servisin tamamına erişim olmadığı anlamına gelmez.
- Aynı oturumda servis/repo üzerinde başarılı işlem yapıldıysa sonraki istekte erişimin kaybolduğunu varsayma; önce yeniden doğrula.
- Kullanıcı “bu oturumda erişim açık” diyorsa bunu tek başına yeterli kanıt kabul etme ama **doğrudan reddetme de**; gerçek connector doğrulamasını yap.
- Tek bir çağrının başarısız olması tüm servise erişim olmadığı anlamına gelmez. Servis erişimi, repo erişimi, yazma yetkisi, Actions/deploy yetkisi ve belirli fonksiyon eksikliği ayrı ayrı değerlendirilir.
- Geçici veya belirsiz hata bir kez güvenli şekilde yeniden denenebilir. Yazma işleminin sonucu belirsizse tekrar yazmadan önce hedef durumu oku ve doğrula.
- Mevcut araçla yapılabilen işi kullanıcıya manuel komut veya işlem olarak devretme.
- “Araç açıldığında yaparım”, “şu an görünmüyor”, “bu oturumda yok” gibi cümleleri **connector keşfi ve gerçek doğrulama yapılmadan kullanma**.
- İşlem gerçekten mümkün değilse yalnız engellenen işlemi, yapılan doğrulamayı, doğrulanan nedeni ve kullanıcının yapması gereken tek zorunlu adımı bildir; genel “erişim yok” ifadesi kullanma.

## Kurallar
- Gereksiz özellik ekleme.
- Teknoloji seçimini alışkanlığa göre değil proje ihtiyacına göre yap.
- Tasarım kararı ile teknik kararı birbirine karıştırma.
- Aynı veri iki farklı yerde yönetilmesin.
- Gizli bilgiler repoya yazılmasın.
- Başlangıçta rollback ve veri kaybı riski düşünülmeden geliştirmeye geçilmesin.

## Tamamlanma Kriteri
Geliştirici; neyi, hangi sırayla, hangi teknolojiyle ve hangi veri yapısıyla yapacağını ek karar üretmeden anlayabiliyorsa bu skill tamamlanmıştır.
