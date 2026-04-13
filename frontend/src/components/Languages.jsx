import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import { Globe } from 'lucide-react';
import { Card } from './ui/card';

const Languages = () => {
  const { t } = useLanguage();

  const languages = [
    { name: 'Turkish', level: 'Native', proficiency: 100 },
    { name: 'English', level: 'Professional Working', proficiency: 90 },
    { name: 'Italian', level: 'Limited Working', proficiency: 60 }
  ];

  const languageNames = {
    en: { Turkish: 'Turkish', English: 'English', Italian: 'Italian' },
    it: { Turkish: 'Turco', English: 'Inglese', Italian: 'Italiano' },
    tr: { Turkish: 'Türkçe', English: 'İngilizce', Italian: 'İtalyanca' }
  };

  const levelNames = {
    en: { Native: 'Native', 'Professional Working': 'Professional Working', 'Limited Working': 'Limited Working' },
    it: { Native: 'Madrelingua', 'Professional Working': 'Professionale', 'Limited Working': 'Lavorativo Limitato' },
    tr: { Native: 'Ana Dil', 'Professional Working': 'Profesyonel', 'Limited Working': 'Sınırlı İş Seviyesi' }
  };

  return (
    <section className="py-12 bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-8">
          <div className="flex items-center justify-center space-x-2 mb-4">
            <Globe className="h-8 w-8 text-blue-600" />
            <h3 className="text-2xl font-bold text-gray-900">Languages</h3>
          </div>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {languages.map((lang, index) => (
            <Card key={index} className="p-6 bg-white border-gray-200 hover:shadow-lg transition-shadow duration-300">
              <div className="text-center">
                <h4 className="text-lg font-bold text-gray-900 mb-2">
                  {lang.name}
                </h4>
                <p className="text-sm text-gray-600 mb-4">{lang.level}</p>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className="bg-blue-600 h-2 rounded-full transition-all duration-500"
                    style={{ width: `${lang.proficiency}%` }}
                  ></div>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Languages;
