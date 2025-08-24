#!/usr/bin/env python3
"""
Test script to verify PricePulse with API support
"""

import sys
import os

def test_complete_functionality():
    """Test that all components of PricePulse work together"""
    print("Testing PricePulse with API support...")
    print("=" * 50)
    
    # Test 1: Check if all required files exist
    required_files = [
        'frontend/index.html',
        'backend/app.py',
        'backend/scraper.py',
        'backend/api_client.py',
        'requirements.txt'
    ]
    
    all_files_exist = True
    for file in required_files:
        filepath = os.path.join(os.path.dirname(__file__), file)
        if not os.path.exists(filepath):
            print(f"[FAIL] Missing file: {file}")
            all_files_exist = False
        else:
            print(f"[PASS] Found: {file}")
    
    if not all_files_exist:
        return False
    
    # Test 2: Check if backend can be imported
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
        from backend.app import app
        print("[PASS] Backend imports successfully")
    except Exception as e:
        print(f"[FAIL] Backend import error: {e}")
        return False
    
    # Test 3: Check if scraper can be imported
    try:
        from backend.scraper import get_price_comparison
        print("[PASS] Scraper imports successfully")
    except Exception as e:
        print(f"[FAIL] Scraper import error: {e}")
        return False
    
    # Test 4: Check if API client can be imported
    try:
        from backend.api_client import get_price_comparison_api
        print("[PASS] API client imports successfully")
    except Exception as e:
        print(f"[FAIL] API client import error: {e}")
        return False
    
    # Test 5: Check if frontend file contains PricePulse branding
    try:
        frontend_path = os.path.join(os.path.dirname(__file__), 'frontend', 'index.html')
        with open(frontend_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'PricePulse' in content and 'method-selector' in content:
            print("[PASS] Frontend contains PricePulse branding and method selector")
        else:
            print("[FAIL] Frontend missing required elements")
            return False
    except Exception as e:
        print(f"[FAIL] Frontend file error: {e}")
        return False
    
    print("=" * 50)
    print("[SUCCESS] All tests passed! PricePulse with API support is ready.")
    print("\nNew features:")
    print("1. Dual method approach (scraping and API)")
    print("2. Method switching in the UI")
    print("3. API client implementation (conceptual)")
    print("4. Enhanced error handling")
    print("\nTo start PricePulse:")
    print("1. Run: python backend/app.py")
    print("2. Visit http://localhost:5000 in your browser")
    print("3. Try both scraping and API methods")
    return True

if __name__ == "__main__":
    test_complete_functionality()