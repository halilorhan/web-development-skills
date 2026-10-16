# 02 — Premium Görsel Tasarım ve UX Sistemi

> **Bağlayıcı önkoşullar:** `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md` ve `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`. Bu iki standart diğer rehberlerin tamamından önce uygulanır. Proje özelindeki onaylı tasarım kilidi ve güvenlik kuralları korunur.
> **Kaynak:** ASGE `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`; `halilorhan/web-development-skills` master 01, 02, 03A, 04, 05, 06, 07. ASGE'ye özel metinler, ID'ler ve sayısal değerler yeni müşteriye taşınmaz.

## Tasarım stratejisi
ASGE'de hedeflenen seviye, jenerik Elementor şablonunun ötesinde özgün, güven veren, dönüşüm odaklı kurumsal deneyimdi. ASGE'nin somut renklerini ve mesajlarını kopyalamak değil; sistematik kalite kararlarını transfer et.

## Tasarım başlangıç kapısı
- Marka kişiliği, rekabet referansları ve hedef kitlenin bilgi ihtiyacını belirle.
- Site haritası ve ana sayfa anlatı sırası onaylanmış olsun.
- Gerçek logo, tipografi, marka görselleri ve içerik kaynaklarını edin.
- Sayfa bazlı kullanılabilirlik ve dönüşüm hedeflerini ölçülebilir tarif et.

## Tasarım tokenları
| Alan | Karar standardı |
|---|---|
| Renk | Marka birincil/ikincil, yüzey, kenarlık, metin, durum renkleri; kontrast denetimi |
| Tipografi | Başlık ölçeği, gövde, ağırlık, satır yüksekliği, satır uzunluğu; tutarlı font yükleme |
| Layout | Desktop shell, max-width, grid, boşluk tokenları; breakpoint'e göre gerçek yeniden düzenleme |
| Bileşen | Hero, CTA, card, header, dropdown, footer, form, logo grid, istatistik, FAQ |
| Hareket | Amaçlı ve hafif animasyon; klavye kullanımı ve `prefers-reduced-motion` |
| Görsel | Tutarlı ışık, oran, yön, kurumsal kalite ve gerçek veriyle ilişki |

**ASGE referansı:** Uygulama kaydında 1440px shell, Inter tipografisi, koyu premium hero, ortak kart ve responsive 3/2/1 grid kararları vardır. Bunlar ASGE uygulama örnekleridir, bütün müşteriler için sabit değer değildir.

## Sayfa tasarımı sırası
1. Moodboard ve rekabet farkı: taklit yok.
2. Global tasarım tokenları ve iki-üç temel component varyantı.
3. Navigasyon/header ve footer, dropdown davranışları; mobile ayrı senaryo.
4. Ana sayfada **değer önerisi → hizmetler → güven kanıtı → dönüşüm** akışı; içerik sırası işe göre uyarlanır.
5. İç sayfalarda tutarlı hero, breadcrumb/bağlam, içerik blokları, ilgili aksiyon.
6. Tablet/mobil: hover'a bağımlı kritik bilgi bırakma; CTA erişilebilir; menü tıklaması ve kaydırma testleri.
7. Gerçek metinlerle kırılım, overflow, kontrast, odak, animasyon ve performans kabulü.

## Zorunlu pilot karşılaştırması ve kanıtı (K2)

**Ring Hamam dersi:** Kullanıcı tarafından reddedilen ilk sürümde metin ağırlıklı, genel geçer Elementor yerleşimi yayına çıktı; gerçek referans site, marka görselleri ve güçlü kompozisyon yeterince uygulanmadı. Sonradan onaylanan tasarımın kalite düzeyi `halilorhan/ring-hamam-spa` deposundaki **`tasarim-onayli-2026-10-16`** sürümünde kayıtlıdır. Bu bir *görsel işçilik kıstasıdır*, tüm müşteriler için kopyalanacak sabit CSS, renk veya logo değildir.

**Pilot kabul işlemi:**
1. Varsa kullanıcı referans sitesinin desktop/mobil görünümünü gerçekten aç ve somut tasarım özelliklerini not et: ilk ekranın görsel kompozisyonu, başlık hiyerarşisi, gerçek logo, menü, CTA, hizmet kartları, galeri ve sayfa derinliği. Referans erişilemediyse durumu `BLOCKED` olarak kaydet; incelemiş gibi anlatma.
2. İlk ana sayfayı gerçek/izinli varlıklarla hazırla. **Boş tema, geçici başlıklar, sahte görseller, tek renk bloklarından ibaret şablon** premium pilot diye sunulmaz.
3. Desktop (yaklaşık 1440 px) ve mobil (yaklaşık 390 px) gerçek render/screenshot veya eşdeğer görsel inceleme kanıtı edin; referansla yan yana değerlendirme sonucunu kaydet. Tablet görünümü K3'te ayrıca kontrol edilir. Bu çözünürlükler örnektir, zorunlu tek ölçü değildir.
4. Eksikleri öznel “oldu” ifadesiyle değil, düzeltilecek **somut bileşen farklarıyla** belirt (logo kalitesi, boşluk, kadraj, CTA, menü, kart sayısı, okunurluk). Hatalı alanı düzelt, aynı kanıtı gereksiz tekrarlama.
5. Pilot `PROJECT-QUALITY-GATE.json` içinde `PASS` durumuna **yalnız tasarım kanıtı ve gerçek kullanıcı onay referansı ile** geçer. Bu gerçekleşmeden toplu iç sayfa üretimi ve yayına geçme. Eksik onay kullanıcıdan bir kez, kısa biçimde istenir; verilmiş onayı yeniden isteme.

**Kabulde reddedilecek durumlar:** Referans analizinin yapılmış gibi gösterilmesi; teknik kaydetme/200 OK'un premium kalite delili sayılması; onaysız tasarımın canlıya alınması; onaylı bileşenlerin sebepsiz değiştirilmesi.

## Tasarım kilidi
Müşteri bir sayfa/alanı onayladıktan sonra global yeniden tasarıma girilmez. Revizyonun etkisini belirle ve sadece ilgili bileşeni değiştir. Yasağı ihlal eden tam sayfa Elementor overwrite kesinlikle kullanılmaz.

## Red kriterleri
Hazır tema hissi, düşük kontrast, hizasız grid, sahte başarı/istatistik, kırpılan yüz/logo, mobilde kapanmayan menü, geçersiz CTA, aşırı animasyon, placeholder medya.

## Kabul
Her sayfa birbiriyle ilişkili görünür ama marka bağlamına özgüdür; masaüstü, tablet ve mobilde bağımsız kontrol yapılmıştır.
