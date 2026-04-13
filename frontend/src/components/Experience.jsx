import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import { Briefcase, MapPin, Calendar } from 'lucide-react';
import { Card } from './ui/card';
import { Badge } from './ui/badge';

const Experience = () => {
  const { t } = useLanguage();

  return (
    <section id="experience" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            {t.experience.title}
          </h2>
        </div>

        <div className="max-w-4xl mx-auto space-y-8">
          {t.experience.positions.map((position, index) => (
            <Card key={index} className="p-8 bg-white border-gray-200 hover:shadow-lg transition-shadow duration-300">
              <div className="flex flex-col md:flex-row md:items-start md:justify-between mb-6">
                <div className="mb-4 md:mb-0">
                  <div className="flex items-center space-x-2 mb-2">
                    <Briefcase className="h-5 w-5 text-emerald-600" />
                    <h3 className="text-2xl font-bold text-gray-900">{position.role}</h3>
                  </div>
                  <p className="text-lg font-semibold text-gray-700 mb-2">{position.company}</p>
                  <div className="flex flex-wrap items-center gap-3 text-sm text-gray-600">
                    <div className="flex items-center space-x-1">
                      <MapPin className="h-4 w-4" />
                      <span>{position.location}</span>
                    </div>
                    <div className="flex items-center space-x-1">
                      <Calendar className="h-4 w-4" />
                      <span>{position.period}</span>
                    </div>
                  </div>
                </div>
                {index === 0 && (
                  <Badge className="bg-emerald-600 text-white hover:bg-emerald-700">
                    {t.experience.current}
                  </Badge>
                )}
              </div>

              <div className="space-y-2">
                {position.responsibilities.map((responsibility, idx) => (
                  <div key={idx} className="flex items-start space-x-2">
                    <div className="w-1.5 h-1.5 bg-emerald-600 rounded-full mt-2 flex-shrink-0"></div>
                    <p className="text-gray-700">{responsibility}</p>
                  </div>
                ))}
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Experience;