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
            'profile': 'Senior Environmental Engineer and Process Safety Specialist with 11+ years of progressive experience in SEVESO compliance, ATEX regulations, and explosion protection for Upper Tier Seveso sites. Proven expertise in developing Process Safety Management systems, conducting HAZOP studies, and delivering risk-based consultancy for pharmaceutical and chemical industries. Strong technical background in consequence modelling (DNV PHAST, Gexcon), regulatory compliance (COMAH, EU Directives), and safety report preparation. Currently serving high-profile international clients including Intel and leading pharmaceutical manufacturers.',
            
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
                    'title': 'Risk Consultant',
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
            'profile': 'Ingegnere Ambientale Senior e Specialista della Sicurezza di Processo con oltre 11 anni di esperienza progressiva in conformità SEVESO, normative ATEX e protezione dalle esplosioni per siti Seveso di Soglia Superiore. Comprovata competenza nello sviluppo di sistemi di gestione della sicurezza di processo, conduzione di studi HAZOP e fornitura di consulenza basata sul rischio per le industrie farmaceutiche e chimiche. Solida formazione tecnica nella modellazione delle conseguenze (DNV PHAST, Gexcon), conformità normativa (COMAH, Direttive UE) e preparazione di rapporti di sicurezza. Attualmente al servizio di clienti internazionali di alto profilo tra cui Intel e principali produttori farmaceutici.',
            
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
            'profile': 'Üst Kademe Seveso tesisleri için SEVESO uyumluluğu, ATEX yönetmelikleri ve patlama koruması konularında 11+ yıllık ilerleyici deneyime sahip Kıdemli Çevre Mühendisi ve Proses Güvenliği Uzmanı. Proses Güvenliği Yönetim sistemleri geliştirme, HAZOP çalışmaları yürütme ve ilaç ve kimya endüstrileri için risk tabanlı danışmanlık sunma konusunda kanıtlanmış uzmanlık. Sonuç modelleme (DNV PHAST, Gexcon), mevzuat uyumluluğu (COMAH, AB Direktifleri) ve güvenlik raporu hazırlama konularında güçlü teknik altyapı. Şu anda Intel ve önde gelen ilaç üreticileri dahil olmak üzere yüksek profilli uluslararası müşterilere hizmet vermektedir.',
            
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
                    'title': 'Risk Danışmanı',
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
    
    # Generate CVs in all languages
    create_cv(f"{cv_dir}/cv_en.pdf", 'en')
    create_cv(f"{cv_dir}/cv_it.pdf", 'it')
    create_cv(f"{cv_dir}/cv_tr.pdf", 'tr')
    
    print("All ATS-friendly CVs with Turkish character support generated successfully!")
