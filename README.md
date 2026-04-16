# 🌍 Sabit Burak Cebeci - Professional Portfolio Website

## 📋 Proje Hakkında

7 dilli (EN, IT, TR, DE, FR, ES, SE) profesyonel portföy ve CV web sitesi.

**Teknoloji Stack:**
- **Frontend:** React (Vite), Tailwind CSS, Shadcn UI
- **Backend:** FastAPI (Python)
- **Database:** MongoDB
- **PDF Generation:** ReportLab (7 dil desteği)
- **i18n Routing:** Custom locale management

---

## 📁 Proje Yapısı

```
/app
├── backend/                  # FastAPI Backend
│   ├── routes/              # API endpoints
│   │   ├── cv.py           # CV download endpoints
│   │   └── contact.py      # Contact form endpoint
│   ├── models/             # Pydantic models
│   │   └── contact.py
│   ├── static/cv/          # Generated PDF files
│   ├── generate_cv.py      # 7-language CV generator
│   ├── server.py           # FastAPI main app
│   └── requirements.txt    # Python dependencies
│
├── frontend/               # React Frontend
│   ├── src/
│   │   ├── components/    # UI components
│   │   ├── pages/         # Page components
│   │   ├── locales/       # 7 language files
│   │   │   ├── en-ie.js   # English (Ireland)
│   │   │   ├── it-it.js   # Italian
│   │   │   ├── tr-tr.js   # Turkish
│   │   │   ├── de-de.js   # German
│   │   │   ├── fr-fr.js   # French
│   │   │   ├── es-es.js   # Spanish
│   │   │   └── se-se.js   # Swedish
│   │   ├── context/       # React Context (i18n)
│   │   └── layouts/       # Layout components
│   ├── public/
│   │   ├── sitemap.xml    # SEO sitemap (7 languages)
│   │   └── robots.txt
│   └── package.json
│
└── DEPLOYMENT_GUIDE.md    # Bu dosya
```

---

## 🚀 Hızlı Başlangıç (Localhost)

### 1️⃣ Backend Kurulumu

```bash
cd backend

# Python virtual environment oluştur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dependencies yükle
pip install -r requirements.txt

# .env dosyası oluştur
cp .env.example .env

# MongoDB bağlantısını düzenle
nano .env  # MONGO_URL ve DB_NAME ayarla

# Serveri başlat
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

**Backend:** http://localhost:8001

---

### 2️⃣ Frontend Kurulumu

```bash
cd frontend

# Dependencies yükle
yarn install

# .env dosyası oluştur
cp .env.example .env

# Backend URL'i ayarla
echo "REACT_APP_BACKEND_URL=http://localhost:8001" > .env

# Development server başlat
yarn start
```

**Frontend:** http://localhost:3000

---

## 🌐 Environment Variables

### Backend (.env)
```env
MONGO_URL=mongodb://localhost:27017/
DB_NAME=portfolio_db
CORS_ORIGINS=http://localhost:3000,https://yourdomain.com
```

### Frontend (.env)
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

---

## 📦 Production Deployment

### Seçenek 1: Vercel (Frontend) + Railway (Backend)

#### Frontend (Vercel):
1. https://vercel.com adresine git
2. GitHub repository'i import et
3. Build settings:
   ```
   Framework: Create React App
   Build Command: yarn build
   Output Directory: build
   ```
4. Environment Variables:
   ```
   REACT_APP_BACKEND_URL=https://your-backend.railway.app
   ```
5. Deploy!

#### Backend (Railway):
1. https://railway.app adresine git
2. "New Project" → "Deploy from GitHub"
3. Backend klasörünü seç
4. Environment Variables:
   ```
   MONGO_URL=mongodb+srv://...
   DB_NAME=portfolio_db
   CORS_ORIGINS=https://yourdomain.com
   ```
5. Deploy!

---

### Seçenek 2: Netlify (Frontend) + Render (Backend)

#### Frontend (Netlify):
```bash
cd frontend
yarn build
# Build klasörünü Netlify'a sürükle-bırak
```

#### Backend (Render):
1. https://render.com adresine git
2. "New Web Service"
3. Repository bağla
4. Settings:
   ```
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn server:app --host 0.0.0.0 --port $PORT
   ```

---

## 🔧 GoDaddy Domain Bağlantısı

### Vercel'e Domain Bağlama:
1. Vercel Dashboard → Settings → Domains
2. Domain adınızı ekleyin: `yourdomain.com`
3. GoDaddy DNS ayarlarına gidin:
   ```
   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   
   Type: A
   Name: @
   Value: 76.76.21.21
   ```
4. 10-15 dakika bekleyin

### Railway Backend için Subdomain:
```
api.yourdomain.com → Railway URL
```

---

## 📄 CV PDF Oluşturma

Tüm 7 dilde CV'ler otomatik oluşturulur:

```bash
cd backend
python generate_cv.py
```

Oluşturulan dosyalar: `backend/static/cv/`
- cv_en.pdf (English)
- cv_it.pdf (Italian)
- cv_tr.pdf (Turkish)
- cv_de.pdf (German)
- cv_fr.pdf (French)
- cv_es.pdf (Spanish)
- cv_se.pdf (Swedish)

---

## 🌍 Desteklenen Diller

| Dil | Locale | Route |
|-----|--------|-------|
| English | en-ie | `/en-ie` |
| Italian | it-it | `/it-it` |
| Turkish | tr-tr | `/tr-tr` |
| German | de-de | `/de-de` |
| French | fr-fr | `/fr-fr` |
| Spanish | es-es | `/es-es` |
| Swedish | se-se | `/se-se` |

**Varsayılan dil:** English (`/` → `/en-ie`)

---

## 🔍 SEO Özellikleri

- ✅ 7 dil için ayrı meta tags
- ✅ JSON-LD Schema (Organization, Person)
- ✅ Sitemap.xml (7 dil için URL'ler)
- ✅ Robots.txt
- ✅ Hreflang tags (çoklu dil SEO)
- ✅ ATS-friendly CV PDFs

---

## 🧪 Testing

```bash
# Backend API test
curl http://localhost:8001/api/cv/en

# Frontend test
http://localhost:3000/de-de
```

---

## 📞 İletişim & Destek

**Geliştirici:** Emergent AI Agent
**Proje Sahibi:** Sabit Burak Cebeci
**Email:** sabitburakcebeci@gmail.com
**LinkedIn:** linkedin.com/in/sbtbrkcbc

---

## 📝 Lisans

Bu proje Sabit Burak Cebeci'ye aittir.

---

**🎉 Başarılar! Portföy siteniz hazır!**

