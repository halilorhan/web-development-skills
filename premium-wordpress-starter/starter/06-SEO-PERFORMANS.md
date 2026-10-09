# 06 — SEO, İçerik Kalitesi ve Performans

> **Bağlayıcı önkoşullar:** `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md` ve `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`. Bu iki standart diğer rehberlerin tamamından önce uygulanır. Proje özelindeki onaylı tasarım kilidi ve güvenlik kuralları korunur.
> **Kaynak:** ASGE `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`; `halilorhan/web-development-skills` master 01, 02, 03A, 04, 05, 06, 07. ASGE'ye özel metinler, ID'ler ve sayısal değerler yeni müşteriye taşınmaz.

## SEO koruma prensibi
ASGE'de eski sitenin tasarımı değiştirildi; yaklaşık dört yıllık indeksli URL geçmişinin korunması ise ayrı zorunlu proje hedefiydi. Yeni projede de önce mevcut URL envanteri çıkarılır; SEO tasarımdan sonra akla gelen görev değildir.

## Zorunlu migrasyon tablosu
En az şu sütunlar: `old_url,new_url,old_status,target_status,action,redirect_301_required,seo_verified,notes`.
- İndeksli/değerli mevcut URL: öncelikle aynı slug, aynı arama niyeti.
- Değişim zorunluysa en yakın gerçek eşdeğere doğrudan 301; anasayfaya toplu yönlendirme yok.
- 404: tarihçe ve uygun içerik karşılığı araştırılmadan silinip bırakılmaz.
- 301 zinciri/döngüsü, 404 ve canonical çakışması test edilir.
- Search Console, sitemap, robots, index/noindex ve internal linkler yayında tekrar okunur.

## Sayfa bazlı SEO
1. Başlık hiyerarşisi H1/H2/H3 kullanıcı niyetine göre.
2. Tekil title ve meta description; benzer sayfalarda otomatik tekrar yok.
3. Canonical gerçekten indekslenecek hedef URL'ye işaret eder.
4. Yanlışlıkla staging noindex'in production'a taşınmasına veya staging'in indekslenmesine izin verme.
5. FAQ/Article/Organization/LocalBusiness gibi yapılandırılmış veri yalnız içerik gerçekten uygunsa.
6. Erişilebilir resim alt metni, anlamlı link metni, özgün doğrulanmış içerik.

## Performans
- LCP için üst kat görünür hero görselinin format ve preload/lazy davranışını bilinçli yönet.
- CLS için medya boyutları ve dinamik alanların yerini sabitle.
- INP için gereksiz JS, büyük animation bundle ve ağır üçüncü taraf yüklerini azalt.
- Elementor CSS ve cache kontrolünü hedefli uygula; işlevi bozacak optimizasyonu körlemesine açma.
- Mobilde font boyutu, görsel yerleşimi, menü etkileşimi ve form kullanılabilirliğini gerçek cihaz genişliklerinde incele.
- Core Web Vitals ölçümleri ve gerçek hız sonuçları ölçüm alınmadan “başarılı” olarak raporlanmaz.

## ASGE'ye özgü dikkat
Dinamik hibe/teşvik sayfaları, programların tarih ve limitleri gibi sürekli değişen veriler içerir. Program sayfası başlığı, index durumu ve resmî kaynak verisi programın gerçek kayıtlarına göre doğrulanır; bu örnek, diğer siteler için genel “dinamik veri güncelliği” dersidir.

## Kabul
Önemli eski URL'ler çalışıyor veya doğru 301 alıyor; sitemap ve canonical gerçek alan adında; staging indeks dışı; production kritik sayfaları bilinçli index ayarlı; sayfalar mobil kullanılabilir ve performans ölçümleri raporlu.
