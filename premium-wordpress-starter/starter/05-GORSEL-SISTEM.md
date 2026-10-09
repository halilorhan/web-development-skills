# 05 — Görsel Üretim, Medya ve Yerleştirme

> **Bağlayıcı önkoşullar:** `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md` ve `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`. Bu iki standart diğer rehberlerin tamamından önce uygulanır. Proje özelindeki onaylı tasarım kilidi ve güvenlik kuralları korunur.
> **Kaynak:** ASGE `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`; `halilorhan/web-development-skills` master 01, 02, 03A, 04, 05, 06, 07. ASGE'ye özel metinler, ID'ler ve sayısal değerler yeni müşteriye taşınmaz.

## Amaç
Her markaya özel tutarlı fotoğraf/illüstrasyon dili kur; sahte montaj, uygunsuz crop ve gereksiz büyük medya olmadan yüksek kalite sağla.

## Üretim brifi — zorunlu alanlar
- Sayfa/bölüm ve hedef mesaj; görsel neyi anlatıyor?
- Format ve yerleşim: desktop hero, yan görsel, portre, ekip kartı, favicon vb.
- Kesin aspect ratio ve kırpılmadan korunacak nesne/yüz/logo güvenli alanı.
- Marka estetiği, ışık, kamera perspektifi, malzeme doğruluğu, görsel gerçeklik ve ton.
- İnsan kullanımı izni; gerçek kişilerin yüzleri/kimliği değişmemeli.
- Metin/logonun görsele gömülüp gömülmeyeceği ve doğrulanmış marka varlıkları.
- Çıkış dosya adı, alternatif metin, gerçek kullanım hedefi.

## ASGE'den alınan uygulama dersleri
- Premium hero için şirketin gerçek hizmetini temsil eden net bir kompozisyon; rastgele stok fotoğrafı değil.
- Müşteri insansız görsel istediğinde insan eklenmez; çerçeve içindeki kompozisyon isteniyorsa ortamın tamamı yeniden üretilir, kaba crop ile ikame edilmez.
- Ekip portreleri aynı çekim dünyasına ait görünmeli: ışık, ölçek, perspektif ve fon eşleştirilmeli. Yüz ve kimlik korunmalı; kişiyi arka plana yapıştırılmış gibi gösterme.
- Dosya adları ve kişi/titr eşlemesi kayıtlı olmalı; markanın onaylı logosu oran değiştirilmeden kullanılmalı.
Bu dersler ASGE'ye özgü görsellerin başka markalara otomatik aktarılabileceği anlamına gelmez.

## Üretim ve dosya akışı
1. Onaylı brief'ten üret; ilk pilot görselde kompozisyon/gerçekçilik onayı al.
2. Görseli hedef canvas'ta üret; rastgele küçültüp büyütme.
3. Perspektif, eller/yüzler, yazı/logo, ışık, keskinlik ve üretim artefaktlarını incele.
4. Gerekli boyutlarda optimize et; modern formatlar destek ve kalite korunuyorsa kullan.
5. Dosya adını semantik ve benzersiz yap; alt metin dekoratif/işlevsel niteliğe göre belirle.
6. WordPress medya kütüphanesinde doğru öğeye bağla, tablet/mobil crop ve image loading'i kontrol et.
7. Var olan görselin yalnız hizası/ölçüsü değişecekse medya dosyasını gereksiz yere yeniden üretme veya re-encode etme.

## Önemli sınırlar
Müşteri vermediği referans logo, insan fotoğrafı, ödül, sertifika, bina veya başarı görseli uydurulmaz. Gizli veri ve kişisel görseller güvenli şekilde işlenir. Görsel dosyasını değiştirirken Elementor tam sayfa overwrite uygulanmaz.

## Kabul
Tüm görseller görevini anlatıyor, doğru yere doğru ölçüde yerleşiyor, responsive kırılmıyor, marka tutarlılığını bozmazken performansı makul tutuyor.
