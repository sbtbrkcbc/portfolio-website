import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import { CheckCircle2 } from 'lucide-react';
import { Card } from './ui/card';

const About = () => {
  const { t } = useLanguage();

  return (
    <section id="about" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            {t.about.title}
          </h2>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <p className="text-lg text-gray-700 leading-relaxed mb-6">
              {t.about.description}
            </p>
          </div>

          <Card className="p-8 bg-gradient-to-br from-blue-50 to-indigo-50 border-none shadow-lg">
            <h3 className="text-xl font-bold text-gray-900 mb-6">Key Competencies</h3>
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
  );
};

export default About;