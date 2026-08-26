# 08 — E-Ticaret

**Sürüm:** 1.0  
**Kapsam:** E-ticaret projeleri  
**Amaç:** Ürün verisinden ödeme ve sipariş sonrasına kadar ticari akışın doğru ve test edilebilir çalışmasını sağlamak.

## Girdiler
- Ürün/kategori yapısı
- SKU, fiyat, vergi, stok ve varyasyon kuralları
- Kargo/teslimat kuralları
- Ödeme yöntemleri
- İade/iptal ve sipariş durumları
- Müşteri hesap/üyelik gereksinimleri

## İş Akışı
1. Kategori ve ürün veri modelini kesinleştir.
2. SKU ve varyasyon kurallarını tanımla.
3. Fiyat, indirim, vergi ve stok davranışını kur.
4. Sepet kurallarını uygula.
5. Kargo/teslimat seçeneklerini uygula.
6. Ödeme entegrasyonunu 05 skill'i üzerinden bağla.
7. Sipariş durum akışını oluştur.
8. Müşteri ve yönetici bildirimlerini test et.
9. İptal/iade senaryolarını kontrol et.
10. Baştan sona test siparişi oluştur ve sonucu doğrula.

## Kurallar
- Ürün varyasyonu ile ayrı ürün kavramı karıştırılmaz.
- SKU benzersiz olmalıdır.
- Fiyat ve stok yalnız arayüz tarafında doğrulanmaz.
- Ödeme başarılı cevabı doğrulanmadan sipariş “ödendi” sayılmaz.
- Aynı ödeme bildirimi iki sipariş etkisi üretmemelidir.
- Stok azaltma/iade mantığı sipariş durumlarıyla tutarlı olmalıdır.
- Kargo ve vergi hesapları sepet toplamıyla tekrar doğrulanır.
- Sipariş verisi ödeme sağlayıcısına gereğinden fazla gönderilmez.
- Canlı ödeme açılmadan test/sandbox akışı tamamlanır.

## Asgari Test Senaryoları
- Tek ürün siparişi
- Varyasyonlu ürün siparişi
- Stokta olmayan ürün
- Başarısız ödeme
- Başarılı ödeme
- İndirim/kargo/vergi hesabı
- Sipariş iptali veya iadesi
- Müşteri ve yönetici bildirimi

## Tamamlanma Kriteri
Ürün → sepet → kargo → ödeme → sipariş → bildirim akışı gerçek senaryoda tutarlı çalışıyor ve başarısız ödeme/stok/iade durumları veri hatası üretmiyorsa tamamlanmıştır.
