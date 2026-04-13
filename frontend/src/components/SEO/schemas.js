export const getOrganizationSchema = (locale) => {
  const isIreland = locale === 'en-ie';
  
  return {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Sabit Burak Cebeci - Process Safety Consultant",
    "image": "https://customer-assets.emergentagent.com/job_ebec55f7-c812-4792-86fc-6db1e6d3ab72/artifacts/k6hhn75q_Sabit%203.jpg",
    "description": isIreland 
      ? "Expert SEVESO and ATEX consultancy for pharmaceutical and chemical industries in Ireland"
      : "Consulenza esperta SEVESO e ATEX per industrie farmaceutiche e chimiche",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "37 Wellington Place",
      "addressLocality": "Dublin",
      "postalCode": "D04 A8N0",
      "addressCountry": "IE"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 53.3329,
      "longitude": -6.2423
    },
    "url": `https://sabitcebeci.com/${locale}/`,
    "telephone": "+353830842944",
    "email": "sabitburakcebeci@gmail.com",
    "priceRange": "€€€",
    "areaServed": [
      { "@type": "Country", "name": "Ireland" },
      { "@type": "Country", "name": "Italy" },
      { "@type": "Country", "name": "European Union" }
    ],
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "Process Safety Services",
      "itemListElement": [
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": isIreland ? "SEVESO Consultancy" : "Consulenza SEVESO"
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": isIreland ? "ATEX Compliance" : "Conformità ATEX"
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": isIreland ? "Explosion Protection" : "Protezione Esplosioni"
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": isIreland ? "Process Safety Management" : "Gestione Sicurezza Processo"
          }
        }
      ]
    }
  };
};

export const getPersonSchema = () => {
  return {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Sabit Burak Cebeci",
    "jobTitle": "Senior Process Safety Consultant",
    "image": "https://customer-assets.emergentagent.com/job_ebec55f7-c812-4792-86fc-6db1e6d3ab72/artifacts/k6hhn75q_Sabit%203.jpg",
    "url": "https://sabitcebeci.com",
    "sameAs": [
      "https://www.linkedin.com/in/sbtbrkcbc/"
    ],
    "email": "sabitburakcebeci@gmail.com",
    "telephone": "+353830842944",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Dublin",
      "addressCountry": "IE"
    },
    "alumniOf": [
      {
        "@type": "EducationalOrganization",
        "name": "Ondokuz Mayıs University"
      }
    ],
    "hasCredential": [
      {
        "@type": "EducationalOccupationalCredential",
        "name": "Master's Degree in Occupational Health & Safety"
      },
      {
        "@type": "EducationalOccupationalCredential",
        "name": "B.Sc. Environmental Engineering"
      }
    ],
    "knowsAbout": [
      "SEVESO Directive",
      "ATEX Compliance",
      "Process Safety Management",
      "Explosion Protection",
      "HAZOP Studies",
      "LOPA Analysis"
    ]
  };
};

export const getServiceSchema = (service, locale) => {
  const isIreland = locale === 'en-ie';
  
  return {
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": service.title,
    "name": service.title,
    "description": service.description,
    "provider": {
      "@type": "Person",
      "name": "Sabit Burak Cebeci",
      "jobTitle": "Senior Process Safety Consultant"
    },
    "areaServed": {
      "@type": "Country",
      "name": isIreland ? "Ireland" : "Italy"
    },
    "url": `https://sabitcebeci.com/${locale}/services/${service.slug}`
  };
};

export const getBreadcrumbSchema = (items) => {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": items.map((item, index) => ({
      "@type": "ListItem",
      "position": index + 1,
      "name": item.name,
      "item": item.url
    }))
  };
};