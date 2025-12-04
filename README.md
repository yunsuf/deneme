# Sunum Kurulum ve Çalıştırma Rehberi

Bu proje, Quarto ve RevealJS kullanılarak hazırlanmış "Dijital Ouroboros" sunumunu içerir.

## Gereksinimler

- **Quarto**: [Quarto CLI](https://quarto.org/docs/get-started/) yüklü olmalıdır.
- **VS Code** (Önerilen): Quarto eklentisi ile birlikte.

## Sunumu Sıfırdan Oluşturma ve Çalıştırma

Sunum dosyası `presentation.qmd` (veya `@presentation.md` olarak referans verdiğiniz dosya) ana kaynak dosyasıdır.

### 1. Terminali Açın
Proje dizininde (`/Users/halis.yilboga/developer/ws/deneme`) bir terminal açın.

### 2. Önbelleği Temizleyin (Opsiyonel ama Önerilir)
Eğer daha önce build aldıysanız ve temiz bir başlangıç istiyorsanız:

```bash
rm -rf presentation_files presentation.html
```

### 3. Sunumu Derleyin ve Önizleyin
Aşağıdaki komut sunumu derler ve varsayılan tarayıcınızda açar. Dosyada değişiklik yaptığınızda otomatik olarak yenilenir.

```bash
quarto preview presentation.qmd
```

**Alternatif Port:**
Eğer port çakışması yaşarsanız:
```bash
quarto preview presentation.qmd --port 7415
```

## Sunumu Statik Olarak Oluşturma (HTML)

Sunumu bir dosya olarak paylaşmak veya internet olmadan çalıştırmak isterseniz:

```bash
quarto render presentation.qmd
```

Bu komut `presentation.html` dosyasını oluşturur. Bu dosyayı herhangi bir tarayıcıda açarak sunumu yapabilirsiniz.

## Sunum Kontrolleri

- **İleri/Geri:** Yön tuşları veya Space
- **Genel Bakış:** `Esc` tuşu (Tüm slaytları kuş bakışı görürsünüz)
- **Tam Ekran:** `F` tuşu
- **Sunucu Notları:** `S` tuşu

## Sorun Giderme

- **Görseller Görünmüyor:** `images/` klasörünün proje kök dizininde olduğundan emin olun.
- **Slaytlar Döngüye Giriyor:** `presentation.qmd` içindeki `loop: false` ayarını kontrol edin.
- **Stil Bozuk:** `cinematic.css` dosyasının mevcut olduğundan emin olun.
