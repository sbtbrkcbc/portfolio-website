import React from 'react';
import { Helmet } from 'react-helmet-async';
import { useLocale } from '../context/LocaleContext';
import { Briefcase, Calendar, MapPin } from 'lucide-react';

const ExperiencePage = () => {
  const { t, locale } = useLocale();
  const experiences = t?.experience?.items || [];
  
  const pageTitle = t?.experience?.meta?.title 
    ? `${t.experience.meta.title} | ${t?.meta?.siteTitle || ''}` 
    : 'Professional Experience';
  const pageDescription = t?.experience?.meta?.description || '';

  return (
    <>
      <Helmet>
        <title>{pageTitle}</title>
        <meta name="description" content={pageDescription} />
      </Helmet>

      <div className="min-h-screen bg-gradient-to-b from-white to-gray-50">
        {/* Header Section */}
        <section className="bg-gradient-to-r from-[#0F2A4D] to-[#1a3a5f] text-white py-16">
          <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 className="text-4xl sm:text-5xl font-bold mb-4">
              {t.experience?.title}
            </h1>
            <p className="text-lg sm:text-xl text-gray-200 max-w-3xl">
              {t.experience?.subtitle}
            </p>
          </div>
        </section>

        {/* Experience Timeline */}
        <section className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="relative">
            {/* Timeline Line */}
            <div className="hidden md:block absolute left-8 top-0 bottom-0 w-0.5 bg-gradient-to-b from-[#0F2A4D] via-blue-300 to-transparent"></div>

            {/* Experience Cards */}
            <div className="space-y-12">
              {experiences.map((exp, index) => (
                <div key={index} className="relative">
                  {/* Timeline Dot */}
                  <div className="hidden md:block absolute left-8 -translate-x-1/2 w-4 h-4 bg-[#0F2A4D] rounded-full border-4 border-white shadow-lg"></div>

                  {/* Experience Card */}
                  <div className="md:ml-20 bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 p-6 sm:p-8 border border-gray-100">
                    {/* Header */}
                    <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between mb-4 gap-3">
                      <div className="flex-1">
                        <h3 className="text-xl sm:text-2xl font-bold text-[#0F2A4D] mb-2">
                          {exp.title}
                        </h3>
                        <div className="flex items-center text-gray-700 mb-2">
                          <Briefcase className="w-5 h-5 mr-2 text-[#0F2A4D]" />
                          <span className="font-medium">{exp.company}</span>
                        </div>
                      </div>
                      <div className="flex flex-col sm:items-end gap-1 text-sm text-gray-600">
                        <div className="flex items-center">
                          <Calendar className="w-4 h-4 mr-2 text-[#0F2A4D]" />
                          <span className="font-medium">{exp.period}</span>
                        </div>
                        {exp.location && (
                          <div className="flex items-center">
                            <MapPin className="w-4 h-4 mr-2 text-[#0F2A4D]" />
                            <span>{exp.location}</span>
                          </div>
                        )}
                      </div>
                    </div>

                    {/* Description */}
                    {exp.description && (
                      <p className="text-gray-600 mb-4 italic border-l-4 border-[#0F2A4D] pl-4">
                        {exp.description}
                      </p>
                    )}

                    {/* Responsibilities */}
                    <div className="space-y-2">
                      <h4 className="font-semibold text-gray-800 text-sm uppercase tracking-wide mb-3">
                        {t.experience?.responsibilitiesLabel}
                      </h4>
                      <ul className="space-y-2">
                        {exp.responsibilities.map((resp, idx) => (
                          <li key={idx} className="flex items-start text-gray-700">
                            <span className="inline-block w-1.5 h-1.5 bg-[#0F2A4D] rounded-full mt-2 mr-3 flex-shrink-0"></span>
                            <span className="text-sm leading-relaxed">{resp}</span>
                          </li>
                        ))}
                      </ul>
                    </div>

                    {/* Tags/Skills (if applicable) */}
                    {exp.skills && exp.skills.length > 0 && (
                      <div className="mt-6 pt-4 border-t border-gray-200">
                        <div className="flex flex-wrap gap-2">
                          {exp.skills.map((skill, idx) => (
                            <span
                              key={idx}
                              className="px-3 py-1 bg-blue-50 text-[#0F2A4D] text-xs font-medium rounded-full border border-blue-100"
                            >
                              {skill}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Download CV CTA */}
          <div className="mt-16 text-center bg-gradient-to-r from-[#0F2A4D] to-[#1a3a5f] rounded-xl p-8 sm:p-12 shadow-xl">
            <h3 className="text-2xl sm:text-3xl font-bold text-white mb-4">
              {t.experience?.downloadCTA?.title}
            </h3>
            <p className="text-gray-200 mb-6 max-w-2xl mx-auto">
              {t.experience?.downloadCTA?.description}
            </p>
            <a
              href={`${process.env.REACT_APP_BACKEND_URL}/api/cv/${locale.split('-')[0]}`}
              download
              className="inline-flex items-center px-8 py-3 bg-white text-[#0F2A4D] font-semibold rounded-lg hover:bg-gray-100 transition-colors duration-200 shadow-lg"
            >
              <svg
                className="w-5 h-5 mr-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                />
              </svg>
              {t.experience?.downloadCTA?.button}
            </a>
          </div>
        </section>
      </div>
    </>
  );
};

export default ExperiencePage;
