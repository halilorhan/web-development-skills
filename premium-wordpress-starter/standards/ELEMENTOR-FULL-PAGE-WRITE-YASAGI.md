# KATI KURAL — Elementor Full-Page Write Yasağı

**Durum:** Zorunlu, varsayılan olarak hiçbir istisnası olmayan güvenli düzenleme politikası.
**Kapsam:** Elementor Pro dahil tüm Elementor sayfaları, template'ler, header, footer, popup, loop item ve global bileşenler.

## Temel kural
**Mevcut bir Elementor sayfasının tamamını tek işlemle yeniden yazmak, bütün _elementor_data ağacını değiştirip kaydetmek, tam sayfa HTML/CSS/JS içeriğini topluca üstüne basmak (full-page write) KESİNLİKLE YASAKTIR.**
Bu yasak; MCP, WP-CLI, REST API, SQL, custom code, Elementor edit API ve başka herhangi bir araçla yapılan güncellemeler için aynıdır. Araç full-page write dışında güvenli yöntem sunmuyorsa o araçla yazma yapılmaz.

## Zorunlu çalışma akışı
1. İşlemden önce sayfanın gerçek Elementor kaynak ID'si, wrapper/template ilişkileri, revision bilgileri, hedef section/container/widget ve mevcut içerik doğrulanır.
2. Yalnız istenen section/container/widget veya ilgili alan üzerinde **noktasal güncelleme** yapılır; diğer element ID'leri, sibling node'lar, global stiller, header/footer, responsive ayarlar ve iç bağlantılar korunur.
3. Güncelleme işlemi olabildiğince Elementor'un kendi kontrollü düzenleme/kayıt API'si ya da widget/container seviyesinde güvenli kısmi düzenleme ile gerçekleştirilir. Belirsiz veya toplu JSON overwrite yöntemine geçilmez.
4. Her değişiklikten önce güncel revision/geri dönüş noktası ve mümkünse ilgili öğenin hedefli yedeği alınır. Değişiklik hemen ardından tekrar okunur; diff yalnız hedeflenen öğeyi göstermelidir.
5. Masaüstü/tablet/mobil görsel, JS/CSS, form, link ve responsive davranış kontrol edilir; gerekli Elementor CSS/cache yenilemeleri kontrollü yapılır.
6. Kısmi güvenli güncelleme teknik olarak mevcut değilse **işlem durdurulur**, hedef ve engel raporlanır; tüm sayfayı yazma yöntemine sessizce geçilmez.

## Özellikle yasak işlemler
- Değiştirilecek tek başlık/metin/görsel için sayfanın tüm widget ağacını yeniden oluşturmak.
- İçeriğe tek satırlık değişiklik için `_elementor_data` meta değerini bütünüyle güncellemek.
- Mevcut template/wrapper ID'lerini, global header/footer referanslarını veya element ID'lerini fark ettirmeden değiştirmek.
- Kaynak sayfanın tamamını tek HTML widget'ına ya da shortcode bloğuna dönüştürmek.
- Sayfa düzeyinde `post_content` değerini toptan değiştirmek; bunun bölüm bazlı düzenleme olduğunu iddia etmek.
- Bir araç yalnızca komple sayfa kaydı yapabiliyorsa sırf kolay diye onu kullanmak.

## Yeni sayfa oluşturma notu
Sıfırdan ve boş bir sayfanın ilk oluşturulması, mevcut sayfanın üzerine yazma değildir; fakat yeni sayfalar da mümkün olduğunca düzenlenebilir, ayrı section/container/widget bileşenlerinden oluşmalıdır. Yeni bir sayfayı tek dev HTML widget olarak kurmak tercih edilen mimari değildir.

## Kabul kriteri
**“Yalnız istenen alan mı değişti ve diğer her şey birebir korundu mu?”** sorusu okuma, diff ve görünüm testiyle kanıtlanamıyorsa değişiklik başarılı sayılmaz.

Bu politika yeni projelerin başlangıcından itibaren otomatik uygulanır. Diğer talimatlarda daha gevşek yazma önerileri bulunması bu yasağı kaldırmaz.
