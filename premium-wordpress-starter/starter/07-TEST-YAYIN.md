# 07 — Test, Staging, Yayın ve Rollback

> **Bağlayıcı önkoşullar:** `../standards/ERISIM-VE-ARAC-ONCELIK-KURALLARI.md` ve `../standards/ELEMENTOR-FULL-PAGE-WRITE-YASAGI.md`. Bu iki standart diğer rehberlerin tamamından önce uygulanır. Proje özelindeki onaylı tasarım kilidi ve güvenlik kuralları korunur.
> **Kaynak:** ASGE `PROJECT-INSTRUCTIONS.md`, `DECISIONS.md`, `IMPLEMENTATION-STATE.md`, `SITE-MAP.md`, `URL-MIGRATION-MAP.csv`; `halilorhan/web-development-skills` master 01, 02, 03A, 04, 05, 06, 07. ASGE'ye özel metinler, ID'ler ve sayısal değerler yeni müşteriye taşınmaz.

## Kural
**Canlı yayın değişikliği, veri/uygulama hedefi doğrulanmadan ve kullanılabilir yedek alınmadan yapılmaz.** SSH zorunluluğu yaratılmaz; gerçek hosting/panel özellikleriyle mümkün en güvenli yol kullanılır.

## Yayın öncesi
1. Bağlı GitHub, Orange tarafından geliştirilen MCP Server for WordPress ve sunucu/panel araçlarını ayrı doğrula. Staging bağlantısı production erişimi değildir.
2. Staging ve production uygulama adları, domainleri, document root, DB adları/prefixleri ve ortam sınırlarını kaydet.
3. Canlıya dokunmadan önce production **dosya + veritabanı** yedeğinin doğru uygulamaya ait, indirilebilir ve geri yüklenebilir olduğunu doğrula. Staging kaynak yedeğini de al.
4. SEO migrasyon tablosu ve bütün önemli URL'ler, form/SMTP, SSL ve üçüncü taraf entegrasyon listesi hazır olsun.
5. Müşteri onaylı tasarım ve kullanıcı akışları staging'de doğrulansın.
6. Riskli silme, DB overwrite, domain ve DNS işlemleri için açık kullanıcı onayı gerekiyorsa al; salt alan adı ekleme ile DB içindeki WordPress URL dönüşümünü birbirine karıştırma.

## Premium pilot ve production yayın kapısı (K2 → K4)

- Yeni siteyi önce **staging veya erişimi kontrollü, indeks dışı önizleme** ortamında oluştur. Gerçek staging yoksa üretim ortamına onaysız tam site yayını yapma; güvenli draft/önizleme kullan.
- Önce **tek ana sayfa pilotu** görsel kanıt ve kullanıcı tasarım onayıyla kabul edilmeli; sonra diğer sayfalar ve global bileşenler genişletilir.
- `PROJECT-QUALITY-GATE.json` üzerinde K1/K2/K3/K4 `PASS`, gerçek kanıt ve açık yayın onayı yoksa **yeni sitenin production publish işlemi yasaktır**. `BLOCKED` veya `FAIL` olan kritik kapı yayın önünde durur.
- GitHub Actions ile deploy edilen gelecekteki müşteri projelerinde `templates/premium-quality-gate.yml` ve `templates/check_quality_gate.py` uyarlanarak zorunlu CI kontrolü kurulabilir. Gerçek kilit için GitHub branch protection/ruleset, gerekli check ve **production Environment reviewers** uygun planda, ilgili repo ayarlarında ayrıca etkinleştirilmeli; deployment workflow'u bu environment'ı kullanmalıdır.
- **Sınır:** Bu repo yalnızca standartları/örnek CI dosyalarını taşır. Orange MCP/WordPress panelinden doğrudan yapılan yayın GitHub Actions tarafından engellenmez. Bağlanmamış pipeline'a “teknik olarak kilitli” denmez. Bu yolda kullanıcı onayı olmadan doğrudan yayını tetiklememek asistanın zorunlu çalışma kuralıdır.

## WordPress migrasyonunda gerçek kontrol
- İlgili ortamda WordPress `home`/`siteurl`, HTTPS ve DB içeriğindeki domain referanslarını **hedef kopya üzerinde**, serialized-safe araçla ele al.
- Domain değişikliği sırasında Elementor verisi/JSON ve serialized metadata için uygun aracı ve istisna tablolarını belirle; staging'i kazara canlı URL'ye çevirmeden önce DB hedefini denetle.
- GUID, lisans/secret, OAuth kayıtları, SMTP/REST ayarları ve başka alan adını içeren bağlantılar kontrollü değerlendirilmeli; global kör replace yapılmaz.
- Permalink, Elementor CSS/cache, medya yolları, form/REST endpoint ve linkleri yeniden test et.
- Primary domain seçimi WordPress home/siteurl ve yönlendirmelerini tek başına garanti etmez.

## Test kapsamı
- **Küçük değişiklik:** yalnız hedef component ve etkilenen mobil görünüm.
- **Orta:** navigasyon, form veya ortak template kullanan ilgili sayfalar.
- **Büyük:** migration, altyapı, URL/DB değişimi; tüm kritik akışlar + 404/301/canonical + SSL + rollback.
- Formları test ederken gerçek müşteri kaydı/mesajı oluşturma etkisini kontrol et; gerçek ödeme/sipariş oluşturma.

## Yayımlama sırası
1. Backup ve rollback kabulü.
2. Çalışan yeni uygulamayı hedef domain üzerinde hazırla.
3. Domain/SSL/DNS/WordPress URL ve mümkünse geçişte düşük kesinti sırasını uygula.
4. Veritabanı ve medya bütünlüğünü test et.
5. Kritik kullanıcı akışı, bağlantılar, mobil/header/dropdown, hız ve SEO smoke/regresyonu tamamla.
6. Başarısızsa eski uygulama + DB + DNS dönüş yolunu işlet.
7. GitHub kaydını, test sonuçlarını, eksikleri ve yayın tarihini belgele.

## Yasaklar
Doğrulanmamış yedeğe güvenerek production silmek; farklı uygulamanın DB'sini yanlışlıkla silmek; yeni domaini bağlamakla sitenin tamamen taşındığını iddia etmek; Elementor tam sayfa overwrite; başarısız SSH yöntemini tekrar tekrar dayatmak.

## Kabul
Production doğru domain ve SSL ile servis veriyor; form, menü, sayfa, medya ve SEO yönlendirmeleri doğrulandı; geri dönüş yolu mevcut.
