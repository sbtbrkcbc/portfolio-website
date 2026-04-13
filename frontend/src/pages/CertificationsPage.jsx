import React from 'react';
import { useLocale } from '../context/LocaleContext';
import SEOHead from '../components/SEO/SEOHead';
import { Award, GraduationCap } from 'lucide-react';
import { Card } from '../components/ui/card';
import { Badge } from '../components/ui/badge';

const CertificationsPage = () => {
  const { locale, t } = useLocale();

  const pageTitle = locale === 'it-it'
    ? 'Certificazioni e Qualifiche Professionali'
    : 'Professional Certifications & Qualifications';

  return (
    <>
      <SEOHead
        title={pageTitle}
        description={t.certifications.subtitle}
      />

      <section className="pt-24 pb-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">{t.certifications.title}</h1>
            <p className="text-xl text-gray-600">{t.certifications.subtitle}</p>
          </div>

          <div className="grid lg:grid-cols-2 gap-12">
            <Card className="p-8 bg-gradient-to-br from-blue-50 to-white border-gray-200">
              <div className="flex items-center space-x-3 mb-6">
                <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
                  <Award className="h-6 w-6 text-white" />
                </div>
                <h2 className="text-2xl font-bold text-gray-900">Certifications</h2>
              </div>
              <div className="space-y-3">
                {t.certifications.items.map((cert, index) => (
                  <div
                    key={index}
                    className="flex items-start space-x-2 p-3 bg-white rounded-lg hover:shadow-md transition-shadow duration-200"
                  >
                    <div className="w-2 h-2 bg-blue-600 rounded-full mt-2 flex-shrink-0"></div>
                    <span className="text-gray-700">{cert}</span>
                  </div>
                ))}
              </div>
            </Card>

            <Card className="p-8 bg-gradient-to-br from-indigo-50 to-white border-gray-200">
              <div className="flex items-center space-x-3 mb-6">
                <div className="w-12 h-12 bg-indigo-600 rounded-lg flex items-center justify-center">
                  <GraduationCap className="h-6 w-6 text-white" />
                </div>
                <h2 className="text-2xl font-bold text-gray-900">{t.certifications.education || 'Education'}</h2>
              </div>
              <div className="space-y-4">
                {t.certifications.education.map((degree, index) => (
                  <div
                    key={index}
                    className="p-4 bg-white rounded-lg hover:shadow-md transition-shadow duration-200 border-l-4 border-indigo-600"
                  >
                    <p className="text-gray-900 font-semibold">{degree}</p>
                  </div>
                ))}
              </div>

              <div className="mt-8">
                <h3 className="text-lg font-bold text-gray-900 mb-4">
                  {locale === 'it-it' ? 'Associazioni Professionali' : 'Professional Memberships'}
                </h3>
                <div className="space-y-2">
                  {t.certifications.memberships.map((membership, index) => (
                    <Badge key={index} variant="secondary" className="mr-2 bg-gray-100 text-gray-800 border border-gray-300">
                      {membership}
                    </Badge>
                  ))}
                </div>
              </div>
            </Card>
          </div>
        </div>
      </section>
    </>
  );
};

export default CertificationsPage;