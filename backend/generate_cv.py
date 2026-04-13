from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

def create_cv(filename, language='en'):
    """
    Generate a professional CV PDF
    """
    # Content in different languages
    content = {
        'en': {
            'name': 'SABIT BURAK CEBECİ',
            'title': 'Environmental Engineer & Process Safety Specialist',
            'contact': 'Contact Information',
            'email': 'Email: sabitburakcebeci@gmail.com',
            'phone': 'Phone: +353 83 084 2944',
            'location': 'Location: Dublin, Ireland',
            'linkedin': 'LinkedIn: linkedin.com/in/sbtbrkcbc',
            'summary_title': 'Professional Summary',
            'summary': 'With over 9 years of specialized experience in environmental engineering and occupational safety, I provide expert consultancy in SEVESO compliance, ATEX regulations, and explosion protection for Upper Tier Seveso sites across Europe. Currently serving as a Risk Consultant at AWN Consulting Ltd., I help companies in chemical production, pharmaceuticals, and manufacturing achieve regulatory compliance while implementing robust process safety management systems.',
            'experience_title': 'Professional Experience',
            'education_title': 'Education',
            'skills_title': 'Key Competencies',
            'certifications_title': 'Certifications',
            'experience': [
                ('Risk Consultant', 'AWN Consulting Ltd., Dublin, Ireland', 'Aug 2023 - Present', [
                    'Process Safety and Environmental Risk Consultancy',
                    'SEVESO Consultancy for multiple client sites',
                    'Explosion Protection Document Preparation',
                    'Safety Report Development and Updates'
                ]),
                ('Process Safety Engineer', 'Guerbet, Ireland', 'Aug 2022 - Jun 2023', [
                    'Developed Process Safety Management System for Upper Tier Seveso site',
                    'Conducted modification assessments under COMAH Regulations',
                    'Led HAZOP and Process Safety Risk Assessments'
                ]),
                ('Safety Specialist & Environmental Engineer', 'Seyir Akademi, Turkey', 'Feb 2019 - Oct 2021', [
                    'SEVESO consultancy for chemical and pharmaceutical clients',
                    'ATEX equipment site audits and inspections',
                    'Explosion Protection Document preparation'
                ])
            ],
            'education': [
                "Master's Degree - Occupational Health & Safety (Thesis), Üsküdar University",
                "Master's Degree - Occupational Health & Safety (Non-Thesis), Yeni Yüzyıl University",
                'B.Sc. Environmental Engineering, Ondokuz Mayıs University'
            ],
            'skills': [
                'SEVESO & COMAH Compliance',
                'ATEX Equipment Selection & Inspection',
                'Process Safety Management Systems',
                'Explosion Protection Documentation',
                'HAZOP Studies',
                'Risk Assessment',
                'ISO 60079, ISO 45001, ISO 14001'
            ]
        },
        'it': {
            'name': 'SABIT BURAK CEBECİ',
            'title': 'Ingegnere Ambientale e Specialista di Sicurezza di Processo',
            'contact': 'Informazioni di Contatto',
            'email': 'Email: sabitburakcebeci@gmail.com',
            'phone': 'Telefono: +353 83 084 2944',
            'location': 'Posizione: Dublino, Irlanda',
            'linkedin': 'LinkedIn: linkedin.com/in/sbtbrkcbc',
            'summary_title': 'Riepilogo Professionale',
            'summary': 'Con oltre 9 anni di esperienza specializzata in ingegneria ambientale e sicurezza occupazionale, fornisco consulenza esperta in conformità SEVESO, normative ATEX e protezione dalle esplosioni per siti Seveso di livello superiore in tutta Europa. Attualmente lavoro come Consulente del Rischio presso AWN Consulting Ltd., aiutando le aziende nella produzione chimica, farmaceutica e manifatturiera a raggiungere la conformità normativa implementando robusti sistemi di gestione della sicurezza di processo.',
            'experience_title': 'Esperienza Professionale',
            'education_title': 'Formazione',
            'skills_title': 'Competenze Chiave',
            'certifications_title': 'Certificazioni',
            'experience': [
                ('Consulente del Rischio', 'AWN Consulting Ltd., Dublino, Irlanda', 'Ago 2023 - Presente', [
                    'Consulenza sulla Sicurezza di Processo e Rischio Ambientale',
                    'Consulenza SEVESO per più siti clienti',
                    'Preparazione Documento di Protezione dalle Esplosioni',
                    'Sviluppo e Aggiornamenti Rapporti di Sicurezza'
                ]),
                ('Ingegnere della Sicurezza di Processo', 'Guerbet, Irlanda', 'Ago 2022 - Giu 2023', [
                    'Sviluppato Sistema di Gestione della Sicurezza di Processo per sito Seveso di livello superiore',
                    'Condotto valutazioni di modifiche secondo Regolamenti COMAH',
                    'Guidato HAZOP e Valutazioni del Rischio di Sicurezza di Processo'
                ]),
                ('Specialista di Sicurezza e Ingegnere Ambientale', 'Seyir Akademi, Turchia', 'Feb 2019 - Ott 2021', [
                    'Consulenza SEVESO per clienti chimici e farmaceutici',
                    'Audit e ispezioni del sito di apparecchiature ATEX',
                    'Preparazione Documento di Protezione dalle Esplosioni'
                ])
            ],
            'education': [
                'Master - Salute e Sicurezza Occupazionale (Tesi), Üsküdar University',
                'Master - Salute e Sicurezza Occupazionale (Senza Tesi), Yeni Yüzyıl University',
                'Laurea in Ingegneria Ambientale, Ondokuz Mayıs University'
            ],
            'skills': [
                'Conformità SEVESO e COMAH',
                'Selezione e Ispezione Apparecchiature ATEX',
                'Sistemi di Gestione della Sicurezza di Processo',
                'Documentazione Protezione dalle Esplosioni',
                'Studi HAZOP',
                'Valutazione del Rischio',
                'ISO 60079, ISO 45001, ISO 14001'
            ]
        },
        'tr': {
            'name': 'SABİT BURAK CEBECİ',
            'title': 'Çevre Mühendisi & Süreç Güvenliği Uzmanı',
            'contact': 'İletişim Bilgileri',
            'email': 'E-posta: sabitburakcebeci@gmail.com',
            'phone': 'Telefon: +353 83 084 2944',
            'location': 'Konum: Dublin, İrlanda',
            'linkedin': 'LinkedIn: linkedin.com/in/sbtbrkcbc',
            'summary_title': 'Profesyonel Özet',
            'summary': 'Çevre mühendisliği ve iş güvenliği alanında 9 yılı aşkın uzman deneyime sahip olarak, Avrupa genelinde Üst Kademe Seveso tesisleri için SEVESO uyumluluğu, ATEX yönetmelikleri ve patlama koruması konularında uzman danışmanlık sağlıyorum. Şu anda AWN Consulting Ltd. bünyesinde Risk Danışmanı olarak görev yapmakta, kimyasal üretim, ilaç ve imalat sektörlerindeki şirketlerin mevzuat uyumluluğuna ulaşmalarına ve güçlü süreç güvenliği yönetim sistemleri uygulamalarına yardımcı oluyorum.',
            'experience_title': 'Profesyonel Deneyim',
            'education_title': 'Eğitim',
            'skills_title': 'Temel Yetkinlikler',
            'certifications_title': 'Sertifikalar',
            'experience': [
                ('Risk Danışmanı', 'AWN Consulting Ltd., Dublin, İrlanda', 'Ağu 2023 - Halen', [
                    'Süreç Güvenliği ve Çevresel Risk Danışmanlığı',
                    'Çoklu müşteri tesisleri için SEVESO Danışmanlığı',
                    'Patlama Koruması Dokümanı Hazırlama',
                    'Güvenlik Raporu Geliştirme ve Güncellemeler'
                ]),
                ('Süreç Güvenliği Mühendisi', 'Guerbet, İrlanda', 'Ağu 2022 - Haz 2023', [
                    'Üst Kademe Seveso tesisi için Süreç Güvenliği Yönetim Sistemi geliştirildi',
                    'COMAH Yönetmelikleri kapsamında modifikasyon değerlendirmeleri yürütüldü',
                    'HAZOP ve Süreç Güvenliği Risk Değerlendirmeleri yönetildi'
                ]),
                ('Güvenlik Uzmanı ve Çevre Mühendisi', 'Seyir Akademi, Türkiye', 'Şub 2019 - Eki 2021', [
                    'Kimyasal ve ilaç müşterileri için SEVESO danışmanlığı',
                    'ATEX ekipman saha denetimleri ve incelemeleri',
                    'Patlama Koruması Dokümanı hazırlama'
                ])
            ],
            'education': [
                'Yüksek Lisans - İş Sağlığı ve Güvenliği (Tezli), Üsküdar Üniversitesi',
                'Yüksek Lisans - İş Sağlığı ve Güvenliği (Tezsiz), Yeni Yüzyıl Üniversitesi',
                'Lisans - Çevre Mühendisliği, Ondokuz Mayıs Üniversitesi'
            ],
            'skills': [
                'SEVESO ve COMAH Uyumluluğu',
                'ATEX Ekipman Seçimi ve Denetimi',
                'Süreç Güvenliği Yönetim Sistemleri',
                'Patlama Koruması Dokümantasyonu',
                'HAZOP Çalışmaları',
                'Risk Değerlendirmesi',
                'ISO 60079, ISO 45001, ISO 14001'
            ]
        }
    }
    
    c = content[language]
    
    # Create PDF
    doc = SimpleDocTemplate(filename, pagesize=A4,
                           topMargin=0.75*inch, bottomMargin=0.75*inch,
                           leftMargin=0.75*inch, rightMargin=0.75*inch)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#059669'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#374151'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#059669'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    # Title
    story.append(Paragraph(c['name'], title_style))
    story.append(Paragraph(c['title'], subtitle_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Contact Information
    contact_data = [
        [c['email']],
        [c['phone']],
        [c['location']],
        [c['linkedin']]
    ]
    contact_table = Table(contact_data, colWidths=[6*inch])
    contact_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#4B5563')),
    ]))
    story.append(contact_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Summary
    story.append(Paragraph(c['summary_title'], heading_style))
    story.append(Paragraph(c['summary'], styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Skills
    story.append(Paragraph(c['skills_title'], heading_style))
    for skill in c['skills']:
        story.append(Paragraph(f"• {skill}", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Experience
    story.append(Paragraph(c['experience_title'], heading_style))
    for job_title, company, period, responsibilities in c['experience']:
        story.append(Paragraph(f"<b>{job_title}</b>", styles['Normal']))
        story.append(Paragraph(f"{company} | {period}", styles['Normal']))
        for resp in responsibilities:
            story.append(Paragraph(f"• {resp}", styles['Normal']))
        story.append(Spacer(1, 0.1*inch))
    
    # Education
    story.append(Paragraph(c['education_title'], heading_style))
    for edu in c['education']:
        story.append(Paragraph(f"• {edu}", styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print(f"CV generated: {filename}")

if __name__ == "__main__":
    cv_dir = "/app/backend/static/cv"
    os.makedirs(cv_dir, exist_ok=True)
    
    create_cv(f"{cv_dir}/cv_en.pdf", 'en')
    create_cv(f"{cv_dir}/cv_it.pdf", 'it')
    create_cv(f"{cv_dir}/cv_tr.pdf", 'tr')
    
    print("All CVs generated successfully!")
