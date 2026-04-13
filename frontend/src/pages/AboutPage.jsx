import React from 'react';
import { useLocale } from '../context/LocaleContext';
import SEOHead from '../components/SEO/SEOHead';
import { getPersonSchema } from '../components/SEO/schemas';
import { CheckCircle2 } from 'lucide-react';
import { Card } from '../components/ui/card';

const AboutPage = () => {
  const { locale, t } = useLocale();
  const schema = getPersonSchema();

  const pageTitle = locale === 'it-it' 
    ? 'Chi Sono | Consulente Senior Sicurezza di Processo'
    : 'About | Senior Process Safety Consultant Ireland';
    
  const pageDescription = t.about.description.substring(0, 155);

  return (
    <>
      <SEOHead
        title={pageTitle}
        description={pageDescription}
        schema={schema}
      />

      <section className="pt-24 pb-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">{t.about.title}</h1>
            <h2 className="text-xl text-gray-600">{t.about.subtitle}</h2>
          </div>

          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <p className="text-lg text-gray-700 leading-relaxed mb-6">
                {t.about.description}
              </p>
              {locale === 'en-ie' && (
                <p className="text-sm text-gray-600 italic bg-blue-50 p-4 rounded-lg border-l-4 border-blue-600">
                  {t.about.clients}
                </p>
              )}
            </div>

            <Card className="p-8 bg-gradient-to-br from-blue-50 to-indigo-50 border-none shadow-lg">
              <h3 className="text-2xl font-bold text-gray-900 mb-6">Key Competencies</h3>
              <div className="space-y-4">
                {t.about.highlights.map((highlight, index) => (
                  <div key={index} className="flex items-start space-x-3">
                    <CheckCircle2 className="h-6 w-6 text-blue-600 flex-shrink-0 mt-0.5" />
                    <span className="text-gray-700 font-medium">{highlight}</span>
                  </div>
                ))}
              </div>
            </Card>
          </div>
        </div>
      </section>
    </>
  );
};

export default AboutPage;