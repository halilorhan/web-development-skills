# 01 — Proje Analizi ve Mimari

**Sürüm:** 1.2  
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

## Araç ve Erişim Doğrulama Protokolü
- Bir işlemi yapamayacağını söylemeden önce mevcut araç/connector durumunu gerçekten kontrol et.
- İlgili servis bağlıysa önce uygun okuma, metadata veya güvenli doğrulama çağrısını yap; yalnız varsayıma dayanarak “erişimim yok” deme.
- Gerekli işlem görünmüyorsa ilgili connector içinde uygun fonksiyonu bir kez keşfet.
- Aynı oturumda servis/repo üzerinde başarılı işlem yapıldıysa sonraki istekte erişimin kaybolduğunu varsayma; önce yeniden doğrula.
- Tek bir çağrının başarısız olması tüm servise erişim olmadığı anlamına gelmez. Servis erişimi, repo erişimi, yazma yetkisi, Actions/deploy yetkisi ve belirli fonksiyon eksikliği ayrı ayrı değerlendirilir.
- Geçici veya belirsiz hata bir kez güvenli şekilde yeniden denenebilir. Yazma işleminin sonucu belirsizse tekrar yazmadan önce hedef durumu oku ve doğrula.
- Mevcut araçla yapılabilen işi kullanıcıya manuel komut veya işlem olarak devretme.
- İşlem gerçekten mümkün değilse yalnız engellenen işlemi, doğrulanan nedeni ve kullanıcının yapması gereken tek zorunlu adımı bildir; genel “erişim yok” ifadesi kullanma.

## Kurallar
- Gereksiz özellik ekleme.
- Teknoloji seçimini alışkanlığa göre değil proje ihtiyacına göre yap.
- Tasarım kararı ile teknik kararı birbirine karıştırma.
- Aynı veri iki farklı yerde yönetilmesin.
- Gizli bilgiler repoya yazılmasın.
- Başlangıçta rollback ve veri kaybı riski düşünülmeden geliştirmeye geçilmesin.

## Tamamlanma Kriteri
Geliştirici; neyi, hangi sırayla, hangi teknolojiyle ve hangi veri yapısıyla yapacağını ek karar üretmeden anlayabiliyorsa bu skill tamamlanmıştır.
