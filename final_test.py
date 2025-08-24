#!/usr/bin/env python3

import sys
import os

def test_complete_package():
    print("Final PricePulse Verification Test")
    print("=" * 50)
    
    # Test 1: Directory structure
    required_paths = [
        'backend/app.py',
        'backend/scraper.py', 
        'backend/api_client.py',
        'frontend/index.html',
        'requirements.txt',
        'README.md'
    ]
    
    print("Checking directory structure...")
    all_good = True
    for path in required_paths:
        full_path = os.path.join(os.path.dirname(__file__), path)
        if os.path.exists(full_path):
            print(f"  OK {path}")
        else:
            print(f"  ERROR {path}")
            all_good = False
    
    # Test 2: Backend components
    print("\nTesting backend components...")
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
        
        from backend.app import app
        print("  OK Flask app loads successfully")
        
        from backend.scraper import get_price_comparison
        print("  OK Scraper module loads successfully")
        
        from backend.api_client import get_price_comparison_api
        print("  OK API client loads successfully")
        
    except Exception as e:
        print(f"  ERROR Backend error: {e}")
        all_good = False
    
    # Test 3: README improvements
    print("\nTesting README...")
    try:
        readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '# PricePulse' in content and 'Key Features' in content:
            print("  OK README is professionally formatted")
        else:
            print("  ERROR README needs improvement")
            all_good = False
                
    except Exception as e:
        print(f"  ERROR README error: {e}")
        all_good = False
    
    print("\n" + "=" * 50)
    if all_good:
        print("SUCCESS! PricePulse is ready to go!")
        print("\nQuick Start:")
        print("1. Run: python backend/app.py")
        print("2. Visit: http://localhost:5000")
        return True
    else:
        print("Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = test_complete_package()
    sys.exit(0 if success else 1)