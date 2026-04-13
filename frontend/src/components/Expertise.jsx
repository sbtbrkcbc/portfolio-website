import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import { Building2, Pill, Sprout, Hammer, Fuel, Factory } from 'lucide-react';
import { Badge } from './ui/badge';

const Expertise = () => {
  const { t } = useLanguage();

  const industryIcons = [
    Building2,
    Pill,
    Sprout,
    Hammer,
    Fuel,
    Factory
  ];

  return (
    <section id="expertise" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            {t.expertise.title}
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            {t.expertise.subtitle}
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {t.expertise.industries.map((industry, index) => {
            const Icon = industryIcons[index];
            return (
              <div
                key={index}
                className="flex items-center space-x-4 p-6 bg-gray-50 rounded-lg hover:bg-blue-50 transition-colors duration-300 border border-gray-200 hover:border-blue-200"
              >
                <div className="w-12 h-12 bg-white rounded-lg flex items-center justify-center shadow-sm">
                  <Icon className="h-6 w-6 text-blue-600" />
                </div>
                <span className="text-gray-900 font-medium">{industry}</span>
              </div>
            );
          })}
        </div>

        {/* Key Technical Skills */}
        <div className="mt-16 text-center">
          <h3 className="text-2xl font-bold text-gray-900 mb-8">Technical Expertise</h3>
          <div className="flex flex-wrap justify-center gap-3">
            {[
              'SEVESO Directive',
              'COMAH Regulations',
              'ATEX Directive',
              'LOPA Analysis',
              'ISO 60079',
              'HAZOP Studies',
              'Risk Assessment',
              'DNV PHAST',
              'Consequence Modeling',
              'ISO 45001',
              'ISO 14001',
              'Process Safety',
              'Emergency Planning',
              'GMP Environment'
            ].map((skill, index) => (
              <Badge
                key={index}
                variant="secondary"
                className="px-4 py-2 text-sm bg-gray-100 hover:bg-blue-100 text-gray-800 border border-gray-300"
              >
                {skill}
              </Badge>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Expertise;