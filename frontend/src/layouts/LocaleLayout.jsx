import React from 'react';
import { Outlet } from 'react-router-dom';
import Header from '../components/Locale/Header';
import Footer from '../components/Locale/Footer';

const LocaleLayout = () => {
  return (
    <>
      <Header />
      <main>
        <Outlet />
      </main>
      <Footer />
    </>
  );
};

export default LocaleLayout;