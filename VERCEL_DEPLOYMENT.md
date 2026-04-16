# 🚀 Vercel + Railway Deployment Rehberi

**ÜCRETSİZ** deployment için en iyi yöntem!

---

## 📋 İhtiyacınız Olanlar

1. ✅ GitHub hesabı
2. ✅ Vercel hesabı (ücretsiz)
3. ✅ Railway hesabı (ücretsiz)
4. ✅ MongoDB Atlas hesabı (ücretsiz)
5. ✅ GoDaddy domain

---

## 🗄️ Adım 1: MongoDB Atlas (Database)

### 1.1 Hesap Oluştur
1. https://www.mongodb.com/cloud/atlas adresine git
2. "Try Free" tıkla
3. Email ile kayıt ol

### 1.2 Cluster Oluştur
1. "Create a Deployment" → "FREE" seç (M0 Sandbox)
2. Provider: **AWS**
3. Region: **Frankfurt** (Avrupa'ya yakın)
4. Cluster Name: `portfolio-db`
5. "Create" tıkla

### 1.3 Database User Oluştur
1. "Database Access" → "Add New Database User"
2. Username: `portfolio_user`
3. Password: **GÜVENLİ BİR ŞİFRE** (kaydet!)
4. "Add User"

### 1.4 Network Access
1. "Network Access" → "Add IP Address"
2. "Allow Access from Anywhere" → `0.0.0.0/0`
3. "Confirm"

### 1.5 Connection String Al
1. "Database" → "Connect"
2. "Connect your application"
3. Connection string'i kopyala:
   ```
   mongodb+srv://portfolio_user:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
4. `<password>` yerine şifrenizi yazın

---

## 🔧 Adım 2: GitHub'a Kod Yükleme

### 2.1 GitHub Repository Oluştur
1. https://github.com/new adresine git
2. Repository name: `portfolio-website`
3. Public veya Private seç
4. "Create repository"

### 2.2 Kodları Yükle

**Yerel bilgisayarınızda:**

```bash
# İndirdiğiniz proje klasörüne git
cd /path/to/portfolio-website

# Git init
git init
git add .
git commit -m "Initial commit: 7-language portfolio website"

# GitHub'a push
git remote add origin https://github.com/KULLANICI_ADINIZ/portfolio-website.git
git branch -M main
git push -u origin main
```

---

## 🚂 Adım 3: Railway (Backend Deployment)

### 3.1 Railway Hesabı
1. https://railway.app adresine git
2. "Start a New Project" → "Deploy from GitHub repo"
3. GitHub hesabınızı bağlayın
4. `portfolio-website` repository'i seçin

### 3.2 Backend Service Oluştur
1. "Add Service" → "GitHub Repo"
2. Root Directory: `/backend`
3. Settings → Environment:
   ```
   MONGO_URL=mongodb+srv://portfolio_user:PASSWORD@cluster0.xxxxx.mongodb.net/
   DB_NAME=portfolio_db
   CORS_ORIGINS=https://yourdomain.com
   ```
4. Settings → Deploy:
   ```
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn server:app --host 0.0.0.0 --port $PORT
   ```

### 3.3 Backend URL'i Kopyala
1. Settings → Domains
2. "Generate Domain" tıkla
3. URL'i kopyala (örn: `portfolio-backend-production.up.railway.app`)

---

## ▲ Adım 4: Vercel (Frontend Deployment)

### 4.1 Vercel Hesabı
1. https://vercel.com adresine git
2. "Start Deploying" → GitHub ile giriş yap

### 4.2 Frontend Deploy
1. "Add New" → "Project"
2. GitHub'dan `portfolio-website` seç
3. **Root Directory:** `frontend` seç
4. Framework Preset: **Create React App**
5. Environment Variables:
   ```
   REACT_APP_BACKEND_URL=https://portfolio-backend-production.up.railway.app
   ```
6. "Deploy" tıkla

### 4.3 Deployment Bekle
- 2-3 dakika içinde deploy olur
- Vercel size bir URL verir: `portfolio-xxx.vercel.app`

---

## 🌐 Adım 5: GoDaddy Domain Bağlama

### 5.1 GoDaddy DNS Ayarları
1. GoDaddy → My Products → Domains
2. Domain'inizi seçin → "DNS" veya "Manage DNS"
3. **Tüm A Records ve CNAME'leri SİLİN**

### 5.2 Vercel Domain Ekleme
1. Vercel Dashboard → Settings → Domains
2. "Add" → `yourdomain.com` girin
3. Vercel size DNS ayarları verecek:
   ```
   Type: A
   Name: @
   Value: 76.76.21.21
   
   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```

### 5.3 GoDaddy'de DNS Kayıtları Ekle
Vercel'in verdiği kayıtları GoDaddy'e ekleyin:

| Type | Name | Value |
|------|------|-------|
| A | @ | 76.76.21.21 |
| CNAME | www | cname.vercel-dns.com |

### 5.4 Subdomain (Backend için - Opsiyonel)
```
Type: CNAME
Name: api
Value: portfolio-backend-production.up.railway.app
```

**Sonuç:** `api.yourdomain.com` → Railway backend

### 5.5 DNS Propagation (10-15 dakika)
- DNS değişiklikleri 10-15 dakika sürer
- https://www.whatsmydns.net/ ile kontrol edin

---

## ✅ Adım 6: Test & Doğrulama

### 6.1 Frontend Test
```
https://yourdomain.com
https://yourdomain.com/de-de
https://yourdomain.com/fr-fr
```

### 6.2 Backend Test
```bash
curl https://api.yourdomain.com/api/cv/en
```

### 6.3 CV İndirme Test
Her dilde "Download CV" butonuna tıklayın:
- EN: Sabit_Burak_Cebeci_CV_EN.pdf
- DE: Sabit_Burak_Cebeci_CV_DE.pdf
- vb.

---

## 🔄 Güncelleme Yapma

### Kod Değişikliklerini Deploy Etme:

```bash
# Değişiklik yap
git add .
git commit -m "Update: ..."
git push

# Vercel ve Railway OTOMATIK deploy eder! 🎉
```

---

## 💰 Maliyet Özeti

| Platform | Ücret | Limit |
|----------|-------|-------|
| **MongoDB Atlas** | ÜCRETSİZ | 512 MB |
| **Railway** | ÜCRETSİZ | $5 kredi/ay |
| **Vercel** | ÜCRETSİZ | 100 GB bandwidth |
| **GoDaddy Domain** | ~$10-15/yıl | - |

**Toplam Aylık Maliyet: $0** 🎉

---

## 🆘 Sorun Giderme

### Vercel Build Hatası
```bash
# package.json kontrol et
# REACT_APP_BACKEND_URL doğru mu?
```

### Railway Backend Hatası
```bash
# Logs kontrol et: Railway Dashboard → Deployments → Logs
# MONGO_URL bağlantısı doğru mu?
```

### DNS Çalışmıyor
- 24 saat bekle (maksimum propagation süresi)
- GoDaddy'de eski DNS kayıtlarını tamamen sil
- Vercel'de domain'i sil ve tekrar ekle

---

## 🎉 Tebrikler!

Artık 7 dilli portföy siteniz canlıda! 

**Sonraki adımlar:**
1. Google Analytics ekle
2. Search Console kurulum
3. LinkedIn/sosyal medyada paylaş
4. CV'nizi güncel tut

---

**⭐ Başarılar! Sabit Burak Cebeci**
