---
marp: true
theme: gaia
class: lead
backgroundColor: #ffffff
color: #333
style: |
  section {
    font-family: 'Inter', sans-serif;
    font-size: 28px;
    padding: 40px;
    background-image: linear-gradient(to bottom right, #ffffff, #f0f4f8);
  }
  h1 { color: #2c3e50; font-size: 2.2em; margin-bottom: 0.2em; }
  h2 { color: #34495e; font-size: 1.5em; margin-top: 0; }
  h3 { color: #e67e22; font-size: 1.2em; }
  code { background: #eee; color: #d35400; font-family: 'Fira Code', monospace; }
  pre { background: #2d3436; color: #dfe6e9; font-size: 0.7em; padding: 15px; border-radius: 8px; box-shadow: 0 10px 20px rgba(0,0,0,0.15); }
  .mermaid svg { max-height: 400px; }
  .box {
    background: #fff;
    border-left: 6px solid #3498db;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    margin-top: 20px;
  }
  .center { text-align: center; }
  .columns { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
  .small { font-size: 0.8em; color: #7f8c8d; }
  a { color: #2980b9; text-decoration: none; border-bottom: 2px solid #3498db; }
---

<!-- _class: center -->
# Tarih Tekerrürden İbarettir
## JSF'ten Modern Mimariye Yolculuk

### 🕰️ "Sunucudan Ayrılış ve Eve Dönüş"

🔗 [Kapsamlı Teknik Rehber İçin Tıklayın](./JSF_to_Modern_Architecture_Complete_Guide.md)

---

# Büyük Resim: Mimari Sarkaç 🕰️

Yazılım dünyası bir sarkaçtır. Şu an "Sunucuya Dönüş" (Server-Side Renaissance) çağını yaşıyoruz.

1.  **2000-2010:** Sunucu Odaklı (JSF, ASP.NET)
    *   *Mantık sunucuda, HTML gönderilir.*
2.  **2010-2023:** İstemci Odaklı (SPA, React)
    *   *Mantık tarayıcıda, JSON gönderilir.*
3.  **2024+:** Modern Sentez (Next.js, RSC)
    *   *Mantık sunucuda (tekrar), ama akıllı.*

🔗 [Detaylı Sarkaç Analizi](./JSF_to_Modern_Architecture_Complete_Guide.md#1-büyük-resim-mimari-sarkaç-the-pendulum)

---

# Component Ağacı: Evden Uzakta Bir Gezi 🌳

UI Component'leri (Buton, Input) nerede yaşıyor?

<div class="columns">
<div>

### JSF
**Ağaç Sunucuda (Heap)**
`UIViewRoot`
*   ✅ Güvenli, DB'ye yakın.
*   ❌ Sunucu belleğini yer (Session).

</div>
<div>

### React SPA
**Ağaç Tarayıcıda (RAM)**
`Virtual DOM`
*   ✅ Sunucu rahat (Stateless).
*   ❌ Client yavaş, Loading spinner.

</div>
</div>

### Modern Çözüm (RSC)
**Ağacın gövdesi sunucuya döndü, yapraklar (interactivity) tarayıcıda kaldı.**

🔗 [Component Ağacı Detayları](./JSF_to_Modern_Architecture_Complete_Guide.md#2-component-ağacı-evden-uzakta-bir-gezi)

---

# Kod Arkeolojisi: İsimler Değişir... 🏛️

Tarih 2006. JSF ile kod yazıyoruz.

```java
// UserBean.java (2006)
public void saveUser() {
    // 1. Hafızadan al
    User user = new User(this.username);
    // 2. Veritabanına yaz
    userDao.save(user); 
}
// Tetikleyici: <h:commandButton action="#{userBean.saveUser}" />
```

Bakalım 20 yıl sonra ne değişmiş? 👇

---

# ...Desenler Kalır (2026) 🔮

Tarih 2026. Next.js Server Actions.

```typescript
// actions.ts (2026)
'use server'
export async function saveUser(formData: FormData) {
    // 1. Formdan al
    const username = formData.get('username');
    // 2. Veritabanına yaz
    await db.user.create({ data: { username } });
}
// Tetikleyici: <form action={saveUser} />
```

### Şok Edici Benzerlik
REST API yok. JSON yok. Sadece **Fonksiyon Çağrısı** var.
JSF haklıydı, sadece teknolojisi eskiydi.

🔗 [Kod Karşılaştırması](./JSF_to_Modern_Architecture_Complete_Guide.md#3-kod-arkeolojisi-isimler-değişir-desenler-kalır)

---

# Gizli Kahraman: State Yönetimi 🧠

**JSF:** `ViewState` (Hidden Input)
**Next.js:** `Closure Encryption` (Hidden Input)

İkisi de aynı şeyi yapar:
**Stateless olan HTTP üzerinde, Stateful bir deneyim simüle etmek.**

> "Modern mimari, 'Stateless' dogmasından vazgeçip 'Akıllı State' kavramına geçti."

🔗 [State Yönetimi Detayları](./JSF_to_Modern_Architecture_Complete_Guide.md#4-gizli-kahraman-state-yönetimi-viewstate-vs-closure)

---

# Dönüşüm Rehberi: Boğucu İncir 🌿

Eski JSF projesini nasıl modernleştireceğiz? Hepsini silip baştan mı yazalım? **ASLA.**

**Strateji: Strangler Fig (Boğucu İncir)**

1.  **Tohum:** JSF'in önüne Next.js Proxy koy.
2.  **Dallar:** Yeni özellikleri (Dashboard) Next.js ile yaz.
3.  **Çürütme:** Eski sayfaları (Login) zamanla taşı.
4.  **Sonuç:** JSF doğal yollarla sistemden atılır.

🔗 [Dönüşüm Stratejisi](./JSF_to_Modern_Architecture_Complete_Guide.md#6-dönüşüm-rehberi-strangler-fig-boğucu-incir)

---

<!-- _class: center -->
# Gelecek Vizyonu 🚀

Sarkaç durmayacak.
**WebAssembly** ve **Agentic Mesh** geliyor.

Ama prensip değişmeyecek:
**"Karmaşıklık yok olmaz, sadece yer değiştirir."**

### Teşekkürler!
Sorular?

🔗 [Tam Rehbere Git](./JSF_to_Modern_Architecture_Complete_Guide.md)

