import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { useLocale } from '../context/LocaleContext';
import SEOHead from '../components/SEO/SEOHead';
import { getServiceSchema } from '../components/SEO/schemas';
import { CheckCircle2, ArrowRight } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';

const ServiceDetailPage = () => {
  const { serviceSlug } = useParams();
  const { locale, t } = useLocale();
  
  const service = t.services.items.find(s => s.slug === serviceSlug);
  
  if (!service) {
    return <div className="pt-24 text-center">Service not found</div>;
  }
  
  const schema = getServiceSchema(service, locale);

  return (
    <>
      <SEOHead
        title={`${service.title} | ${locale === 'it-it' ? 'Consulenza Professionale' : 'Professional Consultancy'}`}
        description={service.description}
        schema={schema}
      />

      <section className="pt-24 pb-20 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="mb-8">
            <Link 
              to={`/${locale}/${locale === 'it-it' ? 'servizi' : 'services'}`}
              className="text-blue-600 hover:text-blue-700 inline-flex items-center mb-4"
            >
              ← {locale === 'it-it' ? 'Torna ai Servizi' : 'Back to Services'}
            </Link>
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">{service.title}</h1>
            <p className="text-xl text-gray-600">{service.shortDesc}</p>
          </div>

          <Card className="p-8 mb-12">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              {locale === 'it-it' ? 'Descrizione del Servizio' : 'Service Description'}
            </h2>
            <p className="text-lg text-gray-700 leading-relaxed mb-6">{service.description}</p>
            
            <h3 className="text-xl font-bold text-gray-900 mb-4">
              {locale === 'it-it' ? 'Caratteristiche Principali' : 'Key Features'}
            </h3>
            <div className="space-y-3">
              {service.features.map((feature, index) => (
                <div key={index} className="flex items-start space-x-3">
                  <CheckCircle2 className="h-6 w-6 text-blue-600 flex-shrink-0 mt-0.5" />
                  <span className="text-gray-700">{feature}</span>
                </div>
              ))}
            </div>
          </Card>

          <div className="text-center">
            <Link to={`/${locale}/${locale === 'it-it' ? 'contatti' : 'contact'}`}>
              <Button size="lg" className="bg-blue-600 hover:bg-blue-700 text-white">
                {locale === 'it-it' ? 'Richiedi Consulenza' : 'Request Consultation'}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
            </Link>
          </div>
        </div>
      </section>
    </>
  );
};

export default ServiceDetailPage;