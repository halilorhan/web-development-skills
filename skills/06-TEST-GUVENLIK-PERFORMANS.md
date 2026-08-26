# 06 — Test, Güvenlik ve Performans

**Sürüm:** 1.0  
**Kapsam:** Tüm web projeleri  
**Amaç:** Yayından önce fonksiyon, güvenlik, responsive ve performans hatalarını sistematik olarak yakalamak.

## Kontrol Sırası
1. Kritik kullanıcı akışlarını test et.
2. Form, buton, menü, link ve yönlendirmeleri kontrol et.
3. Masaüstü, tablet ve mobil görünümü kontrol et.
4. Yetkisiz erişim ve rol kontrollerini test et.
5. Input validation ve hata mesajlarını kontrol et.
6. HTTPS, cookie, güvenlik başlıkları ve hassas veri sızıntılarını kontrol et.
7. 404, 500 ve boş veri senaryolarını kontrol et.
8. Görsel boyutları, lazy load, cache ve gereksiz istekleri kontrol et.
9. Temel Core Web Vitals sorunlarını düzelt.
10. Son değişikliklerden sonra regresyon testi yap.

## Kurallar
- Hata kaynağı belirlenmeden rastgele düzeltme yapılmaz.
- Test amacıyla canlı veriye zarar verilmez.
- Güvenlik kontrolü yalnız eklenti/araç sonucuna bırakılmaz.
- Performans için çalışan özellik kaldırılmaz; önce gerçek darboğaz bulunur.
- Test başarısızsa yayın tamamlanmış sayılmaz.
- Kritik akışlarda yalnız “sayfa açılıyor” kontrolü yeterli değildir.

## Canlıya Çıkış Asgari Kabul Listesi
- Kritik sayfalar 200 cevap veriyor.
- Mobil ve masaüstünde taşma/kırılma yok.
- Formlar gerçek teslim noktasına ulaşıyor.
- Giriş/yetki kontrolleri doğru.
- Kırık link veya görünmeyen ana görsel yok.
- Console/server tarafında kritik hata yok.
- Temel SEO indexleme ayarları doğru.
- Backup/rollback noktası hazır.
- E-ticaret varsa 08 skill'indeki sipariş testleri geçmiş.

## Tamamlanma Kriteri
Kritik hata kalmamış, kabul listesi geçmiş ve son sürüm regresyon testinden başarıyla çıkmışsa tamamlanmıştır.
