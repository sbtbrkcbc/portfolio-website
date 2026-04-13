#!/usr/bin/env python3
"""
Backend API Testing for Sabit Burak Cebeci's Portfolio Website
Tests all backend APIs including contact form, CV download, and health check
"""

import requests
import json
import os
from pathlib import Path

# Get backend URL from environment
frontend_env_path = Path("/app/frontend/.env")
backend_url = None

if frontend_env_path.exists():
    with open(frontend_env_path, 'r') as f:
        for line in f:
            if line.startswith('REACT_APP_BACKEND_URL='):
                backend_url = line.split('=', 1)[1].strip()
                break

if not backend_url:
    print("❌ ERROR: Could not find REACT_APP_BACKEND_URL in frontend/.env")
    exit(1)

print(f"🔗 Testing backend at: {backend_url}")

# Test results tracking
test_results = {
    "health_check": {"passed": False, "details": ""},
    "contact_form_valid": {"passed": False, "details": ""},
    "contact_form_italian": {"passed": False, "details": ""},
    "contact_form_turkish": {"passed": False, "details": ""},
    "contact_form_invalid_email": {"passed": False, "details": ""},
    "contact_form_missing_fields": {"passed": False, "details": ""},
    "cv_download_en": {"passed": False, "details": ""},
    "cv_download_it": {"passed": False, "details": ""},
    "cv_download_tr": {"passed": False, "details": ""},
    "cv_download_invalid": {"passed": False, "details": ""}
}

def test_health_check():
    """Test the health check endpoint"""
    print("\n🔍 Testing Health Check API...")
    try:
        response = requests.get(f"{backend_url}/api/", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("message") == "Hello World":
                test_results["health_check"]["passed"] = True
                test_results["health_check"]["details"] = "✅ Health check passed"
                print("✅ Health check API working correctly")
            else:
                test_results["health_check"]["details"] = f"❌ Unexpected response: {data}"
                print(f"❌ Health check returned unexpected data: {data}")
        else:
            test_results["health_check"]["details"] = f"❌ HTTP {response.status_code}: {response.text}"
            print(f"❌ Health check failed with status {response.status_code}")
            
    except Exception as e:
        test_results["health_check"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"❌ Health check failed: {str(e)}")

def test_contact_form():
    """Test the contact form API with various scenarios"""
    print("\n🔍 Testing Contact Form API...")
    
    # Test 1: Valid English contact form
    print("  📝 Testing valid English contact form...")
    try:
        valid_data = {
            "name": "Marco Rossi",
            "email": "marco.rossi@example.com",
            "message": "Hello, I'm interested in your portfolio and would like to discuss potential collaboration opportunities.",
            "language": "en"
        }
        
        response = requests.post(f"{backend_url}/api/contact", 
                               json=valid_data, 
                               headers={"Content-Type": "application/json"},
                               timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("success") == True:
                test_results["contact_form_valid"]["passed"] = True
                test_results["contact_form_valid"]["details"] = "✅ Valid contact form submission successful"
                print("    ✅ Valid English contact form submission successful")
            else:
                test_results["contact_form_valid"]["details"] = f"❌ API returned success=false: {data}"
                print(f"    ❌ API returned success=false: {data}")
        else:
            test_results["contact_form_valid"]["details"] = f"❌ HTTP {response.status_code}: {response.text}"
            print(f"    ❌ Valid contact form failed with status {response.status_code}: {response.text}")
            
    except Exception as e:
        test_results["contact_form_valid"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ Valid contact form test failed: {str(e)}")
    
    # Test 2: Italian language contact form
    print("  📝 Testing Italian language contact form...")
    try:
        italian_data = {
            "name": "Giuseppe Verdi",
            "email": "giuseppe.verdi@example.it",
            "message": "Ciao, sono interessato al tuo portfolio e vorrei discutere di possibili opportunità di collaborazione.",
            "language": "it"
        }
        
        response = requests.post(f"{backend_url}/api/contact", 
                               json=italian_data, 
                               headers={"Content-Type": "application/json"},
                               timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("success") == True:
                test_results["contact_form_italian"]["passed"] = True
                test_results["contact_form_italian"]["details"] = "✅ Italian contact form submission successful"
                print("    ✅ Italian contact form submission successful")
            else:
                test_results["contact_form_italian"]["details"] = f"❌ API returned success=false: {data}"
                print(f"    ❌ Italian contact form API returned success=false: {data}")
        else:
            test_results["contact_form_italian"]["details"] = f"❌ HTTP {response.status_code}: {response.text}"
            print(f"    ❌ Italian contact form failed with status {response.status_code}: {response.text}")
            
    except Exception as e:
        test_results["contact_form_italian"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ Italian contact form test failed: {str(e)}")
    
    # Test 3: Turkish language contact form
    print("  📝 Testing Turkish language contact form...")
    try:
        turkish_data = {
            "name": "Ahmet Yılmaz",
            "email": "ahmet.yilmaz@example.com.tr",
            "message": "Merhaba, portföyünüzle ilgileniyorum ve potansiyel işbirliği fırsatlarını görüşmek istiyorum.",
            "language": "tr"
        }
        
        response = requests.post(f"{backend_url}/api/contact", 
                               json=turkish_data, 
                               headers={"Content-Type": "application/json"},
                               timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("success") == True:
                test_results["contact_form_turkish"]["passed"] = True
                test_results["contact_form_turkish"]["details"] = "✅ Turkish contact form submission successful"
                print("    ✅ Turkish contact form submission successful")
            else:
                test_results["contact_form_turkish"]["details"] = f"❌ API returned success=false: {data}"
                print(f"    ❌ Turkish contact form API returned success=false: {data}")
        else:
            test_results["contact_form_turkish"]["details"] = f"❌ HTTP {response.status_code}: {response.text}"
            print(f"    ❌ Turkish contact form failed with status {response.status_code}: {response.text}")
            
    except Exception as e:
        test_results["contact_form_turkish"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ Turkish contact form test failed: {str(e)}")
    
    # Test 4: Invalid email format
    print("  📝 Testing invalid email format...")
    try:
        invalid_email_data = {
            "name": "Test User",
            "email": "invalid-email-format",
            "message": "This should fail due to invalid email",
            "language": "en"
        }
        
        response = requests.post(f"{backend_url}/api/contact", 
                               json=invalid_email_data, 
                               headers={"Content-Type": "application/json"},
                               timeout=10)
        
        # Should return 422 for validation error or 400 for bad request
        if response.status_code in [400, 422]:
            test_results["contact_form_invalid_email"]["passed"] = True
            test_results["contact_form_invalid_email"]["details"] = "✅ Invalid email properly rejected"
            print("    ✅ Invalid email format properly rejected")
        elif response.status_code == 200:
            data = response.json()
            if data.get("success") == False:
                test_results["contact_form_invalid_email"]["passed"] = True
                test_results["contact_form_invalid_email"]["details"] = "✅ Invalid email properly rejected with success=false"
                print("    ✅ Invalid email format properly rejected with success=false")
            else:
                test_results["contact_form_invalid_email"]["details"] = f"❌ Invalid email was accepted: {data}"
                print(f"    ❌ Invalid email format was incorrectly accepted: {data}")
        else:
            test_results["contact_form_invalid_email"]["details"] = f"❌ Unexpected status {response.status_code}: {response.text}"
            print(f"    ❌ Unexpected response for invalid email: {response.status_code}")
            
    except Exception as e:
        test_results["contact_form_invalid_email"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ Invalid email test failed: {str(e)}")
    
    # Test 5: Missing required fields
    print("  📝 Testing missing required fields...")
    try:
        missing_fields_data = {
            "name": "Test User",
            # Missing email, message, and language
        }
        
        response = requests.post(f"{backend_url}/api/contact", 
                               json=missing_fields_data, 
                               headers={"Content-Type": "application/json"},
                               timeout=10)
        
        # Should return 422 for validation error or 400 for bad request
        if response.status_code in [400, 422]:
            test_results["contact_form_missing_fields"]["passed"] = True
            test_results["contact_form_missing_fields"]["details"] = "✅ Missing fields properly rejected"
            print("    ✅ Missing required fields properly rejected")
        elif response.status_code == 200:
            data = response.json()
            if data.get("success") == False:
                test_results["contact_form_missing_fields"]["passed"] = True
                test_results["contact_form_missing_fields"]["details"] = "✅ Missing fields properly rejected with success=false"
                print("    ✅ Missing required fields properly rejected with success=false")
            else:
                test_results["contact_form_missing_fields"]["details"] = f"❌ Missing fields were accepted: {data}"
                print(f"    ❌ Missing required fields were incorrectly accepted: {data}")
        else:
            test_results["contact_form_missing_fields"]["details"] = f"❌ Unexpected status {response.status_code}: {response.text}"
            print(f"    ❌ Unexpected response for missing fields: {response.status_code}")
            
    except Exception as e:
        test_results["contact_form_missing_fields"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ Missing fields test failed: {str(e)}")

def test_cv_download():
    """Test the CV download API"""
    print("\n🔍 Testing CV Download API...")
    
    # Test 1: English CV download
    print("  📄 Testing English CV download...")
    try:
        response = requests.get(f"{backend_url}/api/cv/download?lang=en", timeout=10)
        
        if response.status_code == 200:
            if response.headers.get('content-type') == 'application/pdf':
                test_results["cv_download_en"]["passed"] = True
                test_results["cv_download_en"]["details"] = f"✅ English CV download successful ({len(response.content)} bytes)"
                print(f"    ✅ English CV download successful ({len(response.content)} bytes)")
            else:
                test_results["cv_download_en"]["details"] = f"❌ Wrong content type: {response.headers.get('content-type')}"
                print(f"    ❌ English CV wrong content type: {response.headers.get('content-type')}")
        else:
            test_results["cv_download_en"]["details"] = f"❌ HTTP {response.status_code}: {response.text}"
            print(f"    ❌ English CV download failed with status {response.status_code}")
            
    except Exception as e:
        test_results["cv_download_en"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ English CV download test failed: {str(e)}")
    
    # Test 2: Italian CV download
    print("  📄 Testing Italian CV download...")
    try:
        response = requests.get(f"{backend_url}/api/cv/download?lang=it", timeout=10)
        
        if response.status_code == 200:
            if response.headers.get('content-type') == 'application/pdf':
                test_results["cv_download_it"]["passed"] = True
                test_results["cv_download_it"]["details"] = f"✅ Italian CV download successful ({len(response.content)} bytes)"
                print(f"    ✅ Italian CV download successful ({len(response.content)} bytes)")
            else:
                test_results["cv_download_it"]["details"] = f"❌ Wrong content type: {response.headers.get('content-type')}"
                print(f"    ❌ Italian CV wrong content type: {response.headers.get('content-type')}")
        else:
            test_results["cv_download_it"]["details"] = f"❌ HTTP {response.status_code}: {response.text}"
            print(f"    ❌ Italian CV download failed with status {response.status_code}")
            
    except Exception as e:
        test_results["cv_download_it"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ Italian CV download test failed: {str(e)}")
    
    # Test 3: Turkish CV download
    print("  📄 Testing Turkish CV download...")
    try:
        response = requests.get(f"{backend_url}/api/cv/download?lang=tr", timeout=10)
        
        if response.status_code == 200:
            if response.headers.get('content-type') == 'application/pdf':
                test_results["cv_download_tr"]["passed"] = True
                test_results["cv_download_tr"]["details"] = f"✅ Turkish CV download successful ({len(response.content)} bytes)"
                print(f"    ✅ Turkish CV download successful ({len(response.content)} bytes)")
            else:
                test_results["cv_download_tr"]["details"] = f"❌ Wrong content type: {response.headers.get('content-type')}"
                print(f"    ❌ Turkish CV wrong content type: {response.headers.get('content-type')}")
        else:
            test_results["cv_download_tr"]["details"] = f"❌ HTTP {response.status_code}: {response.text}"
            print(f"    ❌ Turkish CV download failed with status {response.status_code}")
            
    except Exception as e:
        test_results["cv_download_tr"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ Turkish CV download test failed: {str(e)}")
    
    # Test 4: Invalid language code
    print("  📄 Testing invalid language code...")
    try:
        response = requests.get(f"{backend_url}/api/cv/download?lang=invalid", timeout=10)
        
        if response.status_code == 404:
            test_results["cv_download_invalid"]["passed"] = True
            test_results["cv_download_invalid"]["details"] = "✅ Invalid language code properly rejected with 404"
            print("    ✅ Invalid language code properly rejected with 404")
        elif response.status_code == 422:
            test_results["cv_download_invalid"]["passed"] = True
            test_results["cv_download_invalid"]["details"] = "✅ Invalid language code properly rejected with 422"
            print("    ✅ Invalid language code properly rejected with 422")
        else:
            test_results["cv_download_invalid"]["details"] = f"❌ Unexpected status {response.status_code}: {response.text}"
            print(f"    ❌ Invalid language code returned unexpected status: {response.status_code}")
            
    except Exception as e:
        test_results["cv_download_invalid"]["details"] = f"❌ Connection error: {str(e)}"
        print(f"    ❌ Invalid language test failed: {str(e)}")

def print_summary():
    """Print test summary"""
    print("\n" + "="*80)
    print("🎯 BACKEND API TEST SUMMARY")
    print("="*80)
    
    passed_tests = sum(1 for result in test_results.values() if result["passed"])
    total_tests = len(test_results)
    
    print(f"\n📊 Overall Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! Backend APIs are working correctly.")
    else:
        print("⚠️  Some tests failed. See details below:")
    
    print("\n📋 Detailed Results:")
    for test_name, result in test_results.items():
        status = "✅ PASS" if result["passed"] else "❌ FAIL"
        print(f"  {status} - {test_name}")
        if not result["passed"]:
            print(f"    Details: {result['details']}")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    print("🚀 Starting Backend API Tests for Sabit Burak Cebeci's Portfolio")
    print("="*80)
    
    # Run all tests
    test_health_check()
    test_contact_form()
    test_cv_download()
    
    # Print summary
    print_summary()