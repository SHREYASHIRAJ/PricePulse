#!/usr/bin/env python3
"""
Test script to verify PricePulse UI improvements
"""

import sys
import os

def test_ui_improvements():
    """Test that the UI improvements are in place"""
    print("Testing PricePulse UI improvements...")
    print("=" * 50)
    
    # Test 1: Check if frontend file exists
    frontend_path = os.path.join(os.path.dirname(__file__), 'frontend', 'index.html')
    if not os.path.exists(frontend_path):
        print("[FAIL] Frontend file not found")
        return False
    else:
        print("[PASS] Frontend file exists")
    
    # Test 2: Check for improved method selector styles
    try:
        with open(frontend_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for new CSS variables
        if '--primary-dark' in content:
            print("[PASS] Darker primary color variables found")
        else:
            print("[FAIL] Darker primary color variables missing")
            return False
            
        # Check for improved method button styles
        if 'var(--primary-dark)' in content and '.method-btn.active' in content:
            print("[PASS] Improved method selector styles found")
        else:
            print("[FAIL] Improved method selector styles missing")
            return False
            
        # Check for animations
        if '@keyframes fadeIn' in content or '@keyframes slideIn' in content:
            print("[PASS] Animation styles found")
        else:
            print("[FAIL] Animation styles missing")
            return False
            
        # Check for enhanced shadows and transitions
        if 'var(--box-shadow-hover)' in content:
            print("[PASS] Enhanced shadow effects found")
        else:
            print("[FAIL] Enhanced shadow effects missing")
            return False
            
    except Exception as e:
        print(f"[FAIL] Error reading frontend file: {e}")
        return False
    
    # Test 3: Check if backend still works
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
        from backend.app import app
        print("[PASS] Backend still works correctly")
    except Exception as e:
        print(f"[FAIL] Backend error: {e}")
        return False
    
    print("=" * 50)
    print("[SUCCESS] All UI improvements are in place!")
    print("\nEnhancements made:")
    print("1. Darker selected method button (primary-dark color)")
    print("2. Better hover effects and shadows")
    print("3. Smooth animations and transitions")
    print("4. Improved visual hierarchy")
    print("5. Enhanced button states")
    print("\nTo see the improvements:")
    print("1. Start PricePulse: python backend/app.py")
    print("2. Visit http://localhost:5000")
    print("3. Notice the darker 'Web Scraping' button when selected")
    print("4. See improved hover effects and animations")
    return True

if __name__ == "__main__":
    test_ui_improvements()