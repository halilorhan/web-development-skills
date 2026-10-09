# 04 — Sayfa ve Bileşen Üretim Sistemi

> **Bağlayıcı önkoşullar:** `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md` ve `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`. Bu iki standart diğer rehberlerin tamamından önce uygulanır. Proje özelindeki onaylı tasarım kilidi ve güvenlik kuralları korunur.
> **Kaynak:** ASGE `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`; `halilorhan/web-development-skills` master 01, 02, 03A, 04, 05, 06, 07. ASGE'ye özel metinler, ID'ler ve sayısal değerler yeni müşteriye taşınmaz.

## Bir sayfa üretme kontrol akışı
1. Sayfa amacı, ziyaretçi niyeti, hedef eylem, SEO URL'si ve gerçek içeriği tespit et.
2. Varsa mevcut sayfanın **yayınlanan wrapper ID'sini, Elementor kaynak/template ID'sini** ve global bileşen bağımlılıklarını oku.
3. Tekrar kullanılabilir component seç: hero, başlık, medya/metin, değer kartı, kanıt, FAQ, form, CTA.
4. Yeni boş sayfaysa section/container/widget olarak modüler kur. Dev HTML widget'a tüm sayfayı gömmek standart yaklaşım değildir.
5. Mevcut sayfaysa yalnız **istenen component düzeyinde kısmi düzenleme** yap.
6. Alt metin, başlık semantiği, link, CTA, responsive ve erişilebilirliği tamamla.
7. Önce staging görüntüsü/kullanıcı akışı test et, sonra değişikliği GitHub/karar kaydına işle.

## Kesin yasak: full-page write
- Mevcut sayfa için tek HTML bloğu, tamamını değiştiren JSON/meta/write, `_elementor_data` toplu kaydı, tüm `post_content` overwrite **kullanılamaz**.
- “Sadece bir görsel değişecek” görevi sayfanın her bölümünü yeniden yazmak için gerekçe değildir.
- Güncellemeye başlamadan mevcut widget/section ID ve sürümünü doğrula.
- Sadece hedeflenen element/özellik üzerinde değişiklik yap; global header, footer, kardeş widget, responsive ayar ve anchor'ları koru.
- Öncesi/sonrası veri farkını hedefli doğrula; kontrolsüz yan etki varsa geri al.
- Kullanılan API yalnız tam sayfa overwrite sunuyorsa başka güvenli yöntem ara; bulunmazsa işlemi yapma.

## Bileşen sözleşmesi (her reusable block için)
- Amaç ve hangi sayfalarda kullanıldığı
- Girdi alanları, içerik kaynağı ve boş/hata davranışı
- Desktop/tablet/mobile layout ve breakpoint
- Semantik HTML, klavye erişimi, kontrast
- Birincil CTA ve hedef link
- Bağımlı JS/CSS, etki alanı, versiyon
- Test ve rollback yönergesi

## ASGE'den ders
ASGE'de içerik kaynakları ile yayımdaki wrapper'lar bazı yerlerde ayrı tutuldu; yanlış ID'ye yazmak görünürde değişiklik olmamasına veya başka sayfanın bozulmasına neden olabilir. Bir kaynak birçok sayfada kullanılıyorsa önce kullanım haritası çıkar. Header dropdown hizası ve boşluk sistemleri tüm siteyi etkileyebilir; scope edilmemiş CSS'den kaçın.

## Kontrol
Yalnız hedef bölüm değişmiş mi? Linkler, animasyonlar, shortcode'lar, responsive ve CTA'lar aynı çalışıyor mu? Bu iki sorunun yanıtı belgelenmeden iş bitmiş sayılmaz.
