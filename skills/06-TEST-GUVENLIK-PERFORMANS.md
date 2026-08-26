# 06 — Test, Güvenlik ve Performans

**Sürüm:** 1.1  
**Kapsam:** Tüm web projeleri  
**Amaç:** Yayından önce fonksiyon, güvenlik, responsive ve performans hatalarını sistematik olarak yakalamak.

## Test Kapsamı Kuralı
Test seviyesi değişikliğin etkisine göre seçilir.

### Küçük / Lokal Değişiklik
Örnek: metin, spacing, tek görsel, tek component görünümü, küçük CSS düzeni.
- Yalnız etkilenen component/sayfayı kontrol et.
- Gerekliyse bir masaüstü ve bir mobil görünüm kontrolü yap.
- İlgili kritik fonksiyon etkileniyorsa yalnız o fonksiyonu smoke test et.
- Tüm site regresyonu, performans taraması veya güvenlik taraması çalıştırma; değişiklik bunları etkiliyorsa genişlet.

### Orta / Fonksiyonel Değişiklik
Örnek: form, navigasyon, template, dinamik veri veya birden çok sayfayı etkileyen component.
- Etkilenen akışı ve bağlı sayfaları test et.
- Responsive ve regresyon kapsamını etki alanına göre genişlet.

### Yüksek Riskli Değişiklik
Örnek: ödeme, üyelik, yetkilendirme, veritabanı, routing, permalink, deployment veya altyapı değişikliği.
- İlgili tüm kritik akışları ve regresyon senaryolarını çalıştır.
- Gerekli güvenlik, veri bütünlüğü ve rollback kontrollerini tamamla.

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
10. Son değişikliklerden sonra gerekli kapsamda regresyon testi yap.

## Kurallar
- Hata kaynağı belirlenmeden rastgele düzeltme yapılmaz.
- Test amacıyla canlı veriye zarar verilmez.
- Güvenlik kontrolü yalnız eklenti/araç sonucuna bırakılmaz.
- Performans için çalışan özellik kaldırılmaz; önce gerçek darboğaz bulunur.
- Test kapsamı değişiklikle orantılı olmalıdır; küçük değişiklik için gereksiz tam test zinciri çalıştırılmaz.
- Aynı test sonucu değişmeden tekrar tekrar kontrol edilmez.
- Gerekli test başarısızsa yayın tamamlanmış sayılmaz.
- Kritik akışlarda yalnız “sayfa açılıyor” kontrolü yeterli değildir.

## Canlıya Çıkış Asgari Kabul Listesi
Bu tam liste yeni sürüm/önemli yayınlarda uygulanır; lokal değişikliklerde yalnız etkilenen maddeler doğrulanır.

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
Değişikliğin risk düzeyine uygun gerekli testler geçmiş ve kritik hata kalmamışsa tamamlanmıştır.
