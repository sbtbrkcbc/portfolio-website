import React from 'react';
import { Link } from 'react-router-dom';
import { useLocale } from '../../context/LocaleContext';
import { Mail, Linkedin } from 'lucide-react';

const Footer = () => {
  const { locale, t } = useLocale();
  const currentYear = new Date().getFullYear();
  const getNavLink = (path) => `/${locale}${path}`;

  return (
    <footer className="bg-gray-900 text-white py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid md:grid-cols-4 gap-8 mb-8">
          <div>
            <h3 className="text-xl font-bold mb-4">Sabit Burak Cebeci</h3>
            <p className="text-gray-400">{t.footer.tagline}</p>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4">{t.footer.services}</h4>
            <div className="space-y-2">
              <Link to={getNavLink(locale === 'it-it' ? '/servizi' : '/services')} className="block text-gray-400 hover:text-white transition-colors">
                {t.footer.services}
              </Link>
              <Link to={getNavLink(locale === 'it-it' ? '/settori' : '/industries')} className="block text-gray-400 hover:text-white transition-colors">
                {t.footer.industries}
              </Link>
            </div>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4">{t.footer.company}</h4>
            <div className="space-y-2">
              <Link to={getNavLink(locale === 'it-it' ? '/chi-sono' : '/about')} className="block text-gray-400 hover:text-white transition-colors">
                {t.nav.about}
              </Link>
              <Link to={getNavLink(locale === 'it-it' ? '/certificazioni' : '/certifications')} className="block text-gray-400 hover:text-white transition-colors">
                {t.nav.certifications}
              </Link>
              <Link to={getNavLink(locale === 'it-it' ? '/contatti' : '/contact')} className="block text-gray-400 hover:text-white transition-colors">
                {t.nav.contact}
              </Link>
            </div>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4">Connect</h4>
            <div className="space-y-3">
              <a href="mailto:sabitburakcebeci@gmail.com" className="flex items-center space-x-2 text-gray-400 hover:text-white transition-colors">
                <Mail className="h-5 w-5" />
                <span className="text-sm">sabitburakcebeci@gmail.com</span>
              </a>
              <a href="https://www.linkedin.com/in/sbtbrkcbc/" target="_blank" rel="noopener noreferrer" className="flex items-center space-x-2 text-gray-400 hover:text-white transition-colors">
                <Linkedin className="h-5 w-5" />
                <span className="text-sm">LinkedIn</span>
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-800 pt-8 text-center text-gray-400 text-sm">
          <p>© {currentYear} Sabit Burak Cebeci. {t.footer.copyright}.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;