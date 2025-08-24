from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
import time

# Add the current directory to sys.path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scraper import get_price_comparison
try:
    from api_client import get_price_comparison_api
    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    # Serve the frontend HTML file with cross-platform path handling
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    frontend_path = os.path.join(project_root, 'frontend', 'index.html')
    
    try:
        with open(frontend_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return jsonify({"error": "Frontend file not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Error reading frontend file: {str(e)}"}), 500

@app.route('/compare', methods=['GET'])
def compare_prices():
    query = request.args.get('query')
    method = request.args.get('method', 'scrape')  # 'scrape' or 'api'
    
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400
    
    # Sanitize query
    query = query.strip()
    if not query:
        return jsonify({"error": "Query parameter cannot be empty"}), 400
    
    # Add a small delay to help with rate limiting
    time.sleep(0.5)
    
    try:
        if method == 'api' and API_AVAILABLE:
            results = get_price_comparison_api(query)
        else:
            results = get_price_comparison(query)
        
        # Check if all scrapers failed
        all_failed = True
        if isinstance(results, dict):
            for key, value in results.items():
                if isinstance(value, list) and len(value) > 0:
                    # Check if all items are errors
                    all_errors = all(isinstance(item, dict) and 'error' in item for item in value)
                    if not all_errors:
                        all_failed = False
                        break
        
        if all_failed:
            error_msg = "Unable to fetch data from any e-commerce platform. "
            if method == 'api' and API_AVAILABLE:
                error_msg += "Try switching to scraping method."
            else:
                error_msg += "Please try again later or try a different search term."
            return jsonify({"error": error_msg}), 503
        
        return jsonify(results)
    except ImportError as e:
        return jsonify({"error": "Internal server configuration error"}), 500
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "api_available": API_AVAILABLE,
        "message": "PricePulse server is running"
    })

if __name__ == '__main__':
    print("=========================================")
    print("  PricePulse - Price Comparison App")
    print("=========================================")
    print("Starting server on http://127.0.0.1:5000")
    print("API support:", "Available" if API_AVAILABLE else "Not available (using web scraping)")
    print("Press CTRL+C to stop the server")
    print("")
    app.run(debug=True, host='127.0.0.1', port=5000)
