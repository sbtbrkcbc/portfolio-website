import React, { createContext, useContext } from 'react';
import { useParams } from 'react-router-dom';
import { enIE } from '../locales/en-ie';
import { itIT } from '../locales/it-it';
import { trTR } from '../locales/tr-tr';
import { deDE } from '../locales/de-de';
import { frFR } from '../locales/fr-fr';
import { esES } from '../locales/es-es';
import { seSE } from '../locales/se-se';

const LocaleContext = createContext();

const locales = {
  'en-ie': enIE,
  'it-it': itIT,
  'tr-tr': trTR,
  'de-de': deDE,
  'fr-fr': frFR,
  'es-es': esES,
  'se-se': seSE,
  'en': enIE // fallback
};

export const LocaleProvider = ({ children }) => {
  const { locale } = useParams();
  const currentLocale = locale || 'en-ie';
  const t = locales[currentLocale] || locales['en-ie'];

  return (
    <LocaleContext.Provider value={{ locale: currentLocale, t }}>
      {children}
    </LocaleContext.Provider>
  );
};

export const useLocale = () => {
  const context = useContext(LocaleContext);
  if (!context) {
    throw new Error('useLocale must be used within LocaleProvider');
  }
  return context;
};