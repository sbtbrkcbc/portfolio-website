import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { useLocale } from '../context/LocaleContext';
import SEOHead from '../components/SEO/SEOHead';
import { CheckCircle2, ArrowRight } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';

const IndustryDetailPage = () => {
  const { industrySlug } = useParams();
  const { locale, t } = useLocale();
  
  const industry = t.industries.items.find(i => i.slug === industrySlug);
  
  if (!industry) {
    return <div className="pt-24 text-center">Industry not found</div>;
  }

  return (
    <>
      <SEOHead
        title={`${industry.title} | ${locale === 'it-it' ? 'Consulenza Specializzata' : 'Specialized Consultancy'}`}
        description={industry.description}
      />

      <section className="pt-24 pb-20 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="mb-8">
            <Link 
              to={`/${locale}/${locale === 'it-it' ? 'settori' : 'industries'}`}
              className="text-blue-600 hover:text-blue-700 inline-flex items-center mb-4"
            >
              ← {locale === 'it-it' ? 'Torna ai Settori' : 'Back to Industries'}
            </Link>
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">{industry.title}</h1>
          </div>

          <Card className="p-8 mb-12">
            <p className="text-lg text-gray-700 leading-relaxed mb-6">{industry.description}</p>
            
            <h3 className="text-xl font-bold text-gray-900 mb-4">
              {locale === 'it-it' ? 'Competenze Chiave' : 'Key Expertise'}
            </h3>
            <div className="space-y-3">
              {industry.highlights.map((highlight, index) => (
                <div key={index} className="flex items-start space-x-3">
                  <CheckCircle2 className="h-6 w-6 text-blue-600 flex-shrink-0 mt-0.5" />
                  <span className="text-gray-700">{highlight}</span>
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

export default IndustryDetailPage;