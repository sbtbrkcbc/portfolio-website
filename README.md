# Sabit Burak Cebeci - International SEO Portfolio

Professional portfolio website for Senior Process Safety Consultant specializing in SEVESO and ATEX compliance.

## 🌍 Live URLs (After Deployment)

- **Ireland (English):** https://sabitcebeci.com/en-ie/
- **Italy (Italian):** https://sabitcebeci.com/it-it/
- **Europe (English):** https://sabitcebeci.com/en/

## 🚀 Quick Start

### Development

```bash
# Frontend
cd /app/frontend
yarn start  # Runs on http://localhost:3000

# Backend (managed by supervisor)
sudo supervisorctl status
sudo supervisorctl restart backend
```

### Access Application
- Frontend: http://localhost:3000 (auto-redirects to /en-ie)
- Backend API: Check `REACT_APP_BACKEND_URL` in frontend/.env

## 📁 Project Structure

```
/app/
├── frontend/
│   ├── public/
│   │   ├── sitemap.xml          # SEO sitemap with hreflang
│   │   └── robots.txt           # Search engine directives
│   ├── src/
│   │   ├── locales/             # Locale-specific content
│   │   │   ├── en-ie.js         # Ireland (English)
│   │   │   └── it-it.js         # Italy (Italian)
│   │   ├── pages/               # Page components
│   │   ├── components/
│   │   │   ├── SEO/             # SEO components
│   │   │   │   ├── SEOHead.jsx  # Meta tags, hreflang
│   │   │   │   └── schemas.js   # JSON-LD schemas
│   │   │   └── Locale/          # Locale-aware components
│   │   ├── context/
│   │   │   └── LocaleContext.js # Locale management
│   │   └── App.js               # Main app with routing
│   └── package.json
├── backend/
│   ├── server.py                # FastAPI server
│   ├── routes/
│   │   ├── contact.py           # Contact form API
│   │   └── cv.py                # CV download API
│   ├── models/
│   │   └── contact.py           # MongoDB models
│   ├── static/cv/               # CV PDFs
│   └── requirements.txt
├── contracts.md                 # API contracts
├── SEO_ARCHITECTURE.md          # Complete SEO plan
└── DEPLOYMENT_GUIDE.md          # Deployment checklist
```

## 🎯 Features

### International SEO
- ✅ Locale-based URL structure
- ✅ Hreflang implementation
- ✅ JSON-LD Schema markup
- ✅ Sitemap with hreflang
- ✅ Unique meta tags per page

### Pages (30+ pages, 2 languages)
- Homepage, About, Services (4 detail), Industries (2 detail), Certifications, Contact

### Technical
- React 19 + React Router
- FastAPI backend
- MongoDB database
- Responsive design

## 🔑 Environment Variables

Frontend: `REACT_APP_BACKEND_URL`, `REACT_APP_SITE_URL`  
Backend: `MONGO_URL`, `DB_NAME`

## 📊 SEO Targets

**Ireland:** SEVESO consultant Ireland, ATEX compliance Dublin  
**Italy:** Consulente SEVESO Italia, Conformità ATEX Italia

## 🚨 Important Notes

- Independent consultant positioning (not corporate)
- No location restrictions
- No auto-redirects based on IP/language
- Safe for current employment

---

**Status:** ✅ Production Ready  
**Version:** 1.0.0
