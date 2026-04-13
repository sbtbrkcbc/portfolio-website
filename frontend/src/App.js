import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import { LocaleProvider } from './context/LocaleContext';
import { Toaster } from './components/ui/toaster';
import './App.css';

// Layouts
import LocaleLayout from './layouts/LocaleLayout';

// Pages
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import ServicesPage from './pages/ServicesPage';
import ServiceDetailPage from './pages/ServiceDetailPage';
import IndustriesPage from './pages/IndustriesPage';
import IndustryDetailPage from './pages/IndustryDetailPage';
import CertificationsPage from './pages/CertificationsPage';
import ExperiencePage from './pages/ExperiencePage';
import ContactPage from './pages/ContactPage';

function App() {
  return (
    <HelmetProvider>
      <BrowserRouter>
        <div className="App">
          <Routes>
            {/* Redirect root to default locale */}
            <Route path="/" element={<Navigate to="/en-ie" replace />} />
            
            {/* Locale-based routes */}
            <Route path="/:locale" element={<LocaleProvider><LocaleLayout /></LocaleProvider>}>
              <Route index element={<HomePage />} />
              
              <Route path="about" element={<AboutPage />} />
              <Route path="chi-sono" element={<AboutPage />} />
              <Route path="hakkimda" element={<AboutPage />} />
              
              <Route path="services" element={<ServicesPage />} />
              <Route path="servizi" element={<ServicesPage />} />
              <Route path="hizmetler" element={<ServicesPage />} />
              <Route path="services/:serviceSlug" element={<ServiceDetailPage />} />
              <Route path="servizi/:serviceSlug" element={<ServiceDetailPage />} />
              <Route path="hizmetler/:serviceSlug" element={<ServiceDetailPage />} />
              
              <Route path="industries" element={<IndustriesPage />} />
              <Route path="settori" element={<IndustriesPage />} />
              <Route path="sektorler" element={<IndustriesPage />} />
              <Route path="industries/:industrySlug" element={<IndustryDetailPage />} />
              <Route path="settori/:industrySlug" element={<IndustryDetailPage />} />
              <Route path="sektorler/:industrySlug" element={<IndustryDetailPage />} />
              
              <Route path="certifications" element={<CertificationsPage />} />
              <Route path="certificazioni" element={<CertificationsPage />} />
              <Route path="sertifikalar" element={<CertificationsPage />} />
              
              <Route path="experience" element={<ExperiencePage />} />
              <Route path="esperienza" element={<ExperiencePage />} />
              <Route path="deneyim" element={<ExperiencePage />} />
              
              <Route path="contact" element={<ContactPage />} />
              <Route path="contatti" element={<ContactPage />} />
              <Route path="iletisim" element={<ContactPage />} />
            </Route>

            {/* 404 - redirect to default locale home */}
            <Route path="*" element={<Navigate to="/en-ie" replace />} />
          </Routes>
          <Toaster />
        </div>
      </BrowserRouter>
    </HelmetProvider>
  );
}

export default App;
