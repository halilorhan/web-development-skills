# ZORUNLU STANDART — Araç, Erişim ve Operasyon Önceliği

**Öncelik:** Bu belge yeni WordPress kurumsal site şablonlarına başlangıçta kopyalanacak yüksek öncelikli operasyon standardıdır. Projeye özel açık kararlar ve güvenlik/onay sınırları saklıdır.

## Kesin çalışma ilkesi

**Önce bağlı araçları kullan; bağlantı istemeyi son çareye bırak.** Kullanıcıya tekrar tekrar “GitHub’ı bağla”, “MCP’yi kur”, “SSH aç”, “sunucuya erişim ver”, “ekran görüntüsü gönder” demek varsayılan davranış olamaz. Önce somut araç keşfi ve en az bir gerçek, hedefe uygun erişim çağrısı yapılır. Araçların adının mevcut olması, yetkinin veya belirli hedefe erişimin kesin olduğu anlamına gelmez.

## Her yeni görevde zorunlu erişim sırası

1. **Mevcut konuşma ve proje kaydı:** Repo, site, staging/production, mevcut bağlantı, önceki engel, kullanıcı tarafından daha önce reddedilmiş yöntemler ve önceki sonuçlar belirlenir. Bilinen bilgi kullanıcıya tekrar sorulmaz.
2. **GitHub:** Kurulu GitHub bağlantısı keşfedilir; hedef repo bulunur, ilgili dosya/branch okuma ve görev gerektiriyorsa yazma yetkisi uygun gerçek çağrıyla sınanır. Repo yolu tahmin edilmez, kod/değişiklik kaydı repoda tutulur.
3. **WordPress MCP:** Bağlı MCP Server for WordPress, WPVibe veya mevcut eşdeğer WordPress araçları keşfedilir. Önce kayıtlı siteler ve *gerçek site URL’si* belirlenir. Staging bağlantısı, production erişimi gibi sunulmaz. Bir WordPress aracı yetersizse diğer uygun ve yetkili WordPress aracı araştırılır.
4. **Sunucu ve hosting:** Mevcut panel/hosting/bağlantı entegrasyonları keşfedilir; hedef uygulama, alan adı, dosya, veritabanı, yedek ve yayın yetenekleri doğrulanır. Panelin File Manager, Site Clone, backup, domain, SSL gibi araçları uygulanabilirse SSH zorunlu tutulmaz. Kullanıcının daha önce çalışmadığını belirttiği SSH yöntemi tekrar önerilmez.
5. **Alternatif yol:** Tek bir araç hatası bütün servisin erişilemez olduğu sonucunu doğurmaz. Aynı işi yapabilen yetkili farklı bağlantı, panel, uygulama veya kontrollü içe/dışa aktarma seçeneği denenir.
6. **Kullanıcıya yönlendirme ancak son çare:** Gerçekten kullanıcı etkileşimi zorunluysa nedeni ve gereken *tek* en kısa işlem söylenir. Gereksiz ekran görüntüsü, panel gezintisi veya aynı bağlantıyı yeniden yapma talebi yoktur.

## İhlal edilemeyecek davranış kuralları

- **Yasak:** Test etmeden “bağlantım yok”, “erişimim yok”, “yetkim yok”, “yapamam” demek.
- **Yasak:** Bağlı GitHub/WordPress/sunucu araçlarının yapabildiği işi kullanıcıya yüklemek.
- **Yasak:** Zaten bağlantılı bir servisi yeniden bağlatmak; staging ile production'ı karıştırmak.
- **Yasak:** Önceden başarısız olduğu bilinen SSH/terminal yöntemini alternatifleri sınamadan tekrar önermek.
- **Yasak:** Doğrulanmayan bir yazma/yayın işlemini yapılmış ilan etmek; belirsiz sonucu körlemesine tekrar çalıştırmak.
- **Yasak:** Gizli anahtar, token, parola veya veritabanı kimlik bilgilerini GitHub'a, sohbet örneklerine ya da günlük kayıtlarına koymak.
- **Zorunlu:** Hedef ve yetki sınırı, değişiklik öncesi mevcut durum, değişiklik sonrası okuma/doğrulama, hata ve geri alma yolu kayıt altına alınır.
- **Zorunlu:** Üretim ortamında silme, üzerine yazma, alan adı değiştirme, DNS, veritabanı migrasyonu gibi riskli işlemler öncesi doğru hedef ve kullanılabilir yedek teyidi alınır; kullanıcının açık onayı gereken yıkıcı işlemler izinsiz yapılmaz.
- **Zorunlu:** Önce staging/test ortamında çalışılır, görsel onaylı alanlar keyfî biçimde değiştirilmez, SEO/URL mirası korunur.
- **Zorunlu:** Bağlantının ömrü ve yetkileri araç sistemine bağlıdır; “her projede sürekli erişim garantisi” verilmez. Ama **her projede önce mevcut erişimi keşfetme/doğrulama yükümlülüğü** değişmez.

## Yeni proje başlangıç kontrolü (asistanın kendi içinde)

- [ ] Projenin GitHub deposu ve talimat dosyaları bulundu ve okundu.
- [ ] Mevcut GitHub erişimi gerçek çağrıyla doğrulandı.
- [ ] WordPress staging ve production bağlantıları *ayrı ayrı* kontrol edildi.
- [ ] Hosting/sunucu/panel araçları ve gerekirse alternatif yollar sınandı.
- [ ] Daha önce başarısız olmuş erişim yöntemleri ve kullanıcı tercihleri hesaba katıldı.
- [ ] Erişimin doğrulanamadığı alanlar spesifik ve dürüstçe kaydedildi.
- [ ] Yapılabilecek işlemler otomatik uygulandı, yalnız kaçınılmaz kullanıcı adımları istendi.
- [ ] Değişiklikler test edildi, kaynak kayıtları güncellendi.

## ASGE’den edinilen ders

ASGE'de GitHub deposu, staging WordPress MCP/WPVibe bağlantısı ve SpeedyPanel'in uygulama, alan adı, yedek ve dosya/veritabanı ekranları ayrı erişim katmanlarıdır. Terminal menüsünün bulunmaması otomatik olarak göçün yapılamayacağı anlamına gelmez. Bağlantı önerisi vermeden önce bağlanılan hedef ve mevcut panel özellikleri doğrulanmalı, kullanıcı aynı işlemleri tekrar tekrar yapmak zorunda bırakılmamalıdır.

**Gelecek kullanım:** Bu belge müşteri özelindeki ASGE içerikleri taşınmadan genel premium WordPress başlangıç reposuna aktarılacak ve proje başlangıç talimatından açıkça referanslanacaktır.
