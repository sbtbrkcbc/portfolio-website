# International SEO Portfolio - Deployment Guide

## 🎯 Project Overview
Professional multilingual portfolio website for Sabit Burak Cebeci - Senior Process Safety Consultant specializing in SEVESO and ATEX compliance.

**Target Markets:** Ireland (Primary), Italy (Primary), Europe (General)

---

## ✅ Completed Features

### 1. International SEO Architecture
- ✅ Locale-based URL structure (`/en-ie/`, `/it-it/`)
- ✅ Hreflang tags implementation (en-IE, it-IT, en, x-default)
- ✅ Canonical URLs on all pages
- ✅ JSON-LD Schema markup (Organization, Person, Service)
- ✅ Sitemap.xml with hreflang relationships
- ✅ robots.txt for search engine guidance
- ✅ Unique meta tags per page per locale

### 2. Pages (Fully Localized)
- ✅ Homepage with hero, services preview, industries
- ✅ About page with professional summary
- ✅ Services overview page
- ✅ 4 Service detail pages (SEVESO, ATEX, Explosion Protection, PSM)
- ✅ Industries overview page
- ✅ 2 Industry detail pages (Pharmaceutical, Chemical)
- ✅ Certifications page
- ✅ Contact page with working backend integration

### 3. Technical Implementation
- ✅ React Router with locale parameter
- ✅ SEO Head component with react-helmet-async
- ✅ Locale context for translations
- ✅ Language switcher with country flags
- ✅ Responsive design (mobile-first)
- ✅ Professional navy blue color scheme
- ✅ No location-specific restrictions
- ✅ Independent consultant positioning (not corporate)

### 4. Backend Integration
- ✅ Contact form saves to MongoDB
- ✅ CV download (3 languages: EN, IT, TR)
- ✅ API endpoints: `/api/contact`, `/api/cv/download`

---

## 🚀 Deployment Checklist

### Pre-Deployment

- [ ] **Environment Variables**
  ```bash
  # Frontend .env
  REACT_APP_BACKEND_URL=https://your-backend-domain.com
  REACT_APP_SITE_URL=https://sabitcebeci.com
  
  # Backend .env (already configured)
  MONGO_URL=mongodb://localhost:27017
  DB_NAME=portfolio
  ```

- [ ] **Update Sitemap URLs**
  - Replace `https://sabitcebeci.com` with your actual domain in `/app/frontend/public/sitemap.xml`

- [ ] **Test All Forms**
  - Contact form submission
  - CV downloads in all languages
  - Language switching

- [ ] **Check All Links**
  - Internal navigation
  - Service detail pages
  - Industry detail pages
  - Language switching maintains context

### Domain & DNS Setup

- [ ] **Purchase Domain** (if not already)
  - Recommended: `sabitcebeci.com` or `sabitcebeci.eu`

- [ ] **Configure DNS**
  - Point domain to your hosting server
  - Set up SSL certificate (Let's Encrypt)

- [ ] **Update URLs**
  - Frontend: Update `REACT_APP_SITE_URL` in `.env`
  - Sitemap: Update all URLs in `sitemap.xml`
  - Schema: Update URLs in schema.js if hardcoded

### Google Search Console Setup

- [ ] **Create Properties for Each Locale**
  1. `https://sabitcebeci.com/en-ie/` - Ireland (English)
  2. `https://sabitcebeci.com/it-it/` - Italy (Italian)
  3. `https://sabitcebeci.com/en/` - Europe (English)

- [ ] **Submit Sitemaps**
  - Submit `https://sabitcebeci.com/sitemap.xml` to each property

- [ ] **Set Geographic Target**
  - Ireland property → Target: Ireland
  - Italy property → Target: Italy
  - Europe property → No specific target

- [ ] **Verify Hreflang**
  - Use Google Search Console International Targeting report
  - Check for hreflang errors

### Analytics & Tracking

- [ ] **Google Analytics 4**
  - Create property with subproperties for each locale
  - Install GA4 tracking code
  - Set up custom events: Contact form, CV download, Language switch

- [ ] **Bing Webmaster Tools**
  - Add site and submit sitemap
  - Verify hreflang implementation

### Content Review (IMPORTANT)

- [ ] **Italian Content Native Review**
  - Have a native Italian speaker review all Italian content
  - Check for naturalness and localization
  - Ensure technical terms are accurate

- [ ] **English Content Proofread**
  - Check all English content for errors
  - Verify technical terminology

- [ ] **Schema Validation**
  - Test all pages with Google Rich Results Test
  - Validate JSON-LD schema

### Performance Optimization

- [ ] **Lighthouse Audit**
  - Run on all major pages
  - Target: 90+ on Performance, SEO, Accessibility

- [ ] **Core Web Vitals**
  - LCP < 2.5s
  - FID < 100ms
  - CLS < 0.1

- [ ] **Image Optimization**
  - Compress all images
  - Add proper alt text
  - Use WebP format where possible

### Security & Compliance

- [ ] **GDPR Compliance** (if targeting EU)
  - Add cookie consent banner
  - Create privacy policy page
  - Add contact data processing notice

- [ ] **SSL Certificate**
  - Ensure HTTPS everywhere
  - No mixed content warnings

---

## 📊 SEO Monitoring (Post-Launch)

### Week 1
- [ ] Verify all pages indexed in Google
- [ ] Check Search Console for crawl errors
- [ ] Monitor hreflang implementation

### Month 1
- [ ] Track keyword rankings for target keywords:
  - **Ireland:** "SEVESO consultant Ireland", "ATEX compliance Dublin"
  - **Italy:** "consulente SEVESO Italia", "conformità ATEX Italia"
- [ ] Monitor organic traffic by locale
- [ ] Check bounce rate and engagement

### Ongoing
- [ ] Monthly keyword ranking reports
- [ ] Quarterly content updates
- [ ] Annual SEO audit

---

## 🎯 Target Keywords by Market

### Ireland (en-IE)
**Primary:**
- SEVESO consultant Ireland
- ATEX compliance Dublin
- Process safety consultant Ireland
- Explosion protection consultant
- COMAH consultant Ireland

**Long-tail:**
- Upper tier SEVESO Ireland
- Pharmaceutical process safety Dublin
- Chemical safety consultant Ireland
- HAZOP studies Ireland

### Italy (it-IT)
**Primary:**
- Consulente SEVESO Italia
- Conformità ATEX Italia
- Consulente sicurezza processo
- Protezione esplosioni Italia

**Long-tail:**
- Sito SEVESO soglia superiore
- Consulente sicurezza farmaceutica
- Conformità direttiva SEVESO III

---

## 🔧 Maintenance

### Monthly
- Review and respond to contact form submissions
- Update CV if certifications added
- Check for broken links
- Monitor site performance

### Quarterly
- Update content with new projects (if allowed)
- Add new certifications
- Review and update keywords
- Analyze competitor SEO

### Annually
- Major content refresh
- SEO audit and strategy review
- Update photos/visuals
- Review and update schema markup

---

## 📞 Support & Issues

### Common Issues

**Issue:** Language switcher not working
- Check React Router configuration
- Verify locale context is properly wrapped
- Check browser console for errors

**Issue:** Hreflang errors in Search Console
- Verify all alternate links are correct
- Ensure bidirectional linking
- Check for typos in locale codes

**Issue:** Contact form not submitting
- Verify backend is running
- Check CORS configuration
- Verify MongoDB connection

**Issue:** SEO pages not indexing
- Check robots.txt is not blocking
- Verify sitemap is accessible
- Check for noindex meta tags

---

## 🎓 Resources

- [Google Search Central - International SEO](https://developers.google.com/search/docs/specialty/international)
- [Hreflang Tag Generator](https://www.aleydasolis.com/english/international-seo-tools/hreflang-tags-generator/)
- [Schema.org Documentation](https://schema.org/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)

---

## 📝 Notes

- Site is built as **independent consultant portfolio**, not corporate
- **No location restrictions** - available for international projects
- **Current employment safe** - positioned as personal expertise showcase
- All **market-specific language removed** - universal appeal
- **Professional tone** - consultant not company

---

**Deployment Status:** ✅ Ready for Production

**Last Updated:** January 2026
**Version:** 1.0.0
