import React from 'react';
import { Helmet } from 'react-helmet-async';
import { useLocale } from '../../context/LocaleContext';

const SEOHead = ({ 
  title, 
  description, 
  keywords,
  canonical,
  schema,
  noindex = false 
}) => {
  const { locale, t } = useLocale();
  
  const baseUrl = process.env.REACT_APP_SITE_URL || 'https://sabitcebeci.com';
  const currentPath = window.location.pathname;
  
  // Generate hreflang URLs
  const getAlternateUrl = (targetLocale) => {
    const pathWithoutLocale = currentPath.replace(`/${locale}`, '');
    return `${baseUrl}/${targetLocale}${pathWithoutLocale}`;
  };
  
  const pageTitle = title || t.meta.siteTitle;
  const pageDescription = description || t.meta.siteDescription;
  const pageKeywords = keywords || t.meta.keywords;
  const canonicalUrl = canonical || `${baseUrl}${currentPath}`;

  return (
    <Helmet>
      {/* Basic Meta Tags */}
      <title>{pageTitle}</title>
      <meta name="description" content={pageDescription} />
      <meta name="keywords" content={pageKeywords} />
      
      {/* Canonical */}
      <link rel="canonical" href={canonicalUrl} />
      
      {/* Hreflang */}
      <link rel="alternate" hrefLang="en-IE" href={getAlternateUrl('en-ie')} />
      <link rel="alternate" hrefLang="it-IT" href={getAlternateUrl('it-it')} />
      <link rel="alternate" hrefLang="en" href={getAlternateUrl('en')} />
      <link rel="alternate" hrefLang="x-default" href={getAlternateUrl('en')} />
      
      {/* Open Graph */}
      <meta property="og:title" content={pageTitle} />
      <meta property="og:description" content={pageDescription} />
      <meta property="og:url" content={canonicalUrl} />
      <meta property="og:type" content="website" />
      <meta property="og:locale" content={locale === 'en-ie' ? 'en_IE' : locale === 'it-it' ? 'it_IT' : 'en'} />
      <meta property="og:image" content="https://customer-assets.emergentagent.com/job_ebec55f7-c812-4792-86fc-6db1e6d3ab72/artifacts/k6hhn75q_Sabit%203.jpg" />
      
      {/* Twitter Card */}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={pageTitle} />
      <meta name="twitter:description" content={pageDescription} />
      
      {/* Robots */}
      {noindex && <meta name="robots" content="noindex,nofollow" />}
      
      {/* Language */}
      <meta httpEquiv="content-language" content={locale} />
      <html lang={locale} />
      
      {/* Schema.org JSON-LD */}
      {schema && (
        <script type="application/ld+json">
          {JSON.stringify(schema)}
        </script>
      )}
    </Helmet>
  );
};

export default SEOHead;