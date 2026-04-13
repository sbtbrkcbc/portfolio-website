import React from 'react';
import { Link } from 'react-router-dom';
import { useLocale } from '../context/LocaleContext';
import SEOHead from '../components/SEO/SEOHead';
import { Shield, FileCheck, AlertTriangle, Settings, ArrowRight } from 'lucide-react';
import { Card } from '../components/ui/card';

const ServicesPage = () => {
  const { locale, t } = useLocale();
  
  const icons = [Shield, FileCheck, AlertTriangle, Settings];
  
  const pageTitle = locale === 'it-it'
    ? 'Servizi di Consulenza SEVESO e ATEX | Sicurezza di Processo'
    : 'SEVESO & ATEX Consultancy Services | Process Safety Ireland';
  
  return (
    <>
      <SEOHead
        title={pageTitle}
        description={t.services.subtitle}
      />

      <section className="pt-24 pb-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">{t.services.title}</h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">{t.services.subtitle}</p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {t.services.items.map((service, index) => {
              const Icon = icons[index];
              return (
                <Card key={index} className="p-8 hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
                  <div className="mb-4">
                    <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                      <Icon className="h-6 w-6 text-blue-600" />
                    </div>
                  </div>
                  <h2 className="text-2xl font-bold text-gray-900 mb-3">{service.title}</h2>
                  <p className="text-gray-600 mb-4">{service.description}</p>
                  
                  <div className="space-y-2 mb-6">
                    {service.features.map((feature, idx) => (
                      <div key={idx} className="flex items-start space-x-2">
                        <div className="w-1.5 h-1.5 bg-blue-600 rounded-full mt-2 flex-shrink-0"></div>
                        <span className="text-sm text-gray-600">{feature}</span>
                      </div>
                    ))}
                  </div>
                  
                  <Link 
                    to={`/${locale}/${locale === 'it-it' ? 'servizi' : 'services'}/${service.slug}`}
                    className="text-blue-600 hover:text-blue-700 font-medium inline-flex items-center"
                  >
                    {locale === 'it-it' ? 'Scopri di più' : 'Learn More'}
                    <ArrowRight className="ml-1 h-4 w-4" />
                  </Link>
                </Card>
              );
            })}
          </div>
        </div>
      </section>
    </>
  );
};

export default ServicesPage;