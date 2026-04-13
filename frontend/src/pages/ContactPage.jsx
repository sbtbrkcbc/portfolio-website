import React, { useState } from 'react';
import { useLocale } from '../context/LocaleContext';
import SEOHead from '../components/SEO/SEOHead';
import { Mail, MapPin, Clock, Send } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Textarea } from '../components/ui/textarea';
import { toast } from '../hooks/use-toast';

const ContactPage = () => {
  const { locale, t } = useLocale();
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    company: '',
    message: ''
  });
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!formData.name || !formData.email || !formData.message) {
      toast({
        title: 'Error',
        description: t.contact.form.error,
        variant: 'destructive'
      });
      return;
    }

    setLoading(true);
    try {
      const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
      const response = await fetch(`${BACKEND_URL}/api/contact`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...formData, language: locale })
      });

      const data = await response.json();

      if (data.success) {
        toast({ title: 'Success', description: t.contact.form.success });
        setFormData({ name: '', email: '', phone: '', company: '', message: '' });
      } else {
        throw new Error(data.message);
      }
    } catch (error) {
      toast({
        title: 'Error',
        description: 'Failed to send message. Please try again.',
        variant: 'destructive'
      });
    } finally {
      setLoading(false);
    }
  };

  const pageTitle = locale === 'it-it'
    ? 'Contattaci | Consulenza SEVESO e ATEX'
    : 'Contact Us | SEVESO & ATEX Consultancy';

  return (
    <>
      <SEOHead
        title={pageTitle}
        description={t.contact.description}
      />

      <section className="pt-24 pb-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">{t.contact.title}</h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">{t.contact.subtitle}</p>
          </div>

          <div className="grid lg:grid-cols-2 gap-12 max-w-6xl mx-auto">
            <div className="space-y-6">
              <Card className="p-6 bg-white border-gray-200 hover:shadow-lg transition-shadow duration-300">
                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Mail className="h-6 w-6 text-blue-600" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-gray-900 mb-1">{t.contact.info.email}</h3>
                    <a href="mailto:sabitburakcebeci@gmail.com" className="text-blue-600 hover:text-blue-700 font-medium">
                      sabitburakcebeci@gmail.com
                    </a>
                  </div>
                </div>
              </Card>

              <Card className="p-6 bg-white border-gray-200 hover:shadow-lg transition-shadow duration-300">
                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <MapPin className="h-6 w-6 text-gray-600" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-gray-900 mb-1">{t.contact.info.address}</h3>
                    <p className="text-gray-600">Dublin, Ireland</p>
                    <p className="text-sm text-gray-500 mt-2">{t.contact.serviceAreas}</p>
                  </div>
                </div>
              </Card>

              <Card className="p-6 bg-white border-gray-200 hover:shadow-lg transition-shadow duration-300">
                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Clock className="h-6 w-6 text-green-600" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-gray-900 mb-1">{t.contact.info.hours}</h3>
                    <p className="text-gray-600">{t.contact.info.hoursText}</p>
                  </div>
                </div>
              </Card>
            </div>

            <Card className="p-8 bg-white border-gray-200">
              <h2 className="text-2xl font-bold text-gray-900 mb-6">{t.contact.form.name ? t.contact.form.name : 'Send Message'}</h2>
              <form onSubmit={handleSubmit} className="space-y-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">{t.contact.form.name}</label>
                  <Input
                    type="text"
                    value={formData.name}
                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                    placeholder={t.contact.form.name}
                    required
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">{t.contact.form.email}</label>
                  <Input
                    type="email"
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    placeholder={t.contact.form.email}
                    required
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">{t.contact.form.phone}</label>
                  <Input
                    type="tel"
                    value={formData.phone}
                    onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                    placeholder={t.contact.form.phone}
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">{t.contact.form.company}</label>
                  <Input
                    type="text"
                    value={formData.company}
                    onChange={(e) => setFormData({ ...formData, company: e.target.value })}
                    placeholder={t.contact.form.company}
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">{t.contact.form.message}</label>
                  <Textarea
                    value={formData.message}
                    onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                    placeholder={t.contact.form.message}
                    className="min-h-32"
                    required
                  />
                </div>

                <Button
                  type="submit"
                  size="lg"
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white"
                  disabled={loading}
                >
                  {loading ? (
                    <span>{locale === 'it-it' ? 'Invio...' : 'Sending...'}</span>
                  ) : (
                    <>
                      <Send className="h-4 w-4 mr-2" />
                      {t.contact.form.submit}
                    </>
                  )}
                </Button>
              </form>
            </Card>
          </div>
        </div>
      </section>
    </>
  );
};

export default ContactPage;