import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import { Award, GraduationCap } from 'lucide-react';
import { Card } from './ui/card';
import { Badge } from './ui/badge';

const Certifications = () => {
  const { t } = useLanguage();

  return (
    <section id="certifications" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            {t.certifications.title}
          </h2>
        </div>

        <div className="grid lg:grid-cols-2 gap-12">
          {/* Certifications */}
          <Card className="p-8 bg-gradient-to-br from-blue-50 to-white border-gray-200">
            <div className="flex items-center space-x-3 mb-6">
              <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
                <Award className="h-6 w-6 text-white" />
              </div>
              <h3 className="text-2xl font-bold text-gray-900">Certifications</h3>
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

          {/* Education */}
          <Card className="p-8 bg-gradient-to-br from-blue-50 to-white border-gray-200">
            <div className="flex items-center space-x-3 mb-6">
              <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
                <GraduationCap className="h-6 w-6 text-white" />
              </div>
              <h3 className="text-2xl font-bold text-gray-900">{t.certifications.education}</h3>
            </div>
            <div className="space-y-4">
              {t.certifications.degrees.map((degree, index) => (
                <div
                  key={index}
                  className="p-4 bg-white rounded-lg hover:shadow-md transition-shadow duration-200 border-l-4 border-blue-600"
                >
                  <p className="text-gray-900 font-semibold">{degree}</p>
                </div>
              ))}
            </div>

            {/* Professional Memberships */}
            <div className="mt-8">
              <h4 className="text-lg font-bold text-gray-900 mb-4">Professional Memberships</h4>
              <div className="space-y-2">
                <Badge variant="secondary" className="mr-2 bg-gray-100 text-gray-800 border border-gray-300">
                  Chamber of Environmental Engineers
                </Badge>
                <Badge variant="secondary" className="bg-gray-100 text-gray-800 border border-gray-300">
                  Engineers Ireland
                </Badge>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default Certifications;