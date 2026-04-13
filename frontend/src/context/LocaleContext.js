import React, { createContext, useContext } from 'react';
import { useParams } from 'react-router-dom';
import { enIE } from '../locales/en-ie';
import { itIT } from '../locales/it-it';

const LocaleContext = createContext();

const locales = {
  'en-ie': enIE,
  'it-it': itIT,
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