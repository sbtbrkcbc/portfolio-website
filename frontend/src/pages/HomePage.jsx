import React from 'react';
import { Link } from 'react-router-dom';
import { useLocale } from '../context/LocaleContext';
import SEOHead from '../components/SEO/SEOHead';
import { getOrganizationSchema } from '../components/SEO/schemas';
import { Award, MapPin, Download, Linkedin, ArrowRight } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';

const HomePage = () => {
  const { locale, t } = useLocale();
  const schema = getOrganizationSchema(locale);

  const handleDownloadCV = () => {
    const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
    // Extract language code from locale (e.g., 'de-de' -> 'de')
    const lang = locale.split('-')[0];
    window.open(`${BACKEND_URL}/api/cv/download?lang=${lang}`, '_blank');
  };

  return (
    <>
      <SEOHead
        title={t.meta.siteTitle}
        description={t.meta.siteDescription}
        keywords={t.meta.keywords}
        schema={schema}
      />

      {/* Hero Section */}
      <section className="pt-24 pb-16 bg-gradient-to-b from-gray-50 to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-6">
              <div className="space-y-2">
                <h1 className="text-4xl md:text-5xl font-bold text-gray-900 leading-tight">
                  {t.hero.title}
                </h1>
                <h2 className="text-2xl md:text-3xl font-semibold text-gray-700">
                  {t.hero.subtitle}
                </h2>
                <p className="text-lg text-gray-600">
                  {t.hero.description}
                </p>
              </div>

              <div className="flex flex-wrap gap-4">
                <Link 
                  to={`/${locale}/${locale === 'it-it' ? 'esperienza' : locale === 'tr-tr' ? 'deneyim' : 'experience'}`}
                  className="flex items-center space-x-2 bg-white px-4 py-2 rounded-lg shadow-sm border border-gray-200 hover:border-[#0F2A4D] hover:shadow-md transition-all duration-200 cursor-pointer group"
                >
                  <Award className="h-5 w-5 text-[#0F2A4D] group-hover:scale-110 transition-transform" />
                  <span className="font-semibold text-gray-900 group-hover:text-[#0F2A4D]">{t.hero.experience}</span>
                </Link>
                <div className="flex items-center space-x-2 bg-white px-4 py-2 rounded-lg shadow-sm border border-gray-200">
                  <MapPin className="h-5 w-5 text-blue-600" />
                  <span className="font-medium text-gray-700">{t.hero.location}</span>
                </div>
              </div>

              <div className="flex flex-wrap gap-4 pt-4">
                <Link to={`/${locale}/${locale === 'it-it' ? 'contatti' : 'contact'}`}>
                  <Button size="lg" className="bg-blue-600 hover:bg-blue-700 text-white">
                    {t.hero.cta}
                    <ArrowRight className="ml-2 h-4 w-4" />
                  </Button>
                </Link>
                <Button onClick={handleDownloadCV} variant="outline" size="lg" className="border-gray-300 hover:border-blue-600 hover:text-blue-600">
                  <Download className="h-4 w-4 mr-2" />
                  {t.hero.downloadCV}
                </Button>
                <Button onClick={() => window.open('https://www.linkedin.com/in/sbtbrkcbc/', '_blank')} variant="outline" size="lg" className="border-gray-300 hover:border-blue-600 hover:text-blue-600">
                  <Linkedin className="h-4 w-4 mr-2" />
                  LinkedIn
                </Button>
              </div>

              <p className="text-sm text-gray-600 italic">{t.hero.trustedBy}</p>
            </div>

            <div className="flex justify-center lg:justify-end">
              <div className="relative">
                <div className="w-72 h-72 md:w-96 md:h-96 rounded-2xl overflow-hidden shadow-2xl border-4 border-white">
                  <img src="https://customer-assets.emergentagent.com/job_ebec55f7-c812-4792-86fc-6db1e6d3ab72/artifacts/k6hhn75q_Sabit%203.jpg" alt="Sabit Burak Cebeci" className="w-full h-full object-cover" />
                </div>
                <div className="absolute -bottom-4 -right-4 w-24 h-24 bg-blue-600 rounded-2xl opacity-20"></div>
                <div className="absolute -top-4 -left-4 w-24 h-24 bg-indigo-600 rounded-2xl opacity-20"></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Services Preview */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{t.services.title}</h2>
            <p className="text-lg text-gray-600">{t.services.subtitle}</p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {t.services.items.slice(0, 4).map((service, index) => (
              <Card key={index} className="p-6 hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
                <h3 className="text-xl font-bold text-gray-900 mb-3">{service.title}</h3>
                <p className="text-gray-600 mb-4">{service.shortDesc}</p>
                <Link to={`/${locale}/${locale === 'it-it' ? 'servizi' : 'services'}/${service.slug}`} className="text-blue-600 hover:text-blue-700 font-medium inline-flex items-center">
                  {locale === 'it-it' ? 'Scopri di più' : 'Learn More'}
                  <ArrowRight className="ml-1 h-4 w-4" />
                </Link>
              </Card>
            ))}
          </div>

          <div className="text-center mt-12">
            <Link to={`/${locale}/${locale === 'it-it' ? 'servizi' : 'services'}`}>
              <Button size="lg" variant="outline" className="border-blue-600 text-blue-600 hover:bg-blue-50">
                {locale === 'it-it' ? 'Vedi Tutti i Servizi' : 'View All Services'}
                <ArrowRight className="ml-2 h-4 w-4" />
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Industries */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{t.industries.title}</h2>
            <p className="text-lg text-gray-600">{t.industries.subtitle}</p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {t.industries.items.map((industry, index) => (
              <Card key={index} className="p-8 bg-white hover:shadow-xl transition-all duration-300">
                <h3 className="text-2xl font-bold text-gray-900 mb-4">{industry.title}</h3>
                <p className="text-gray-600 mb-6">{industry.description}</p>
                <Link to={`/${locale}/${locale === 'it-it' ? 'settori' : 'industries'}/${industry.slug}`} className="text-blue-600 hover:text-blue-700 font-medium inline-flex items-center">
                  {locale === 'it-it' ? 'Esplora Settore' : 'Explore Industry'}
                  <ArrowRight className="ml-1 h-4 w-4" />
                </Link>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-blue-600 text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            {locale === 'it-it' ? 'Pronto a Iniziare?' : 'Ready to Get Started?'}
          </h2>
          <p className="text-xl mb-8 text-blue-100">
            {t.contact.subtitle}
          </p>
          <Link to={`/${locale}/${locale === 'it-it' ? 'contatti' : 'contact'}`}>
            <Button size="lg" className="bg-white text-blue-600 hover:bg-gray-100">
              {t.hero.cta}
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
          </Link>
        </div>
      </section>
    </>
  );
};

export default HomePage;