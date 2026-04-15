from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
from datetime import datetime

# Register Turkish-compatible font
pdfmetrics.registerFont(TTFont('DejaVu', '/app/backend/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold', '/app/backend/DejaVuSans.ttf'))

# Navy Blue color from website theme
NAVY_BLUE = colors.HexColor('#0F2A4D')
DARK_GRAY = colors.HexColor('#2D3748')
LIGHT_GRAY = colors.HexColor('#E2E8F0')
MED_GRAY = colors.HexColor('#4B5563')

def create_cv(filename, language='en'):
    """
    Generate ATS-friendly, European standard CV with Turkish character support
    Design based on social engineering principles for Process Safety field
    """
    
    # Content in different languages
    content = {
        'en': {
            'name': 'SABIT BURAK CEBECİ',
            'title': 'Risk Consultant | SEVESO & ATEX Specialist',
            'subtitle': 'Environmental & Process Safety Engineering',
            'email': 'sabitburakcebeci@gmail.com',
            'phone': '+353 83 084 2944',
            'location': 'Dublin, Ireland',
            'linkedin': 'linkedin.com/in/sbtbrkcbc',
            
            'profile_title': 'PROFESSIONAL PROFILE',
            'profile': 'Senior Environmental Engineer and Process Safety Specialist with 13+ years of progressive experience in SEVESO compliance, ATEX regulations, and explosion protection for Upper Tier Seveso sites. Proven expertise in developing Process Safety Management systems, conducting HAZOP studies, and delivering risk-based consultancy for pharmaceutical and chemical industries. Strong technical background in consequence modelling (DNV PHAST, Gexcon), regulatory compliance (COMAH, EU Directives), and safety report preparation. Currently serving high-profile international clients including Intel and leading pharmaceutical manufacturers.',
            
            'competencies_title': 'CORE COMPETENCIES',
            'competencies': [
                ['SEVESO Directive Compliance', 'ATEX Equipment Certification & Inspection', 'Explosion Protection Documentation'],
                ['Process Safety Management (PSM)', 'HAZOP Studies & LOPA Analysis', 'COMAH Regulations 2015'],
                ['DNV PHAST Consequence Modelling', 'Risk Assessment & Mitigation', 'Safety Report Preparation'],
                ['ISO 60079, ISO 45001, ISO 14001', 'Emergency Response Planning', 'Technical Report Writing']
            ],
            
            'certifications_title': 'PROFESSIONAL CERTIFICATIONS & TRAINING',
            'certifications': [
                'Technical Report Writing – Engineers Ireland (Apr 2024)',
                'DNV SA-01 Consequence Modelling Software Training – DNV (Jan 2024)',
                'Effects/Risk & Risk Curves Modelling Software – Gexcon (Nov 2023)',
                'LOPA - Layer of Protection Analysis – CCPS',
                'HAZOP Training Certification – Seyir Akademi (2019)',
                'ATEX Equipment Certification – Seyir Akademi (2019)',
                'Explosion Protection Document Training – Seyir Akademi (2019)',
                'ISO 60079 Standards Training – Seyir Akademi',
                'ISO 45001:2018 OHSMS Certification',
                'ISO 14001 Environmental Management Systems'
            ],
            
            'experience_title': 'PROFESSIONAL EXPERIENCE',
            'experience': [
                {
                    'title': 'Senior Risk Consultant',
                    'company': 'AWN Consulting Ltd.',
                    'location': 'Dublin, Ireland',
                    'period': 'August 2023 – Present',
                    'responsibilities': [
                        'Provide process safety and environmental risk consultancy for Upper Tier Seveso sites across Ireland and Europe',
                        'Conduct SEVESO consultancy services including safety report preparation, significant modification assessments, and regulatory compliance reviews',
                        'Prepare and update Explosion Protection Documents (EPD) using DNV PHAST consequence modelling software',
                        'Support high-profile clients including Intel and pharmaceutical manufacturers in achieving COMAH compliance',
                        'Deliver technical report writing and regulatory submission support to Irish EPA and HSA'
                    ]
                },
                {
                    'title': 'Process Safety Engineer',
                    'company': 'Guerbet (Pharmaceutical Manufacturing)',
                    'location': 'Dublin, Ireland',
                    'period': 'August 2022 – June 2023',
                    'responsibilities': [
                        'Developed and led the Process Safety Management System for an Upper Tier Seveso site',
                        'Conducted significant modification assessments under COMAH Regulations 2015',
                        'Updated and maintained site Safety Report and Explosion Protection Document',
                        'Led Process Safety Risk Assessments including HAZOP and LOPA studies',
                        'Managed Management of Change (MoC) procedures for plant, process, and system modifications',
                        'Provided ATEX inspection reviews and EHS support for capital expenditure projects',
                        'Assisted Emergency Response Team management and emergency planning activities'
                    ]
                },
                {
                    'title': 'Safety Specialist & Environmental Engineer',
                    'company': 'Seyir Akademi (Leading Process Safety Consultancy)',
                    'location': 'Istanbul, Turkey',
                    'period': 'February 2019 – October 2021',
                    'responsibilities': [
                        'Delivered SEVESO consultancy for 30+ clients in chemical production, pharmaceuticals, and agricultural chemicals',
                        'Prepared Explosion Protection Documents and Safety Reports applying European standards',
                        'Conducted ATEX equipment site audits, inspections, and hazardous area classification reviews',
                        'Performed occupational safety field audits and comprehensive risk assessments',
                        'Managed explosion modeling and consequence analysis for major hazard sites',
                        'Applied ISO 60079 standards for explosive atmosphere equipment selection'
                    ]
                },
                {
                    'title': 'Safety Specialist',
                    'company': 'Momentum OSGB',
                    'location': 'Turkey',
                    'period': 'September 2017 – February 2019',
                    'responsibilities': [
                        'Provided occupational safety expertise consultancy across multiple industries including chemical plants, construction, manufacturing, and healthcare',
                        'Conducted environmental risk assessments and safety compliance audits',
                        'Developed safety management systems for chemical storage and processing facilities'
                    ]
                },
                {
                    'title': 'Safety Measurement & Emission Reporting Specialist',
                    'company': 'Testmer Measurement And Testing Services Ltd.',
                    'location': 'Turkey',
                    'period': 'July 2016 – September 2017',
                    'responsibilities': [
                        'Conducted occupational health and safety environment measurements and exposure assessments',
                        'Prepared emission and odour measurement reports in accordance with international standards',
                        'Applied scientific calculation methods and quality management systems to reporting processes'
                    ]
                },
                {
                    'title': 'Environmental Engineer',
                    'company': 'Metreküp Treatment Technologies',
                    'location': 'Turkey',
                    'period': 'April 2014 – April 2015',
                    'responsibilities': [
                        'Designed wastewater treatment plants for industrial facilities',
                        'Provided water treatment consultancy for 13 factories across various industries',
                        'Conducted in-water analysis, reporting, and on-site construction management'
                    ]
                }
            ],
            
            'education_title': 'EDUCATION',
            'education': [
                {
                    'degree': "Master's Degree (Thesis)",
                    'field': 'Occupational Health and Safety',
                    'institution': 'Üsküdar University, Health Sciences Institute',
                    'location': 'Istanbul, Turkey',
                    'period': 'September 2018 – February 2020',
                    'thesis': 'Thesis: "The Necessity To Use Machine Safety Equipment Instead Of Safety Equipment Used In Passenger Elevators And Relevance Of Risk Assessment ISO Standards Applicability Comparison"'
                },
                {
                    'degree': "Master's Degree (Non-Thesis)",
                    'field': 'Occupational Health and Safety',
                    'institution': 'Yeni Yüzyıl University, Health Sciences Institute',
                    'location': 'Istanbul, Turkey',
                    'period': 'September 2016 – February 2017',
                    'thesis': None
                },
                {
                    'degree': 'Bachelor of Science',
                    'field': 'Environmental Engineering (with 1 Year English Preparatory Class)',
                    'institution': 'Ondokuz Mayıs University, Faculty of Engineering',
                    'location': 'Samsun, Turkey',
                    'period': 'September 2008 – July 2013',
                    'thesis': None
                }
            ],
            
            'memberships_title': 'PROFESSIONAL MEMBERSHIPS',
            'memberships': [
                'American Institute of Chemical Engineers (AIChE)',
                'Engineers Ireland',
                'Chamber of Environmental Engineers, Turkey'
            ],
            
            'skills_title': 'TECHNICAL SKILLS & SOFTWARE',
            'skills': [
                ['Process Safety', 'DNV PHAST, Gexcon Risk Modelling, HAZOP Facilitation, LOPA Analysis, Safety Report Writing'],
                ['Regulatory Compliance', 'SEVESO Directive III, COMAH Regulations 2015, ATEX Directive 2014/34/EU, ISO 60079, ISO 45001, ISO 14001'],
                ['Engineering', 'AutoCAD 2D/3D, Rhino 3D, Wastewater Treatment Design, Explosion Protection Systems'],
                ['Languages', 'Turkish (Native), English (Professional Working Proficiency)']
            ]
        },
        'it': {
            'name': 'SABIT BURAK CEBECİ',
            'title': 'Consulente del Rischio | Specialista SEVESO e ATEX',
            'subtitle': 'Ingegneria Ambientale e Sicurezza di Processo',
            'email': 'sabitburakcebeci@gmail.com',
            'phone': '+353 83 084 2944',
            'location': 'Dublino, Irlanda',
            'linkedin': 'linkedin.com/in/sbtbrkcbc',
            
            'profile_title': 'PROFILO PROFESSIONALE',
            'profile': 'Ingegnere Ambientale Senior e Specialista della Sicurezza di Processo con oltre 13 anni di esperienza progressiva in conformità SEVESO, normative ATEX e protezione dalle esplosioni per siti Seveso di Soglia Superiore. Comprovata competenza nello sviluppo di sistemi di gestione della sicurezza di processo, conduzione di studi HAZOP e fornitura di consulenza basata sul rischio per le industrie farmaceutiche e chimiche. Solida formazione tecnica nella modellazione delle conseguenze (DNV PHAST, Gexcon), conformità normativa (COMAH, Direttive UE) e preparazione di rapporti di sicurezza. Attualmente al servizio di clienti internazionali di alto profilo tra cui Intel e principali produttori farmaceutici.',
            
            'competencies_title': 'COMPETENZE PRINCIPALI',
            'competencies': [
                ['Conformità Direttiva SEVESO', 'Certificazione e Ispezione Apparecchiature ATEX', 'Documentazione Protezione Esplosioni'],
                ['Gestione Sicurezza Processo (PSM)', 'Studi HAZOP e Analisi LOPA', 'Regolamenti COMAH 2015'],
                ['Modellazione Conseguenze DNV PHAST', 'Valutazione e Mitigazione Rischio', 'Preparazione Rapporti Sicurezza'],
                ['ISO 60079, ISO 45001, ISO 14001', 'Pianificazione Risposta Emergenze', 'Redazione Report Tecnici']
            ],
            
            'certifications_title': 'CERTIFICAZIONI E FORMAZIONE PROFESSIONALE',
            'certifications': [
                'Redazione Report Tecnici – Engineers Ireland (Apr 2024)',
                'Formazione Software Modellazione Conseguenze DNV SA-01 – DNV (Gen 2024)',
                'Software Modellazione Effetti/Rischio e Curve Rischio – Gexcon (Nov 2023)',
                'LOPA - Layer of Protection Analysis – CCPS',
                'Certificazione Formazione HAZOP – Seyir Akademi (2019)',
                'Certificazione Apparecchiature ATEX – Seyir Akademi (2019)',
                'Formazione Documento Protezione Esplosioni – Seyir Akademi (2019)',
                'Formazione Standard ISO 60079 – Seyir Akademi',
                'Certificazione ISO 45001:2018 SGSSL',
                'Sistemi Gestione Ambientale ISO 14001'
            ],
            
            'experience_title': 'ESPERIENZA PROFESSIONALE',
            'experience': [
                {
                    'title': 'Consulente del Rischio',
                    'company': 'AWN Consulting Ltd.',
                    'location': 'Dublino, Irlanda',
                    'period': 'Agosto 2023 – Presente',
                    'responsibilities': [
                        'Fornisco consulenza sulla sicurezza di processo e rischio ambientale per siti Seveso di Soglia Superiore in Irlanda e Europa',
                        'Conduco servizi di consulenza SEVESO inclusa preparazione rapporti di sicurezza, valutazioni modifiche significative e revisioni conformità normativa',
                        'Preparo e aggiorno Documenti di Protezione Esplosioni (EPD) utilizzando software modellazione conseguenze DNV PHAST',
                        'Supporto clienti di alto profilo inclusi Intel e produttori farmaceutici nel raggiungimento conformità COMAH',
                        'Fornisco redazione report tecnici e supporto presentazioni normative a EPA e HSA irlandesi'
                    ]
                },
                {
                    'title': 'Ingegnere Sicurezza di Processo',
                    'company': 'Guerbet (Produzione Farmaceutica)',
                    'location': 'Dublino, Irlanda',
                    'period': 'Agosto 2022 – Giugno 2023',
                    'responsibilities': [
                        'Sviluppato e guidato il Sistema di Gestione Sicurezza di Processo per sito Seveso Soglia Superiore',
                        'Condotto valutazioni modifiche significative secondo Regolamenti COMAH 2015',
                        'Aggiornato e mantenuto Rapporto Sicurezza sito e Documento Protezione Esplosioni',
                        'Guidato Valutazioni Rischio Sicurezza Processo inclusi studi HAZOP e LOPA',
                        'Gestito procedure Gestione del Cambiamento (MoC) per modifiche impianto, processo e sistema',
                        'Fornito revisioni ispezioni ATEX e supporto EHS per progetti investimento capitale',
                        'Assistito gestione Team Risposta Emergenze e attività pianificazione emergenze'
                    ]
                },
                {
                    'title': 'Specialista Sicurezza e Ingegnere Ambientale',
                    'company': 'Seyir Akademi (Consulenza Leader Sicurezza Processo)',
                    'location': 'Istanbul, Turchia',
                    'period': 'Febbraio 2019 – Ottobre 2021',
                    'responsibilities': [
                        'Fornita consulenza SEVESO per oltre 30 clienti in produzione chimica, farmaceutica e chimica agricola',
                        'Preparati Documenti Protezione Esplosioni e Rapporti Sicurezza applicando standard europei',
                        'Condotti audit sito apparecchiature ATEX, ispezioni e revisioni classificazione aree pericolose',
                        'Eseguiti audit campo sicurezza occupazionale e valutazioni rischio complete',
                        'Gestita modellazione esplosioni e analisi conseguenze per siti rischio incidente rilevante',
                        'Applicati standard ISO 60079 per selezione apparecchiature atmosfere esplosive'
                    ]
                },
                {
                    'title': 'Specialista Sicurezza',
                    'company': 'Momentum OSGB',
                    'location': 'Turchia',
                    'period': 'Settembre 2017 – Febbraio 2019',
                    'responsibilities': [
                        'Fornita consulenza competenza sicurezza occupazionale attraverso molteplici industrie',
                        'Condotte valutazioni rischio ambientale e audit conformità sicurezza',
                        'Sviluppati sistemi gestione sicurezza per strutture stoccaggio e lavorazione chimica'
                    ]
                },
                {
                    'title': 'Specialista Misurazione Sicurezza e Reporting Emissioni',
                    'company': 'Testmer Measurement And Testing Services Ltd.',
                    'location': 'Turchia',
                    'period': 'Luglio 2016 – Settembre 2017',
                    'responsibilities': [
                        'Condotte misurazioni ambiente salute e sicurezza occupazionale e valutazioni esposizione',
                        'Preparati report misurazione emissioni e odori secondo standard internazionali'
                    ]
                },
                {
                    'title': 'Ingegnere Ambientale',
                    'company': 'Metreküp Treatment Technologies',
                    'location': 'Turchia',
                    'period': 'Aprile 2014 – Aprile 2015',
                    'responsibilities': [
                        'Progettati impianti trattamento acque reflue per strutture industriali',
                        'Fornita consulenza trattamento acque per 13 fabbriche attraverso varie industrie'
                    ]
                }
            ],
            
            'education_title': 'FORMAZIONE',
            'education': [
                {
                    'degree': 'Master (Tesi)',
                    'field': 'Salute e Sicurezza Occupazionale',
                    'institution': 'Üsküdar University, Istituto Scienze Salute',
                    'location': 'Istanbul, Turchia',
                    'period': 'Settembre 2018 – Febbraio 2020',
                    'thesis': 'Tesi: "La Necessità di Utilizzare Apparecchiature Sicurezza Macchine Invece di Apparecchiature Sicurezza Utilizzate negli Ascensori Passeggeri e Rilevanza Confronto Applicabilità Standard ISO Valutazione Rischio"'
                },
                {
                    'degree': 'Master (Senza Tesi)',
                    'field': 'Salute e Sicurezza Occupazionale',
                    'institution': 'Yeni Yüzyıl University, Istituto Scienze Salute',
                    'location': 'Istanbul, Turchia',
                    'period': 'Settembre 2016 – Febbraio 2017',
                    'thesis': None
                },
                {
                    'degree': 'Laurea Triennale',
                    'field': 'Ingegneria Ambientale (con 1 Anno Corso Preparatorio Inglese)',
                    'institution': 'Ondokuz Mayıs University, Facoltà Ingegneria',
                    'location': 'Samsun, Turchia',
                    'period': 'Settembre 2008 – Luglio 2013',
                    'thesis': None
                }
            ],
            
            'memberships_title': 'AFFILIAZIONI PROFESSIONALI',
            'memberships': [
                'American Institute of Chemical Engineers (AIChE)',
                'Engineers Ireland',
                'Camera Ingegneri Ambientali, Turchia'
            ],
            
            'skills_title': 'COMPETENZE TECNICHE E SOFTWARE',
            'skills': [
                ['Sicurezza Processo', 'DNV PHAST, Modellazione Rischio Gexcon, Facilitazione HAZOP, Analisi LOPA, Redazione Rapporti Sicurezza'],
                ['Conformità Normativa', 'Direttiva SEVESO III, Regolamenti COMAH 2015, Direttiva ATEX 2014/34/UE, ISO 60079, ISO 45001, ISO 14001'],
                ['Ingegneria', 'AutoCAD 2D/3D, Rhino 3D, Progettazione Trattamento Acque Reflue, Sistemi Protezione Esplosioni'],
                ['Lingue', 'Turco (Madrelingua), Inglese (Competenza Professionale)']
            ]
        },
        'tr': {
            'name': 'SABİT BURAK CEBECİ',
            'title': 'Risk Danışmanı | SEVESO ve ATEX Uzmanı',
            'subtitle': 'Çevre ve Proses Güvenliği Mühendisliği',
            'email': 'sabitburakcebeci@gmail.com',
            'phone': '+353 83 084 2944',
            'location': 'Dublin, İrlanda',
            'linkedin': 'linkedin.com/in/sbtbrkcbc',
            
            'profile_title': 'PROFESYONELÖZGEÇMİŞ',
            'profile': 'Üst Kademe Seveso tesisleri için SEVESO uyumluluğu, ATEX yönetmelikleri ve patlama koruması konularında 13+ yıllık ilerleyici deneyime sahip Kıdemli Çevre Mühendisi ve Proses Güvenliği Uzmanı. Proses Güvenliği Yönetim sistemleri geliştirme, HAZOP çalışmaları yürütme ve ilaç ve kimya endüstrileri için risk tabanlı danışmanlık sunma konusunda kanıtlanmış uzmanlık. Sonuç modelleme (DNV PHAST, Gexcon), mevzuat uyumluluğu (COMAH, AB Direktifleri) ve güvenlik raporu hazırlama konularında güçlü teknik altyapı. Şu anda Intel ve önde gelen ilaç üreticileri dahil olmak üzere yüksek profilli uluslararası müşterilere hizmet vermektedir.',
            
            'competencies_title': 'TEMEL YETKİNLİKLER',
            'competencies': [
                ['SEVESO Direktifi Uyumluluğu', 'ATEX Ekipman Sertifikasyonu ve Denetimi', 'Patlama Koruması Dokümantasyonu'],
                ['Proses Güvenliği Yönetimi (PSM)', 'HAZOP Çalışmaları ve LOPA Analizi', 'COMAH Yönetmelikleri 2015'],
                ['DNV PHAST Sonuç Modelleme', 'Risk Değerlendirme ve Azaltma', 'Güvenlik Raporu Hazırlama'],
                ['ISO 60079, ISO 45001, ISO 14001', 'Acil Durum Müdahale Planlaması', 'Teknik Rapor Yazımı']
            ],
            
            'certifications_title': 'PROFESYONEL SERTİFİKALAR VE EĞİTİMLER',
            'certifications': [
                'Teknik Rapor Yazımı – Engineers Ireland (Nis 2024)',
                'DNV SA-01 Sonuç Modelleme Yazılımı Eğitimi – DNV (Oca 2024)',
                'Etkiler/Risk ve Risk Eğrileri Modelleme Yazılımı – Gexcon (Kas 2023)',
                'LOPA - Layer of Protection Analysis – CCPS',
                'HAZOP Eğitim Sertifikası – Seyir Akademi (2019)',
                'ATEX Ekipman Sertifikasyonu – Seyir Akademi (2019)',
                'Patlama Koruması Dokümanı Eğitimi – Seyir Akademi (2019)',
                'ISO 60079 Standartları Eğitimi – Seyir Akademi',
                'ISO 45001:2018 İSGYS Sertifikasyonu',
                'ISO 14001 Çevre Yönetim Sistemleri'
            ],
            
            'experience_title': 'PROFESYONEL DENEYİM',
            'experience': [
                {
                    'title': 'Kıdemli Risk Danışmanı',
                    'company': 'AWN Consulting Ltd.',
                    'location': 'Dublin, İrlanda',
                    'period': 'Ağustos 2023 – Halen',
                    'responsibilities': [
                        'İrlanda ve Avrupa genelindeki Üst Kademe Seveso tesisleri için proses güvenliği ve çevresel risk danışmanlığı sağlama',
                        'Güvenlik raporu hazırlama, önemli modifikasyon değerlendirmeleri ve mevzuat uyumluluk incelemeleri dahil SEVESO danışmanlık hizmetleri yürütme',
                        'DNV PHAST sonuç modelleme yazılımı kullanarak Patlama Koruması Dokümanları (EPD) hazırlama ve güncelleme',
                        'Intel ve ilaç üreticileri dahil yüksek profilli müşterilere COMAH uyumluluğuna ulaşmada destek sağlama',
                        'İrlanda EPA ve HSA\'ya teknik rapor yazımı ve mevzuat başvuru desteği sunma'
                    ]
                },
                {
                    'title': 'Proses Güvenliği Mühendisi',
                    'company': 'Guerbet (İlaç Üretimi)',
                    'location': 'Dublin, İrlanda',
                    'period': 'Ağustos 2022 – Haziran 2023',
                    'responsibilities': [
                        'Üst Kademe Seveso tesisi için Proses Güvenliği Yönetim Sistemi geliştirme ve yönetme',
                        'COMAH Yönetmelikleri 2015 kapsamında önemli modifikasyon değerlendirmeleri yürütme',
                        'Tesis Güvenlik Raporu ve Patlama Koruması Dokümanını güncelleme ve sürdürme',
                        'HAZOP ve LOPA çalışmaları dahil Proses Güvenliği Risk Değerlendirmelerini yönetme',
                        'Tesis, proses ve sistem modifikasyonları için Değişiklik Yönetimi (MoC) prosedürlerini yönetme',
                        'ATEX denetim incelemeleri ve sermaye harcama projeleri için EHS desteği sağlama',
                        'Acil Durum Müdahale Ekibi yönetimi ve acil durum planlama faaliyetlerine yardımcı olma'
                    ]
                },
                {
                    'title': 'Güvenlik Uzmanı ve Çevre Mühendisi',
                    'company': 'Seyir Akademi (Önde Gelen Proses Güvenliği Danışmanlığı)',
                    'location': 'İstanbul, Türkiye',
                    'period': 'Şubat 2019 – Ekim 2021',
                    'responsibilities': [
                        'Kimyasal üretim, ilaç ve tarımsal kimyasallar alanında 30+ müşteri için SEVESO danışmanlığı sunma',
                        'Avrupa standartlarını uygulayarak Patlama Koruması Dokümanları ve Güvenlik Raporları hazırlama',
                        'ATEX ekipman saha denetimleri, teftişler ve tehlikeli alan sınıflandırma incelemeleri yürütme',
                        'İş güvenliği saha denetimleri ve kapsamlı risk değerlendirmeleri gerçekleştirme',
                        'Büyük tehlike tesisleri için patlama modelleme ve sonuç analizi yönetme',
                        'Patlayıcı atmosfer ekipman seçimi için ISO 60079 standartlarını uygulama'
                    ]
                },
                {
                    'title': 'Güvenlik Uzmanı',
                    'company': 'Momentum OSGB',
                    'location': 'Türkiye',
                    'period': 'Eylül 2017 – Şubat 2019',
                    'responsibilities': [
                        'Kimyasal tesisler, inşaat, imalat ve sağlık dahil birçok sektörde iş güvenliği uzmanlık danışmanlığı sağlama',
                        'Çevresel risk değerlendirmeleri ve güvenlik uyumluluk denetimleri yürütme',
                        'Kimyasal depolama ve işleme tesisleri için güvenlik yönetim sistemleri geliştirme'
                    ]
                },
                {
                    'title': 'Güvenlik Ölçümü ve Emisyon Raporlama Uzmanı',
                    'company': 'Testmer Ölçüm ve Test Hizmetleri Ltd.',
                    'location': 'Türkiye',
                    'period': 'Temmuz 2016 – Eylül 2017',
                    'responsibilities': [
                        'İş sağlığı ve güvenliği çevre ölçümleri ve maruziyet değerlendirmeleri yürütme',
                        'Uluslararası standartlara uygun emisyon ve koku ölçümü raporları hazırlama'
                    ]
                },
                {
                    'title': 'Çevre Mühendisi',
                    'company': 'Metreküp Arıtma Teknolojileri',
                    'location': 'Türkiye',
                    'period': 'Nisan 2014 – Nisan 2015',
                    'responsibilities': [
                        'Endüstriyel tesisler için atık su arıtma tesisleri tasarlama',
                        'Çeşitli sektörlerdeki 13 fabrika için su arıtma danışmanlığı sağlama'
                    ]
                }
            ],
            
            'education_title': 'EĞİTİM',
            'education': [
                {
                    'degree': 'Yüksek Lisans (Tezli)',
                    'field': 'İş Sağlığı ve Güvenliği',
                    'institution': 'Üsküdar Üniversitesi, Sağlık Bilimleri Enstitüsü',
                    'location': 'İstanbul, Türkiye',
                    'period': 'Eylül 2018 – Şubat 2020',
                    'thesis': 'Tez: "Yolcu Asansörlerinde Kullanılan Güvenlik Ekipmanları Yerine Makine Güvenlik Ekipmanlarının Kullanılma Gerekliliği ve Risk Değerlendirmesi ISO Standartlarının Uygulanabilirlik Karşılaştırması"'
                },
                {
                    'degree': 'Yüksek Lisans (Tezsiz)',
                    'field': 'İş Sağlığı ve Güvenliği',
                    'institution': 'Yeni Yüzyıl Üniversitesi, Sağlık Bilimleri Enstitüsü',
                    'location': 'İstanbul, Türkiye',
                    'period': 'Eylül 2016 – Şubat 2017',
                    'thesis': None
                },
                {
                    'degree': 'Lisans',
                    'field': 'Çevre Mühendisliği (1 Yıl İngilizce Hazırlık ile)',
                    'institution': 'Ondokuz Mayıs Üniversitesi, Mühendislik Fakültesi',
                    'location': 'Samsun, Türkiye',
                    'period': 'Eylül 2008 – Temmuz 2013',
                    'thesis': None
                }
            ],
            
            'memberships_title': 'PROFESYONEL ÜYELİKLER',
            'memberships': [
                'American Institute of Chemical Engineers (AIChE)',
                'Engineers Ireland',
                'Çevre Mühendisleri Odası, Türkiye'
            ],
            
            'skills_title': 'TEKNİK BECERİLER VE YAZILIMLAR',
            'skills': [
                ['Proses Güvenliği', 'DNV PHAST, Gexcon Risk Modelleme, HAZOP Kolaylaştırma, LOPA Analizi, Güvenlik Raporu Yazımı'],
                ['Mevzuat Uyumluluğu', 'SEVESO Direktifi III, COMAH Yönetmelikleri 2015, ATEX Direktifi 2014/34/AB, ISO 60079, ISO 45001, ISO 14001'],
                ['Mühendislik', 'AutoCAD 2D/3D, Rhino 3D, Atık Su Arıtma Tasarımı, Patlama Koruması Sistemleri'],
                ['Diller', 'Türkçe (Anadil), İngilizce (Profesyonel İş Yeterliliği)']
            ]
        },
        'de': {
            'name': 'SABIT BURAK CEBECİ',
            'title': 'Risikoberater | SEVESO & ATEX Spezialist',
            'subtitle': 'Umwelt- und Prozesssicherheitsingenieurwesen',
            'email': 'sabitburakcebeci@gmail.com',
            'phone': '+353 83 084 2944',
            'location': 'Dublin, Irland',
            'linkedin': 'linkedin.com/in/sbtbrkcbc',
            
            'profile_title': 'BERUFSPROFIL',
            'profile': 'Senior Umweltingenieur und Prozesssicherheitsspezialist mit über 13 Jahren fortschreitender Erfahrung in SEVESO-Compliance, ATEX-Vorschriften und Explosionsschutz für Seveso-Anlagen der oberen Klasse. Nachgewiesene Expertise in der Entwicklung von Prozesssicherheitsmanagementsystemen, Durchführung von HAZOP-Studien und Bereitstellung risikobasierter Beratung für die Pharma- und Chemieindustrie. Starker technischer Hintergrund in Konsequenzmodellierung (DNV PHAST, Gexcon), regulatorischer Compliance (COMAH, EU-Richtlinien) und Sicherheitsberichtserstellung. Derzeit im Dienst hochkarätiger internationaler Kunden wie Intel und führender Pharmahersteller.',
            
            'competencies_title': 'KERNKOMPETENZEN',
            'competencies': [
                ['SEVESO-Richtlinien-Compliance', 'ATEX-Gerätezertifizierung & Inspektion', 'Explosionsschutzdokumentation'],
                ['Prozesssicherheitsmanagement (PSM)', 'HAZOP-Studien & LOPA-Analyse', 'COMAH-Vorschriften 2015'],
                ['DNV PHAST Konsequenzmodellierung', 'Risikobewertung & Risikominderung', 'Sicherheitsberichtserstellung'],
                ['ISO 60079, ISO 45001, ISO 14001', 'Notfallmaßnahmenplanung', 'Technisches Berichtswesen']
            ],
            
            'certifications_title': 'BERUFSZERTIFIZIERUNGEN & SCHULUNGEN',
            'certifications': [
                'Technisches Berichtswesen – Engineers Ireland (Apr 2024)',
                'DNV SA-01 Konsequenzmodellierungs-Software-Schulung – DNV (Jan 2024)',
                'Effekt-/Risiko- & Risikokurven-Modellierungs-Software – Gexcon (Nov 2023)',
                'LOPA - Layer of Protection Analysis – CCPS',
                'HAZOP-Schulungszertifizierung – Seyir Akademi (2019)',
                'ATEX-Gerätezertifizierung – Seyir Akademi (2019)',
                'Explosionsschutzdokument-Schulung – Seyir Akademi (2019)',
                'ISO 60079 Standards-Schulung – Seyir Akademi',
                'ISO 45001:2018 OHSMS-Zertifizierung',
                'ISO 14001 Umweltmanagementsysteme'
            ],
            
            'experience_title': 'BERUFSERFAHRUNG',
            'experience': [
                {
                    'title': 'Senior Risikoberater',
                    'company': 'AWN Consulting Ltd.',
                    'location': 'Dublin, Irland',
                    'period': 'August 2023 – Heute',
                    'responsibilities': [
                        'Bereitstellung von Prozesssicherheits- und Umweltrisikoberatung für Seveso-Anlagen der oberen Klasse in Irland und Europa',
                        'Durchführung von SEVESO-Beratungsdienstleistungen einschließlich Sicherheitsberichtserstellung, Bewertung wesentlicher Änderungen und regulatorischer Compliance-Überprüfungen',
                        'Erstellung und Aktualisierung von Explosionsschutzdokumenten (EPD) mit DNV PHAST Konsequenzmodellierungs-Software',
                        'Unterstützung hochkarätiger Kunden wie Intel und Pharmahersteller bei der Einhaltung der COMAH-Vorschriften',
                        'Bereitstellung von technischem Berichtswesen und regulatorischer Einreichungsunterstützung für die irische EPA und HSA'
                    ]
                },
                {
                    'title': 'Prozesssicherheitsingenieur',
                    'company': 'Guerbet (Pharmazeutische Fertigung)',
                    'location': 'Dublin, Irland',
                    'period': 'August 2022 – Juni 2023',
                    'responsibilities': [
                        'Entwicklung und Leitung des Prozesssicherheitsmanagementsystems für eine Seveso-Anlage der oberen Klasse',
                        'Durchführung von Bewertungen wesentlicher Änderungen gemäß COMAH-Vorschriften 2015',
                        'Aktualisierung und Wartung des Standort-Sicherheitsberichts und Explosionsschutzdokuments',
                        'Leitung von Prozesssicherheitsrisikobewertungen einschließlich HAZOP- und LOPA-Studien',
                        'Verwaltung von Management of Change (MoC)-Verfahren für Anlagen-, Prozess- und Systemänderungen',
                        'Bereitstellung von ATEX-Inspektionsüberprüfungen und EHS-Unterstützung für Kapitalinvestitionsprojekte',
                        'Unterstützung des Notfallteam-Managements und Notfallplanungsaktivitäten'
                    ]
                },
                {
                    'title': 'Sicherheitsspezialist & Umweltingenieur',
                    'company': 'Seyir Akademi (Führende Prozesssicherheitsberatung)',
                    'location': 'Istanbul, Türkei',
                    'period': 'Februar 2019 – Oktober 2021',
                    'responsibilities': [
                        'SEVESO-Beratung für über 30 Kunden in chemischer Produktion, Pharmazie und Agrarchemie',
                        'Erstellung von Explosionsschutzdokumenten und Sicherheitsberichten nach europäischen Standards',
                        'Durchführung von ATEX-Geräte-Standortaudits, Inspektionen und Überprüfungen der Gefahrenbereichsklassifizierung',
                        'Durchführung von Arbeitssicherheits-Feldaudits und umfassenden Risikobewertungen',
                        'Verwaltung von Explosionsmodellierung und Konsequenzanalyse für Standorte mit erheblichen Gefahren',
                        'Anwendung von ISO 60079-Standards für die Auswahl von Geräten für explosive Atmosphären'
                    ]
                },
                {
                    'title': 'Sicherheitsspezialist',
                    'company': 'Momentum OSGB',
                    'location': 'Türkei',
                    'period': 'September 2017 – Februar 2019',
                    'responsibilities': [
                        'Bereitstellung von Arbeitssicherheitsexpertise-Beratung in mehreren Branchen einschließlich Chemieanlagen, Bauwesen, Fertigung und Gesundheitswesen',
                        'Durchführung von Umweltrisikobewertungen und Sicherheits-Compliance-Audits',
                        'Entwicklung von Sicherheitsmanagementsystemen für chemische Lager- und Verarbeitungsanlagen'
                    ]
                },
                {
                    'title': 'Sicherheitsmess- & Emissionsberichtsspezialist',
                    'company': 'Testmer Measurement And Testing Services Ltd.',
                    'location': 'Türkei',
                    'period': 'Juli 2016 – September 2017',
                    'responsibilities': [
                        'Durchführung von Arbeitsgesundheits- und Sicherheitsumgebungsmessungen und Expositionsbewertungen',
                        'Erstellung von Emissions- und Geruchsmessberichten gemäß internationalen Standards'
                    ]
                },
                {
                    'title': 'Umweltingenieur',
                    'company': 'Metreküp Treatment Technologies',
                    'location': 'Türkei',
                    'period': 'April 2014 – April 2015',
                    'responsibilities': [
                        'Planung von Abwasserbehandlungsanlagen für Industrieanlagen',
                        'Bereitstellung von Wasserbehandlungsberatung für 13 Fabriken in verschiedenen Branchen'
                    ]
                }
            ],
            
            'education_title': 'AUSBILDUNG',
            'education': [
                {
                    'degree': 'Master-Abschluss (mit Thesis)',
                    'field': 'Arbeitsschutz und Arbeitssicherheit',
                    'institution': 'Üsküdar Universität, Institut für Gesundheitswissenschaften',
                    'location': 'Istanbul, Türkei',
                    'period': 'September 2018 – Februar 2020',
                    'thesis': 'Thesis: "Die Notwendigkeit der Verwendung von Maschinensicherheitsausrüstung anstelle von Sicherheitsausrüstung in Personenaufzügen und Relevanz der Anwendbarkeit von ISO-Standards zur Risikobewertung"'
                },
                {
                    'degree': 'Master-Abschluss (ohne Thesis)',
                    'field': 'Arbeitsschutz und Arbeitssicherheit',
                    'institution': 'Yeni Yüzyıl Universität, Institut für Gesundheitswissenschaften',
                    'location': 'Istanbul, Türkei',
                    'period': 'September 2016 – Februar 2017',
                    'thesis': None
                },
                {
                    'degree': 'Bachelor of Science',
                    'field': 'Umweltingenieurwesen (mit 1 Jahr Englisch-Vorbereitungsklasse)',
                    'institution': 'Ondokuz Mayıs Universität, Fakultät für Ingenieurwesen',
                    'location': 'Samsun, Türkei',
                    'period': 'September 2008 – Juli 2013',
                    'thesis': None
                }
            ],
            
            'memberships_title': 'BERUFSMITGLIEDSCHAFTEN',
            'memberships': [
                'American Institute of Chemical Engineers (AIChE)',
                'Engineers Ireland',
                'Kammer der Umweltingenieure, Türkei'
            ],
            
            'skills_title': 'TECHNISCHE FÄHIGKEITEN & SOFTWARE',
            'skills': [
                ['Prozesssicherheit', 'DNV PHAST, Gexcon Risikomodellierung, HAZOP-Moderation, LOPA-Analyse, Sicherheitsberichtserstellung'],
                ['Regulatorische Compliance', 'SEVESO-Richtlinie III, COMAH-Vorschriften 2015, ATEX-Richtlinie 2014/34/EU, ISO 60079, ISO 45001, ISO 14001'],
                ['Ingenieurwesen', 'AutoCAD 2D/3D, Rhino 3D, Abwasserbehandlungsplanung, Explosionsschutzsysteme'],
                ['Sprachen', 'Türkisch (Muttersprache), Englisch (Professionelle Arbeitskompetenz)']
            ]
        },
        'fr': {
            'name': 'SABIT BURAK CEBECİ',
            'title': 'Consultant en Risques | Spécialiste SEVESO & ATEX',
            'subtitle': 'Ingénierie Environnementale et Sécurité des Procédés',
            'email': 'sabitburakcebeci@gmail.com',
            'phone': '+353 83 084 2944',
            'location': 'Dublin, Irlande',
            'linkedin': 'linkedin.com/in/sbtbrkcbc',
            
            'profile_title': 'PROFIL PROFESSIONNEL',
            'profile': 'Ingénieur Environnemental Senior et Spécialiste de la Sécurité des Procédés avec plus de 13 ans d\'expérience progressive en conformité SEVESO, réglementations ATEX et protection contre les explosions pour les sites Seveso Seuil Haut. Expertise avérée dans le développement de systèmes de gestion de la sécurité des procédés, la conduite d\'études HAZOP et la fourniture de conseil basé sur les risques pour les industries pharmaceutiques et chimiques. Solide formation technique en modélisation des conséquences (DNV PHAST, Gexcon), conformité réglementaire (COMAH, Directives UE) et préparation de rapports de sécurité. Actuellement au service de clients internationaux de haut niveau incluant Intel et des fabricants pharmaceutiques de premier plan.',
            
            'competencies_title': 'COMPÉTENCES PRINCIPALES',
            'competencies': [
                ['Conformité Directive SEVESO', 'Certification & Inspection Équipements ATEX', 'Documentation Protection Explosions'],
                ['Gestion Sécurité Procédés (PSM)', 'Études HAZOP & Analyse LOPA', 'Règlements COMAH 2015'],
                ['Modélisation Conséquences DNV PHAST', 'Évaluation & Atténuation Risques', 'Préparation Rapports Sécurité'],
                ['ISO 60079, ISO 45001, ISO 14001', 'Planification Intervention Urgence', 'Rédaction Rapports Techniques']
            ],
            
            'certifications_title': 'CERTIFICATIONS & FORMATION PROFESSIONNELLES',
            'certifications': [
                'Rédaction de Rapports Techniques – Engineers Ireland (Avr 2024)',
                'Formation Logiciel Modélisation Conséquences DNV SA-01 – DNV (Jan 2024)',
                'Logiciel Modélisation Effets/Risque & Courbes Risque – Gexcon (Nov 2023)',
                'LOPA - Layer of Protection Analysis – CCPS',
                'Certification Formation HAZOP – Seyir Akademi (2019)',
                'Certification Équipements ATEX – Seyir Akademi (2019)',
                'Formation Document Protection Explosions – Seyir Akademi (2019)',
                'Formation Standards ISO 60079 – Seyir Akademi',
                'Certification ISO 45001:2018 SGSST',
                'Systèmes de Gestion Environnementale ISO 14001'
            ],
            
            'experience_title': 'EXPÉRIENCE PROFESSIONNELLE',
            'experience': [
                {
                    'title': 'Consultant en Risques Senior',
                    'company': 'AWN Consulting Ltd.',
                    'location': 'Dublin, Irlande',
                    'period': 'Août 2023 – Présent',
                    'responsibilities': [
                        'Fournir des services de conseil en sécurité des procédés et risques environnementaux pour les sites Seveso Seuil Haut en Irlande et en Europe',
                        'Conduire des services de conseil SEVESO incluant la préparation de rapports de sécurité, les évaluations de modifications significatives et les révisions de conformité réglementaire',
                        'Préparer et mettre à jour les Documents de Protection contre les Explosions (EPD) en utilisant le logiciel de modélisation des conséquences DNV PHAST',
                        'Soutenir des clients de haut niveau incluant Intel et des fabricants pharmaceutiques dans l\'atteinte de la conformité COMAH',
                        'Fournir la rédaction de rapports techniques et le soutien aux soumissions réglementaires à l\'EPA et HSA irlandais'
                    ]
                },
                {
                    'title': 'Ingénieur Sécurité des Procédés',
                    'company': 'Guerbet (Fabrication Pharmaceutique)',
                    'location': 'Dublin, Irlande',
                    'period': 'Août 2022 – Juin 2023',
                    'responsibilities': [
                        'Développé et dirigé le Système de Gestion de la Sécurité des Procédés pour un site Seveso Seuil Haut',
                        'Conduit des évaluations de modifications significatives selon les Règlements COMAH 2015',
                        'Mis à jour et maintenu le Rapport de Sécurité du site et le Document de Protection contre les Explosions',
                        'Dirigé les Évaluations de Risques de Sécurité des Procédés incluant les études HAZOP et LOPA',
                        'Géré les procédures de Gestion du Changement (MoC) pour les modifications d\'installation, de procédé et de système',
                        'Fourni des révisions d\'inspection ATEX et un soutien EHS pour les projets d\'investissement',
                        'Assisté la gestion de l\'Équipe d\'Intervention d\'Urgence et les activités de planification d\'urgence'
                    ]
                },
                {
                    'title': 'Spécialiste Sécurité & Ingénieur Environnemental',
                    'company': 'Seyir Akademi (Cabinet Leader en Sécurité des Procédés)',
                    'location': 'Istanbul, Turquie',
                    'period': 'Février 2019 – Octobre 2021',
                    'responsibilities': [
                        'Fourni des services de conseil SEVESO pour plus de 30 clients en production chimique, pharmaceutique et chimie agricole',
                        'Préparé des Documents de Protection contre les Explosions et des Rapports de Sécurité appliquant les standards européens',
                        'Conduit des audits sur site d\'équipements ATEX, inspections et révisions de classification de zones dangereuses',
                        'Effectué des audits sur site de sécurité au travail et des évaluations complètes des risques',
                        'Géré la modélisation d\'explosion et l\'analyse des conséquences pour les sites à risques majeurs',
                        'Appliqué les standards ISO 60079 pour la sélection d\'équipements en atmosphères explosives'
                    ]
                },
                {
                    'title': 'Spécialiste Sécurité',
                    'company': 'Momentum OSGB',
                    'location': 'Turquie',
                    'period': 'Septembre 2017 – Février 2019',
                    'responsibilities': [
                        'Fourni des services de conseil en expertise de sécurité au travail dans plusieurs industries incluant les usines chimiques, construction, fabrication et santé',
                        'Conduit des évaluations des risques environnementaux et des audits de conformité sécurité',
                        'Développé des systèmes de gestion de la sécurité pour les installations de stockage et traitement chimique'
                    ]
                },
                {
                    'title': 'Spécialiste Mesures Sécurité & Reporting Émissions',
                    'company': 'Testmer Measurement And Testing Services Ltd.',
                    'location': 'Turquie',
                    'period': 'Juillet 2016 – Septembre 2017',
                    'responsibilities': [
                        'Conduit des mesures d\'environnement de santé et sécurité au travail et des évaluations d\'exposition',
                        'Préparé des rapports de mesure d\'émissions et d\'odeurs conformément aux standards internationaux'
                    ]
                },
                {
                    'title': 'Ingénieur Environnemental',
                    'company': 'Metreküp Treatment Technologies',
                    'location': 'Turquie',
                    'period': 'Avril 2014 – Avril 2015',
                    'responsibilities': [
                        'Conçu des stations de traitement des eaux usées pour les installations industrielles',
                        'Fourni des services de conseil en traitement de l\'eau pour 13 usines dans diverses industries'
                    ]
                }
            ],
            
            'education_title': 'FORMATION',
            'education': [
                {
                    'degree': 'Master (avec Thèse)',
                    'field': 'Santé et Sécurité au Travail',
                    'institution': 'Université d\'Üsküdar, Institut des Sciences de la Santé',
                    'location': 'Istanbul, Turquie',
                    'period': 'Septembre 2018 – Février 2020',
                    'thesis': 'Thèse: "La Nécessité d\'Utiliser des Équipements de Sécurité Machine au Lieu des Équipements de Sécurité Utilisés dans les Ascenseurs de Passagers et Pertinence de la Comparaison d\'Applicabilité des Standards ISO d\'Évaluation des Risques"'
                },
                {
                    'degree': 'Master (sans Thèse)',
                    'field': 'Santé et Sécurité au Travail',
                    'institution': 'Université Yeni Yüzyıl, Institut des Sciences de la Santé',
                    'location': 'Istanbul, Turquie',
                    'period': 'Septembre 2016 – Février 2017',
                    'thesis': None
                },
                {
                    'degree': 'Licence en Sciences',
                    'field': 'Ingénierie Environnementale (avec 1 An de Classe Préparatoire Anglais)',
                    'institution': 'Université Ondokuz Mayıs, Faculté d\'Ingénierie',
                    'location': 'Samsun, Turquie',
                    'period': 'Septembre 2008 – Juillet 2013',
                    'thesis': None
                }
            ],
            
            'memberships_title': 'AFFILIATIONS PROFESSIONNELLES',
            'memberships': [
                'American Institute of Chemical Engineers (AIChE)',
                'Engineers Ireland',
                'Chambre des Ingénieurs Environnementaux, Turquie'
            ],
            
            'skills_title': 'COMPÉTENCES TECHNIQUES & LOGICIELS',
            'skills': [
                ['Sécurité Procédés', 'DNV PHAST, Modélisation Risque Gexcon, Animation HAZOP, Analyse LOPA, Rédaction Rapports Sécurité'],
                ['Conformité Réglementaire', 'Directive SEVESO III, Règlements COMAH 2015, Directive ATEX 2014/34/UE, ISO 60079, ISO 45001, ISO 14001'],
                ['Ingénierie', 'AutoCAD 2D/3D, Rhino 3D, Conception Traitement Eaux Usées, Systèmes Protection Explosions'],
                ['Langues', 'Turc (Langue Maternelle), Anglais (Compétence Professionnelle)']
            ]
        },
        'es': {
            'name': 'SABIT BURAK CEBECİ',
            'title': 'Consultor de Riesgos | Especialista SEVESO y ATEX',
            'subtitle': 'Ingeniería Ambiental y Seguridad de Procesos',
            'email': 'sabitburakcebeci@gmail.com',
            'phone': '+353 83 084 2944',
            'location': 'Dublín, Irlanda',
            'linkedin': 'linkedin.com/in/sbtbrkcbc',
            
            'profile_title': 'PERFIL PROFESIONAL',
            'profile': 'Ingeniero Ambiental Senior y Especialista en Seguridad de Procesos con más de 13 años de experiencia progresiva en cumplimiento SEVESO, regulaciones ATEX y protección contra explosiones para instalaciones Seveso de Nivel Superior. Experiencia comprobada en el desarrollo de sistemas de gestión de seguridad de procesos, realización de estudios HAZOP y prestación de consultoría basada en riesgos para las industrias farmacéutica y química. Sólida formación técnica en modelado de consecuencias (DNV PHAST, Gexcon), cumplimiento normativo (COMAH, Directivas UE) y preparación de informes de seguridad. Actualmente al servicio de clientes internacionales de alto perfil como Intel y fabricantes farmacéuticos líderes.',
            
            'competencies_title': 'COMPETENCIAS PRINCIPALES',
            'competencies': [
                ['Cumplimiento Directiva SEVESO', 'Certificación e Inspección Equipos ATEX', 'Documentación Protección Explosiones'],
                ['Gestión Seguridad Procesos (PSM)', 'Estudios HAZOP y Análisis LOPA', 'Regulaciones COMAH 2015'],
                ['Modelado Consecuencias DNV PHAST', 'Evaluación y Mitigación de Riesgos', 'Preparación Informes Seguridad'],
                ['ISO 60079, ISO 45001, ISO 14001', 'Planificación Respuesta Emergencias', 'Redacción Informes Técnicos']
            ],
            
            'certifications_title': 'CERTIFICACIONES Y FORMACIÓN PROFESIONAL',
            'certifications': [
                'Redacción de Informes Técnicos – Engineers Ireland (Abr 2024)',
                'Formación Software Modelado Consecuencias DNV SA-01 – DNV (Ene 2024)',
                'Software Modelado Efectos/Riesgo y Curvas de Riesgo – Gexcon (Nov 2023)',
                'LOPA - Layer of Protection Analysis – CCPS',
                'Certificación Formación HAZOP – Seyir Akademi (2019)',
                'Certificación Equipos ATEX – Seyir Akademi (2019)',
                'Formación Documento Protección Explosiones – Seyir Akademi (2019)',
                'Formación Estándares ISO 60079 – Seyir Akademi',
                'Certificación ISO 45001:2018 SGSSO',
                'Sistemas de Gestión Ambiental ISO 14001'
            ],
            
            'experience_title': 'EXPERIENCIA PROFESIONAL',
            'experience': [
                {
                    'title': 'Consultor de Riesgos Senior',
                    'company': 'AWN Consulting Ltd.',
                    'location': 'Dublín, Irlanda',
                    'period': 'Agosto 2023 – Presente',
                    'responsibilities': [
                        'Proporcionar consultoría en seguridad de procesos y riesgos ambientales para instalaciones Seveso de Nivel Superior en Irlanda y Europa',
                        'Realizar servicios de consultoría SEVESO incluyendo preparación de informes de seguridad, evaluaciones de modificaciones significativas y revisiones de cumplimiento normativo',
                        'Preparar y actualizar Documentos de Protección contra Explosiones (EPD) utilizando software de modelado de consecuencias DNV PHAST',
                        'Apoyar a clientes de alto perfil como Intel y fabricantes farmacéuticos en el logro del cumplimiento COMAH',
                        'Proporcionar redacción de informes técnicos y apoyo en presentaciones normativas a la EPA y HSA irlandesas'
                    ]
                },
                {
                    'title': 'Ingeniero de Seguridad de Procesos',
                    'company': 'Guerbet (Fabricación Farmacéutica)',
                    'location': 'Dublín, Irlanda',
                    'period': 'Agosto 2022 – Junio 2023',
                    'responsibilities': [
                        'Desarrollado y dirigido el Sistema de Gestión de Seguridad de Procesos para una instalación Seveso de Nivel Superior',
                        'Realizado evaluaciones de modificaciones significativas según Regulaciones COMAH 2015',
                        'Actualizado y mantenido el Informe de Seguridad de la instalación y el Documento de Protección contra Explosiones',
                        'Dirigido Evaluaciones de Riesgo de Seguridad de Procesos incluyendo estudios HAZOP y LOPA',
                        'Gestionado procedimientos de Gestión del Cambio (MoC) para modificaciones de planta, proceso y sistema',
                        'Proporcionado revisiones de inspección ATEX y apoyo EHS para proyectos de inversión de capital',
                        'Asistido en la gestión del Equipo de Respuesta a Emergencias y actividades de planificación de emergencias'
                    ]
                },
                {
                    'title': 'Especialista en Seguridad e Ingeniero Ambiental',
                    'company': 'Seyir Akademi (Consultoría Líder en Seguridad de Procesos)',
                    'location': 'Estambul, Turquía',
                    'period': 'Febrero 2019 – Octubre 2021',
                    'responsibilities': [
                        'Proporcionado consultoría SEVESO para más de 30 clientes en producción química, farmacéutica y química agrícola',
                        'Preparado Documentos de Protección contra Explosiones e Informes de Seguridad aplicando estándares europeos',
                        'Realizado auditorías de equipos ATEX en instalaciones, inspecciones y revisiones de clasificación de áreas peligrosas',
                        'Ejecutado auditorías de campo de seguridad ocupacional y evaluaciones de riesgo exhaustivas',
                        'Gestionado modelado de explosiones y análisis de consecuencias para instalaciones con riesgos mayores',
                        'Aplicado estándares ISO 60079 para selección de equipos en atmósferas explosivas'
                    ]
                },
                {
                    'title': 'Especialista en Seguridad',
                    'company': 'Momentum OSGB',
                    'location': 'Turquía',
                    'period': 'Septiembre 2017 – Febrero 2019',
                    'responsibilities': [
                        'Proporcionado consultoría experta en seguridad ocupacional en múltiples industrias incluyendo plantas químicas, construcción, fabricación y salud',
                        'Realizado evaluaciones de riesgo ambiental y auditorías de cumplimiento de seguridad',
                        'Desarrollado sistemas de gestión de seguridad para instalaciones de almacenamiento y procesamiento químico'
                    ]
                },
                {
                    'title': 'Especialista en Medición de Seguridad y Reporte de Emisiones',
                    'company': 'Testmer Measurement And Testing Services Ltd.',
                    'location': 'Turquía',
                    'period': 'Julio 2016 – Septiembre 2017',
                    'responsibilities': [
                        'Realizado mediciones de ambiente de salud y seguridad ocupacional y evaluaciones de exposición',
                        'Preparado informes de medición de emisiones y olores conforme a estándares internacionales'
                    ]
                },
                {
                    'title': 'Ingeniero Ambiental',
                    'company': 'Metreküp Treatment Technologies',
                    'location': 'Turquía',
                    'period': 'Abril 2014 – Abril 2015',
                    'responsibilities': [
                        'Diseñado plantas de tratamiento de aguas residuales para instalaciones industriales',
                        'Proporcionado consultoría en tratamiento de agua para 13 fábricas en diversas industrias'
                    ]
                }
            ],
            
            'education_title': 'FORMACIÓN',
            'education': [
                {
                    'degree': 'Máster (con Tesis)',
                    'field': 'Salud y Seguridad Ocupacional',
                    'institution': 'Universidad Üsküdar, Instituto de Ciencias de la Salud',
                    'location': 'Estambul, Turquía',
                    'period': 'Septiembre 2018 – Febrero 2020',
                    'thesis': 'Tesis: "La Necesidad de Utilizar Equipos de Seguridad de Máquinas en Lugar de Equipos de Seguridad Utilizados en Ascensores de Pasajeros y Relevancia de la Comparación de Aplicabilidad de Estándares ISO de Evaluación de Riesgos"'
                },
                {
                    'degree': 'Máster (sin Tesis)',
                    'field': 'Salud y Seguridad Ocupacional',
                    'institution': 'Universidad Yeni Yüzyıl, Instituto de Ciencias de la Salud',
                    'location': 'Estambul, Turquía',
                    'period': 'Septiembre 2016 – Febrero 2017',
                    'thesis': None
                },
                {
                    'degree': 'Licenciatura en Ciencias',
                    'field': 'Ingeniería Ambiental (con 1 Año de Clase Preparatoria de Inglés)',
                    'institution': 'Universidad Ondokuz Mayıs, Facultad de Ingeniería',
                    'location': 'Samsun, Turquía',
                    'period': 'Septiembre 2008 – Julio 2013',
                    'thesis': None
                }
            ],
            
            'memberships_title': 'AFILIACIONES PROFESIONALES',
            'memberships': [
                'American Institute of Chemical Engineers (AIChE)',
                'Engineers Ireland',
                'Cámara de Ingenieros Ambientales, Turquía'
            ],
            
            'skills_title': 'HABILIDADES TÉCNICAS Y SOFTWARE',
            'skills': [
                ['Seguridad Procesos', 'DNV PHAST, Modelado Riesgo Gexcon, Facilitación HAZOP, Análisis LOPA, Redacción Informes Seguridad'],
                ['Cumplimiento Normativo', 'Directiva SEVESO III, Regulaciones COMAH 2015, Directiva ATEX 2014/34/UE, ISO 60079, ISO 45001, ISO 14001'],
                ['Ingeniería', 'AutoCAD 2D/3D, Rhino 3D, Diseño Tratamiento Aguas Residuales, Sistemas Protección Explosiones'],
                ['Idiomas', 'Turco (Nativo), Inglés (Competencia Profesional)']
            ]
        },
        'se': {
            'name': 'SABIT BURAK CEBECİ',
            'title': 'Riskkonsult | SEVESO & ATEX Specialist',
            'subtitle': 'Miljö- och Processsäkerhetsteknik',
            'email': 'sabitburakcebeci@gmail.com',
            'phone': '+353 83 084 2944',
            'location': 'Dublin, Irland',
            'linkedin': 'linkedin.com/in/sbtbrkcbc',
            
            'profile_title': 'PROFESSIONELL PROFIL',
            'profile': 'Senior miljöingenjör och processsäkerhetsspecialist med 13+ års progressiv erfarenhet av SEVESO-efterlevnad, ATEX-förordningar och explosionsskydd för Seveso-anläggningar i övre klass. Beprövad expertis inom utveckling av processsäkerhetshanteringssystem, genomförande av HAZOP-studier och tillhandahållande av riskbaserad rådgivning för läkemedels- och kemiindustrin. Stark teknisk bakgrund inom konsekvensmodellering (DNV PHAST, Gexcon), regelefterlevnad (COMAH, EU-direktiv) och säkerhetsrapportförberedelse. För närvarande tjänar högt profilerade internationella kunder inklusive Intel och ledande läkemedelsproducenter.',
            
            'competencies_title': 'KÄRNKOMPETENSER',
            'competencies': [
                ['SEVESO-direktivefterlevnad', 'ATEX-utrustningscertifiering & Inspektion', 'Explosionsskyddsdokumentation'],
                ['Processsäkerhetshantering (PSM)', 'HAZOP-studier & LOPA-analys', 'COMAH-förordningar 2015'],
                ['DNV PHAST Konsekvensmodellering', 'Riskbedömning & Riskreducering', 'Säkerhetsrapportförberedelse'],
                ['ISO 60079, ISO 45001, ISO 14001', 'Nödinsatsplanering', 'Teknisk Rapportskrivning']
            ],
            
            'certifications_title': 'PROFESSIONELLA CERTIFIERINGAR & UTBILDNING',
            'certifications': [
                'Teknisk Rapportskrivning – Engineers Ireland (Apr 2024)',
                'DNV SA-01 Konsekvensmodelleringsprogramutbildning – DNV (Jan 2024)',
                'Effekt-/Risk- & Riskkurvsmodelleringsprogram – Gexcon (Nov 2023)',
                'LOPA - Layer of Protection Analysis – CCPS',
                'HAZOP-utbildningscertifiering – Seyir Akademi (2019)',
                'ATEX-utrustningscertifiering – Seyir Akademi (2019)',
                'Explosionsskyddsdokumentutbildning – Seyir Akademi (2019)',
                'ISO 60079 Standardsutbildning – Seyir Akademi',
                'ISO 45001:2018 OHSMS-certifiering',
                'ISO 14001 Miljöledningssystem'
            ],
            
            'experience_title': 'PROFESSIONELL ERFARENHET',
            'experience': [
                {
                    'title': 'Senior Riskkonsult',
                    'company': 'AWN Consulting Ltd.',
                    'location': 'Dublin, Irland',
                    'period': 'Augusti 2023 – Nuvarande',
                    'responsibilities': [
                        'Tillhandahålla processsäkerhets- och miljöriskkonsultation för Seveso-anläggningar i övre klass i Irland och Europa',
                        'Genomföra SEVESO-konsulttjänster inklusive säkerhetsrapportförberedelse, betydande modifieringsbedömningar och regelefterlevnadsgranskningar',
                        'Förbereda och uppdatera explosionsskyddsdokument (EPD) med hjälp av DNV PHAST konsekvensmodelleringsprogram',
                        'Stödja högt profilerade kunder inklusive Intel och läkemedelsproducenter för att uppnå COMAH-efterlevnad',
                        'Tillhandahålla teknisk rapportskrivning och stöd för myndighetsinlämningar till irländska EPA och HSA'
                    ]
                },
                {
                    'title': 'Processsäkerhetsingenjör',
                    'company': 'Guerbet (Läkemedelsproduktion)',
                    'location': 'Dublin, Irland',
                    'period': 'Augusti 2022 – Juni 2023',
                    'responsibilities': [
                        'Utvecklade och ledde processsäkerhetshanteringssystemet för en Seveso-anläggning i övre klass',
                        'Genomförde bedömningar av betydande modifieringar enligt COMAH-förordningar 2015',
                        'Uppdaterade och underhöll anläggningens säkerhetsrapport och explosionsskyddsdokument',
                        'Ledde processsäkerhetsriskbedömningar inklusive HAZOP- och LOPA-studier',
                        'Hanterade förändringsledningsrutiner (MoC) för anläggnings-, process- och systemmodifieringar',
                        'Tillhandahöll ATEX-inspektionsgranskningar och EHS-stöd för kapitalinvesteringsprojekt',
                        'Assisterade nödinsatsteamsledning och nödplaneringsaktiviteter'
                    ]
                },
                {
                    'title': 'Säkerhetsspecialist & Miljöingenjör',
                    'company': 'Seyir Akademi (Ledande Processsäkerhetskonsult)',
                    'location': 'Istanbul, Turkiet',
                    'period': 'Februari 2019 – Oktober 2021',
                    'responsibilities': [
                        'Levererade SEVESO-konsultation för 30+ kunder inom kemisk produktion, läkemedel och jordbrukskemikalier',
                        'Förberedde explosionsskyddsdokument och säkerhetsrapporter med tillämpning av europeiska standarder',
                        'Genomförde ATEX-utrustningsanläggningsrevisioner, inspektioner och granskningar av farlig områdesklassificering',
                        'Utförde arbetsmiljösäkerhetsfältrevisioner och omfattande riskbedömningar',
                        'Hanterade explosionsmodellering och konsekvensanalys för anläggningar med stor risk',
                        'Tillämpade ISO 60079-standarder för val av utrustning för explosiv atmosfär'
                    ]
                },
                {
                    'title': 'Säkerhetsspecialist',
                    'company': 'Momentum OSGB',
                    'location': 'Turkiet',
                    'period': 'September 2017 – Februari 2019',
                    'responsibilities': [
                        'Tillhandahöll expertis inom arbetsmiljösäkerhet för flera branscher inklusive kemiska anläggningar, byggande, tillverkning och hälsovård',
                        'Genomförde miljöriskbedömningar och säkerhetsefterlevnadsrevisioner',
                        'Utvecklade säkerhetshanteringssystem för kemisk lagrings- och bearbetningsanläggningar'
                    ]
                },
                {
                    'title': 'Säkerhetsmätnings- & Emissionsrapporteringsspecialist',
                    'company': 'Testmer Measurement And Testing Services Ltd.',
                    'location': 'Turkiet',
                    'period': 'Juli 2016 – September 2017',
                    'responsibilities': [
                        'Genomförde arbetshälso- och säkerhetsmiljömätningar och exponeringsbedömningar',
                        'Förberedde emissions- och luktmätningsrapporter i enlighet med internationella standarder'
                    ]
                },
                {
                    'title': 'Miljöingenjör',
                    'company': 'Metreküp Treatment Technologies',
                    'location': 'Turkiet',
                    'period': 'April 2014 – April 2015',
                    'responsibilities': [
                        'Designade avloppsvattenreningsanläggningar för industriella anläggningar',
                        'Tillhandahöll vattenbehandlingskonsultation för 13 fabriker inom olika branscher'
                    ]
                }
            ],
            
            'education_title': 'UTBILDNING',
            'education': [
                {
                    'degree': 'Masterexamen (med Avhandling)',
                    'field': 'Arbetsmiljö och Säkerhet',
                    'institution': 'Üsküdar Universitet, Hälsovetenskapsinstitutet',
                    'location': 'Istanbul, Turkiet',
                    'period': 'September 2018 – Februari 2020',
                    'thesis': 'Avhandling: "Nödvändigheten att använda maskinsäkerhetsutrustning istället för säkerhetsutrustning som används i passagerarh issar och relevans av tillämpbarheten av ISO-standarder för riskbedömning"'
                },
                {
                    'degree': 'Masterexamen (utan Avhandling)',
                    'field': 'Arbetsmiljö och Säkerhet',
                    'institution': 'Yeni Yüzyıl Universitet, Hälsovetenskapsinstitutet',
                    'location': 'Istanbul, Turkiet',
                    'period': 'September 2016 – Februari 2017',
                    'thesis': None
                },
                {
                    'degree': 'Kandidatexamen',
                    'field': 'Miljöteknik (med 1 års engelsk förberedelseklass)',
                    'institution': 'Ondokuz Mayıs Universitet, Ingenjörsfakulteten',
                    'location': 'Samsun, Turkiet',
                    'period': 'September 2008 – Juli 2013',
                    'thesis': None
                }
            ],
            
            'memberships_title': 'PROFESSIONELLA MEDLEMSKAP',
            'memberships': [
                'American Institute of Chemical Engineers (AIChE)',
                'Engineers Ireland',
                'Kammaren för miljöingenjörer, Turkiet'
            ],
            
            'skills_title': 'TEKNISKA FÄRDIGHETER & PROGRAMVARA',
            'skills': [
                ['Processsäkerhet', 'DNV PHAST, Gexcon Riskmodellering, HAZOP-facilitering, LOPA-analys, Säkerhetsrapportskrivning'],
                ['Regelefterlevnad', 'SEVESO-direktiv III, COMAH-förordningar 2015, ATEX-direktiv 2014/34/EU, ISO 60079, ISO 45001, ISO 14001'],
                ['Ingenjörskonst', 'AutoCAD 2D/3D, Rhino 3D, Avloppsvattenreningsdesign, Explosionsskyddssystem'],
                ['Språk', 'Turkiska (Modersmål), Engelska (Professionell Arbetskompetens)']
            ]
        }
    }
    
    c = content[language]
    
    # Create PDF with proper margins for ATS compatibility
    doc = SimpleDocTemplate(
        filename, 
        pagesize=A4,
        topMargin=2*cm,
        bottomMargin=2*cm,
        leftMargin=2*cm,
        rightMargin=2*cm
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # ATS-Friendly Custom Styles using DejaVu font
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontName='DejaVu-Bold',
        fontSize=20,
        textColor=NAVY_BLUE,
        spaceAfter=4,
        alignment=TA_CENTER,
        leading=24
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='DejaVu',
        fontSize=12,
        textColor=DARK_GRAY,
        spaceAfter=2,
        alignment=TA_CENTER,
        leading=14
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='DejaVu',
        fontSize=10,
        textColor=MED_GRAY,
        spaceAfter=8,
        alignment=TA_CENTER,
        leading=12
    )
    
    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='DejaVu-Bold',
        fontSize=11,
        textColor=NAVY_BLUE,
        spaceAfter=8,
        spaceBefore=12,
        leading=13,
        borderWidth=0,
        borderPadding=0,
        leftIndent=0
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='DejaVu',
        fontSize=9,
        textColor=DARK_GRAY,
        spaceAfter=4,
        leading=11,
        alignment=TA_JUSTIFY
    )
    
    job_title_style = ParagraphStyle(
        'JobTitleStyle',
        parent=styles['Normal'],
        fontName='DejaVu-Bold',
        fontSize=10,
        textColor=DARK_GRAY,
        spaceAfter=2,
        leading=12
    )
    
    job_company_style = ParagraphStyle(
        'JobCompanyStyle',
        parent=styles['Normal'],
        fontName='DejaVu',
        fontSize=9,
        textColor=MED_GRAY,
        spaceAfter=4,
        leading=11
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='DejaVu',
        fontSize=9,
        textColor=DARK_GRAY,
        spaceAfter=3,
        leftIndent=15,
        leading=11
    )
    
    # Header with Photo
    photo_path = '/app/backend/profile_photo.jpg'
    if os.path.exists(photo_path):
        # Create header table with photo and contact info
        photo = Image(photo_path, width=3*cm, height=3*cm)
        
        header_data = [[photo, Paragraph(c['name'], name_style)]]
        header_table = Table(header_data, colWidths=[3.5*cm, 14*cm])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'LEFT'),
        ]))
        story.append(header_table)
    else:
        # Fallback if photo not available
        story.append(Paragraph(c['name'], name_style))
    
    story.append(Paragraph(c['title'], title_style))
    story.append(Paragraph(c['subtitle'], subtitle_style))
    story.append(Spacer(1, 3*mm))
    
    # Contact Information (simple, ATS-readable)
    contact_text = f"{c['email']} | {c['phone']} | {c['location']} | {c['linkedin']}"
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='DejaVu',
        fontSize=9,
        textColor=MED_GRAY,
        alignment=TA_CENTER,
        spaceAfter=8
    )
    story.append(Paragraph(contact_text, contact_style))
    
    # Horizontal line separator
    story.append(Spacer(1, 2*mm))
    line_table = Table([['']], colWidths=[17*cm])
    line_table.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, 0), 0.5, LIGHT_GRAY),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 3*mm))
    
    # Professional Profile
    story.append(Paragraph(c['profile_title'], section_heading_style))
    story.append(Paragraph(c['profile'], body_style))
    story.append(Spacer(1, 4*mm))
    
    # Core Competencies (table format for ATS)
    story.append(Paragraph(c['competencies_title'], section_heading_style))
    comp_data = []
    for row in c['competencies']:
        comp_row = [Paragraph(f"• {item}", bullet_style) for item in row]
        comp_data.append(comp_row)
    
    comp_table = Table(comp_data, colWidths=[5.5*cm, 5.5*cm, 5.5*cm])
    comp_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(comp_table)
    story.append(Spacer(1, 4*mm))
    
    # Professional Certifications
    story.append(Paragraph(c['certifications_title'], section_heading_style))
    for cert in c['certifications']:
        story.append(Paragraph(f"• {cert}", bullet_style))
    story.append(Spacer(1, 4*mm))
    
    # Professional Experience
    story.append(Paragraph(c['experience_title'], section_heading_style))
    for exp in c['experience']:
        # Job title and company (bold for ATS parsing)
        story.append(Paragraph(f"<b>{exp['title']}</b>", job_title_style))
        story.append(Paragraph(f"{exp['company']} | {exp['location']} | {exp['period']}", job_company_style))
        
        # Responsibilities with action verbs
        for resp in exp['responsibilities']:
            story.append(Paragraph(f"• {resp}", bullet_style))
        
        story.append(Spacer(1, 3*mm))
    
    # Education
    story.append(Paragraph(c['education_title'], section_heading_style))
    for edu in c['education']:
        story.append(Paragraph(f"<b>{edu['degree']} - {edu['field']}</b>", job_title_style))
        story.append(Paragraph(f"{edu['institution']}, {edu['location']} | {edu['period']}", job_company_style))
        if edu['thesis']:
            story.append(Paragraph(edu['thesis'], bullet_style))
        story.append(Spacer(1, 2*mm))
    
    # Professional Memberships
    story.append(Paragraph(c['memberships_title'], section_heading_style))
    for member in c['memberships']:
        story.append(Paragraph(f"• {member}", bullet_style))
    story.append(Spacer(1, 3*mm))
    
    # Technical Skills
    story.append(Paragraph(c['skills_title'], section_heading_style))
    for skill_cat, skill_list in c['skills']:
        story.append(Paragraph(f"<b>{skill_cat}:</b> {skill_list}", bullet_style))
    
    # Build PDF
    doc.build(story)
    print(f"ATS-friendly CV generated: {filename}")

if __name__ == "__main__":
    cv_dir = "/app/backend/static/cv"
    os.makedirs(cv_dir, exist_ok=True)
    
    # Generate CVs in all 7 languages
    create_cv(f"{cv_dir}/cv_en.pdf", 'en')
    create_cv(f"{cv_dir}/cv_it.pdf", 'it')
    create_cv(f"{cv_dir}/cv_tr.pdf", 'tr')
    create_cv(f"{cv_dir}/cv_de.pdf", 'de')
    create_cv(f"{cv_dir}/cv_fr.pdf", 'fr')
    create_cv(f"{cv_dir}/cv_es.pdf", 'es')
    create_cv(f"{cv_dir}/cv_se.pdf", 'se')
    
    print("All 7 ATS-friendly CVs with multilingual character support generated successfully!")
