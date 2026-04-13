import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import { MapPin, Award, Download, Linkedin } from 'lucide-react';
import { Button } from './ui/button';

const Hero = () => {
  const { t } = useLanguage();

  const scrollToContact = () => {
    const element = document.getElementById('contact');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleDownloadCV = () => {
    // This will be implemented later with backend
    alert('CV download will be available soon');
  };

  return (
    <section className="pt-24 pb-16 bg-gradient-to-b from-gray-50 to-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="space-y-6">
            <div className="space-y-2">
              <h1 className="text-4xl md:text-5xl font-bold text-gray-900 leading-tight">
                Sabit Burak Cebeci
              </h1>
              <h2 className="text-2xl md:text-3xl font-semibold text-gray-700">
                {t.hero.title}
              </h2>
              <p className="text-lg text-gray-600">
                {t.hero.subtitle}
              </p>
            </div>

            {/* Stats */}
            <div className="flex flex-wrap gap-4">
              <div className="flex items-center space-x-2 bg-white px-4 py-2 rounded-lg shadow-sm border border-gray-200">
                <Award className="h-5 w-5 text-emerald-600" />
                <span className="font-semibold text-gray-900">{t.hero.experience}</span>
              </div>
              <div className="flex items-center space-x-2 bg-white px-4 py-2 rounded-lg shadow-sm border border-gray-200">
                <MapPin className="h-5 w-5 text-emerald-600" />
                <span className="font-medium text-gray-700">{t.hero.location}</span>
              </div>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-wrap gap-4 pt-4">
              <Button
                onClick={scrollToContact}
                size="lg"
                className="bg-emerald-600 hover:bg-emerald-700 text-white"
              >
                {t.hero.cta}
              </Button>
              <Button
                onClick={handleDownloadCV}
                variant="outline"
                size="lg"
                className="border-gray-300 hover:border-emerald-600 hover:text-emerald-600"
              >
                <Download className="h-4 w-4 mr-2" />
                {t.hero.downloadCV}
              </Button>
              <Button
                onClick={() => window.open('https://www.linkedin.com/in/sbtbrkcbc/', '_blank')}
                variant="outline"
                size="lg"
                className="border-gray-300 hover:border-blue-600 hover:text-blue-600"
              >
                <Linkedin className="h-4 w-4 mr-2" />
                LinkedIn
              </Button>
            </div>
          </div>

          {/* Right - Photo */}
          <div className="flex justify-center lg:justify-end">
            <div className="relative">
              <div className="w-72 h-72 md:w-96 md:h-96 rounded-2xl overflow-hidden shadow-2xl border-4 border-white">
                <img
                  src="https://customer-assets.emergentagent.com/job_ebec55f7-c812-4792-86fc-6db1e6d3ab72/artifacts/k6hhn75q_Sabit%203.jpg"
                  alt="Sabit Burak Cebeci"
                  className="w-full h-full object-cover"
                />
              </div>
              <div className="absolute -bottom-4 -right-4 w-24 h-24 bg-emerald-600 rounded-2xl opacity-20"></div>
              <div className="absolute -top-4 -left-4 w-24 h-24 bg-blue-600 rounded-2xl opacity-20"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;