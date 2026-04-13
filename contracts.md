# Backend Integration Contracts

## Overview
This document outlines the API contracts and integration plan for connecting the frontend portfolio website with the FastAPI backend and MongoDB database.

## Current Frontend Mock Data
Currently, all content is stored in `/app/frontend/src/translations.js` and served statically. No backend calls are being made except the initial health check.

## Backend Features to Implement

### 1. Contact Form Submission API
**Endpoint:** `POST /api/contact`

**Request Body:**
```json
{
  "name": "string",
  "email": "string",
  "message": "string",
  "language": "string" // en, it, or tr
}
```

**Response:**
```json
{
  "success": true,
  "message": "Message sent successfully",
  "id": "message_id"
}
```

**MongoDB Collection:** `contact_messages`
**Schema:**
- name: String
- email: String
- message: String
- language: String
- created_at: DateTime
- read: Boolean (default: false)

### 2. CV Download API
**Endpoint:** `GET /api/cv/download`

**Query Parameters:**
- `lang`: Language code (en, it, tr)

**Response:** PDF file download

**Implementation:**
- Store CV PDFs in `/app/backend/static/cv/` directory
- Files: `cv_en.pdf`, `cv_it.pdf`, `cv_tr.pdf`
- Return file as downloadable response

### 3. Analytics/View Counter (Optional)
**Endpoint:** `POST /api/analytics/page-view`

**Request Body:**
```json
{
  "page": "string",
  "language": "string",
  "referrer": "string"
}
```

**MongoDB Collection:** `page_views`

## Frontend Integration Points

### 1. Contact Component
**File:** `/app/frontend/src/components/Contact.jsx`

**Current Mock Behavior:**
- Line 26-37: Form submission shows toast alert
- Need to replace with actual API call

**Integration:**
```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  if (!formData.name || !formData.email || !formData.message) {
    toast({ title: 'Error', description: t.contact.error, variant: 'destructive' });
    return;
  }
  
  try {
    const response = await axios.post(`${API}/contact`, {
      ...formData,
      language
    });
    toast({ title: 'Success', description: t.contact.success });
    setFormData({ name: '', email: '', message: '' });
  } catch (error) {
    toast({ title: 'Error', description: 'Failed to send message', variant: 'destructive' });
  }
};
```

### 2. Hero Component
**File:** `/app/frontend/src/components/Hero.jsx`

**Current Mock Behavior:**
- Line 21-24: CV download shows alert
- Need to replace with actual API call

**Integration:**
```javascript
const handleDownloadCV = () => {
  window.open(`${API}/cv/download?lang=${language}`, '_blank');
};
```

## Backend File Structure

```
/app/backend/
├── server.py (main FastAPI app)
├── models/
│   ├── contact.py (Contact message model)
│   └── analytics.py (Analytics model - optional)
├── routes/
│   ├── contact.py (Contact form routes)
│   └── cv.py (CV download routes)
└── static/
    └── cv/
        ├── cv_en.pdf
        ├── cv_it.pdf
        └── cv_tr.pdf
```

## Implementation Steps

### Phase 1: Contact Form Backend
1. Create MongoDB model for contact messages
2. Create POST endpoint for contact form
3. Add email validation
4. Test with curl
5. Integrate frontend Contact component
6. Test end-to-end

### Phase 2: CV Download
1. Create CV PDFs (one for each language)
2. Create static file serving endpoint
3. Implement download route
4. Integrate frontend Hero component
5. Test downloads

### Phase 3: Testing
1. Test contact form with all three languages
2. Test CV downloads for all languages
3. Verify MongoDB storage
4. Test error handling

## Environment Variables
No new environment variables needed. Using existing:
- `MONGO_URL` - Already configured
- `REACT_APP_BACKEND_URL` - Already configured

## Notes
- All translations are already complete in `translations.js`
- No authentication required for contact form (public)
- Consider adding rate limiting for contact form to prevent spam
- CV files need to be created/uploaded manually
