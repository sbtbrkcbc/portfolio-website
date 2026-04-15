import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useLocale } from '../../context/LocaleContext';
import { Menu, X, Globe } from 'lucide-react';
import { Button } from '../ui/button';

const Header = () => {
  const { locale, t } = useLocale();
  const navigate = useNavigate();
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [langMenuOpen, setLangMenuOpen] = useState(false);

  const locales = [
    { code: 'en-ie', label: 'English', flag: '🇬🇧' },
    { code: 'de-de', label: 'Deutsch', flag: '🇩🇪' },
    { code: 'fr-fr', label: 'Français', flag: '🇫🇷' },
    { code: 'es-es', label: 'Español', flag: '🇪🇸' },
    { code: 'it-it', label: 'Italiano', flag: '🇮🇹' },
    { code: 'se-se', label: 'Svenska', flag: '🇸🇪' },
    { code: 'tr-tr', label: 'Türkçe', flag: '🇹🇷' }
  ];

  const switchLocale = (newLocale) => {
    const currentPath = location.pathname.replace(`/${locale}`, '');
    navigate(`/${newLocale}${currentPath}`);
    setLangMenuOpen(false);
  };

  const getNavLink = (path) => `/${locale}${path}`;

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex-shrink-0">
            <Link to={getNavLink('')} className="text-xl font-bold text-gray-900">
              Sabit Burak Cebeci
            </Link>
          </div>

          <nav className="hidden md:flex items-center space-x-8">
            <Link to={getNavLink(locale === 'it-it' ? '/chi-sono' : locale === 'tr-tr' ? '/hakkimda' : '/about')} className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              {t.nav.about}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/servizi' : locale === 'tr-tr' ? '/hizmetler' : '/services')} className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              {t.nav.services}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/settori' : locale === 'tr-tr' ? '/sektorler' : '/industries')} className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              {t.nav.industries}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/certificazioni' : locale === 'tr-tr' ? '/sertifikalar' : '/certifications')} className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              {t.nav.certifications}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/esperienza' : locale === 'tr-tr' ? '/deneyim' : '/experience')} className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              {t.nav.experience}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/contatti' : locale === 'tr-tr' ? '/iletisim' : '/contact')} className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              {t.nav.contact}
            </Link>

            <div className="relative">
              <Button
                variant="outline"
                size="sm"
                onClick={() => setLangMenuOpen(!langMenuOpen)}
                className="flex items-center space-x-1"
              >
                <Globe className="h-4 w-4" />
                <span>{locale.toUpperCase()}</span>
              </Button>
              {langMenuOpen && (
                <div className="absolute right-0 mt-2 w-56 bg-white rounded-md shadow-lg border border-gray-200 py-1">
                  {locales.map((loc) => (
                    <button
                      key={loc.code}
                      onClick={() => switchLocale(loc.code)}
                      className={`block w-full text-left px-4 py-2 text-sm hover:bg-gray-100 ${
                        locale === loc.code ? 'bg-blue-50 font-medium text-blue-600' : 'text-gray-700'
                      }`}
                    >
                      <span className="mr-2">{loc.flag}</span>
                      {loc.label}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </nav>

          <div className="md:hidden flex items-center space-x-2">
            <Button
              variant="outline"
              size="sm"
              onClick={() => setLangMenuOpen(!langMenuOpen)}
            >
              <Globe className="h-4 w-4" />
            </Button>
            {langMenuOpen && (
              <div className="absolute right-16 top-16 w-56 bg-white rounded-md shadow-lg border border-gray-200 py-1">
                {locales.map((loc) => (
                  <button
                    key={loc.code}
                    onClick={() => switchLocale(loc.code)}
                    className={`block w-full text-left px-4 py-2 text-sm hover:bg-gray-100 ${
                      locale === loc.code ? 'bg-blue-50 font-medium' : ''
                    }`}
                  >
                    <span className="mr-2">{loc.flag}</span>
                    {loc.label}
                  </button>
                ))}
              </div>
            )}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="text-gray-700 hover:text-gray-900"
            >
              {mobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>
        </div>

        {mobileMenuOpen && (
          <nav className="md:hidden py-4 space-y-2 border-t border-gray-200">
            <Link to={getNavLink(locale === 'it-it' ? '/chi-sono' : locale === 'tr-tr' ? '/hakkimda' : '/about')} className="block px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md" onClick={() => setMobileMenuOpen(false)}>
              {t.nav.about}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/servizi' : locale === 'tr-tr' ? '/hizmetler' : '/services')} className="block px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md" onClick={() => setMobileMenuOpen(false)}>
              {t.nav.services}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/settori' : locale === 'tr-tr' ? '/sektorler' : '/industries')} className="block px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md" onClick={() => setMobileMenuOpen(false)}>
              {t.nav.industries}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/certificazioni' : locale === 'tr-tr' ? '/sertifikalar' : '/certifications')} className="block px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md" onClick={() => setMobileMenuOpen(false)}>
              {t.nav.certifications}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/esperienza' : locale === 'tr-tr' ? '/deneyim' : '/experience')} className="block px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md" onClick={() => setMobileMenuOpen(false)}>
              {t.nav.experience}
            </Link>
            <Link to={getNavLink(locale === 'it-it' ? '/contatti' : locale === 'tr-tr' ? '/iletisim' : '/contact')} className="block px-4 py-2 text-gray-700 hover:bg-gray-50 rounded-md" onClick={() => setMobileMenuOpen(false)}>
              {t.nav.contact}
            </Link>
          </nav>
        )}
      </div>
    </header>
  );
};

export default Header;