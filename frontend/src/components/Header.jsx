import React, { useState } from 'react';
import { useLanguage } from '../context/LanguageContext';
import { Menu, X, Globe } from 'lucide-react';
import { Button } from './ui/button';

const Header = () => {
  const { language, setLanguage, t } = useLanguage();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [langMenuOpen, setLangMenuOpen] = useState(false);

  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });
      setMobileMenuOpen(false);
    }
  };

  const languages = [
    { code: 'en', label: 'English' },
    { code: 'it', label: 'Italiano' },
    { code: 'tr', label: 'Türkçe' }
  ];

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo/Name */}
          <div className="flex-shrink-0">
            <h1 className="text-xl font-bold text-gray-900">Sabit Burak Cebeci</h1>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            <button
              onClick={() => scrollToSection('about')}
              className="text-gray-700 hover:text-gray-900 transition-colors font-medium"
            >
              {t.nav.about}
            </button>
            <button
              onClick={() => scrollToSection('services')}
              className="text-gray-700 hover:text-gray-900 transition-colors font-medium"
            >
              {t.nav.services}
            </button>
            <button
              onClick={() => scrollToSection('expertise')}
              className="text-gray-700 hover:text-gray-900 transition-colors font-medium"
            >
              {t.nav.expertise}
            </button>
            <button
              onClick={() => scrollToSection('experience')}
              className="text-gray-700 hover:text-gray-900 transition-colors font-medium"
            >
              {t.nav.experience}
            </button>
            <button
              onClick={() => scrollToSection('certifications')}
              className="text-gray-700 hover:text-gray-900 transition-colors font-medium"
            >
              {t.nav.certifications}
            </button>
            <button
              onClick={() => scrollToSection('contact')}
              className="text-gray-700 hover:text-gray-900 transition-colors font-medium"
            >
              {t.nav.contact}
            </button>

            {/* Language Switcher */}
            <div className="relative">
              <Button
                variant="outline"
                size="sm"
                onClick={() => setLangMenuOpen(!langMenuOpen)}
                className="flex items-center space-x-1"
              >
                <Globe className="h-4 w-4" />
                <span>{language.toUpperCase()}</span>
              </Button>
              {langMenuOpen && (
                <div className="absolute right-0 mt-2 w-36 bg-white rounded-md shadow-lg border border-gray-200">
                  {languages.map((lang) => (
                    <button
                      key={lang.code}
                      onClick={() => {
                        setLanguage(lang.code);
                        setLangMenuOpen(false);
                      }}
                      className={`block w-full text-left px-4 py-2 text-sm hover:bg-gray-100 ${
                        language === lang.code ? 'bg-gray-50 font-medium' : ''
                      }`}
                    >
                      {lang.label}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </nav>

          {/* Mobile menu button */}
          <div className="md:hidden flex items-center space-x-2">
            <div className="relative">
              <Button
                variant="outline"
                size="sm"
                onClick={() => setLangMenuOpen(!langMenuOpen)}
                className="flex items-center space-x-1"
              >
                <Globe className="h-4 w-4" />
                <span>{language.toUpperCase()}</span>
              </Button>
              {langMenuOpen && (
                <div className="absolute right-0 mt-2 w-36 bg-white rounded-md shadow-lg border border-gray-200">
                  {languages.map((lang) => (
                    <button
                      key={lang.code}
                      onClick={() => {
                        setLanguage(lang.code);
                        setLangMenuOpen(false);
                      }}
                      className={`block w-full text-left px-4 py-2 text-sm hover:bg-gray-100 ${
                        language === lang.code ? 'bg-gray-50 font-medium' : ''
                      }`}
                    >
                      {lang.label}
                    </button>
                  ))}
                </div>
              )}
            </div>
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="text-gray-700 hover:text-gray-900"
            >
              {mobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <nav className="md:hidden py-4 space-y-2 border-t border-gray-200">
            <button
              onClick={() => scrollToSection('about')}
              className="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md"
            >
              {t.nav.about}
            </button>
            <button
              onClick={() => scrollToSection('services')}
              className="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md"
            >
              {t.nav.services}
            </button>
            <button
              onClick={() => scrollToSection('expertise')}
              className="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md"
            >
              {t.nav.expertise}
            </button>
            <button
              onClick={() => scrollToSection('experience')}
              className="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md"
            >
              {t.nav.experience}
            </button>
            <button
              onClick={() => scrollToSection('certifications')}
              className="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md"
            >
              {t.nav.certifications}
            </button>
            <button
              onClick={() => scrollToSection('contact')}
              className="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md"
            >
              {t.nav.contact}
            </button>
          </nav>
        )}
      </div>
    </header>
  );
};

export default Header;