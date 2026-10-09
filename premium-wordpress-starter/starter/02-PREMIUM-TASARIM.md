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

## Tasarım kilidi
Müşteri bir sayfa/alanı onayladıktan sonra global yeniden tasarıma girilmez. Revizyonun etkisini belirle ve sadece ilgili bileşeni değiştir. Yasağı ihlal eden tam sayfa Elementor overwrite kesinlikle kullanılmaz.

## Red kriterleri
Hazır tema hissi, düşük kontrast, hizasız grid, sahte başarı/istatistik, kırpılan yüz/logo, mobilde kapanmayan menü, geçersiz CTA, aşırı animasyon, placeholder medya.

## Kabul
Her sayfa birbiriyle ilişkili görünür ama marka bağlamına özgüdür; masaüstü, tablet ve mobilde bağımsız kontrol yapılmıştır.
