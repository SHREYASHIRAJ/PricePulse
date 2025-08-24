# PricePulse 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Build-Stable-brightgreen" alt="Build Status">
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-orange" alt="Platform">
</p>

<p align="center">
  <strong>A modern price comparison application for Indian e-commerce platforms</strong>
</p>

##  Overview

PricePulse is an price comparison tool that helps you find the best deals across major Indian e-commerce platforms. With its modern interface and dual data retrieval methods, PricePulse makes price comparison simple, fast, and visually appealing.

##  Key Features

###  Dual Data Retrieval Methods
- **Web Scraping**: Direct HTML parsing for real-time data
- **API Method**: Structured API calls (conceptual implementation)
- **Method Switching**: Easily toggle between approaches
- **Intelligent Fallbacks**: Automatic retry mechanisms

###  Enhanced Functionality
- **Real-time Comparison**: Instant price comparisons across platforms
- **Smart Retry System**: Exponential backoff for failed requests
- **Generic Search**: Fallback search for better results
- **Comprehensive Error Handling**: Clear, actionable error messages

##  Supported Platforms

| Platform | Method | Status |
|----------|--------|--------|
| 🛒 Flipkart | Scraping | ⚠️ Rate Limited |
| 🛒 Amazon India | Scraping | ✅ Working |
| 🛒 Reliance Digital | Scraping | ⚠️ Structure Changes |

##  Prerequisites

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Internet Connection**: Required for data retrieval
- **Browser**: Any modern web browser

##  Quick Start

### 1. Installation
```bash
# Clone the repository (or navigate to your download folder)
cd price-compare-app

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Application
```bash
# Start the server
python backend/app.py

# Open your browser and navigate to
http://localhost:5000
```

### 3. Using PricePulse
1. Enter a product name in the search box
2. Choose between Web Scraping or API method
3. Click "Search" or press Enter
4. Compare prices across platforms
5. Click product links to visit the store

##  Data Flow

```
User Input → Method Selection → Data Retrieval → Result Processing → UI Display
```

##  User Interface

### Modern Dashboard
- **Gradient Header**: Beautiful purple-to-blue gradient
- **Method Toggle**: Easy switching between scraping and API
- **Search Interface**: Clean, intuitive search experience
- **Result Cards**: Platform-specific styling with hover effects

### Responsive Design
```
Desktop: 3-4 columns
Tablet: 2 columns
Mobile: 1 column
```

##  Technical Architecture

### Backend (Python/Flask)
```
backend/
├── app.py          # Flask server and routes
├── scraper.py      # Web scraping logic
└── api_client.py   # API client implementation
```

### Frontend (HTML/CSS/JS)
```
frontend/
├── index.html      # Main interface
└── favicon.ico     # Application icon
```

### Key Libraries
- **Flask**: Web framework
- **BeautifulSoup**: HTML parsing
- **Requests**: HTTP library
- **Flask-CORS**: Cross-origin resource sharing

##  Data Retrieval Methods

### Web Scraping Approach
```
Pros:
✓ No API keys required
✓ Access to all public data
✓ Real-time information

Cons:
⚠ Sites may block requests
⚠ Structure changes break scrapers
⚠ Rate limiting issues
```

### API Method Approach
```
Pros:
✓ More reliable and faster
✓ Structured data format
✓ Less likely to break

Cons:
⚠ Requires API credentials
⚠ Limited public APIs in India
⚠ Rate limits and quotas
```

##  Troubleshooting Guide

### Common Issues

| Issue | Solution |
|-------|----------|
| **529 Server Error (Flipkart)** | Anti-bot protection - try again later |
| **No Products Found (Reliance)** | Site structure may have changed |
| **Connection Failed** | Ensure backend server is running |
| **Slow Responses** | Add delays between requests |

### Best Practices
1. **Search Timing**: Use during off-peak hours
2. **Search Terms**: Try generic terms (e.g., "phone" vs "iPhone 15")
3. **Rate Limiting**: Wait between searches
4. **Method Switching**: Try both scraping and API methods

##  Development

### Project Structure
```
price-compare-app/
├── backend/
│   ├── app.py          # Flask application
│   ├── scraper.py      # Web scraping logic
│   └── api_client.py   # API client (conceptual)
├── frontend/
│   ├── index.html      # Main interface
│   └── favicon.ico     # Application icon
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

### Running Tests
```bash
# Test backend components
python -c "from backend.app import app; print('App loads successfully')"

# Verify scraping functionality
python -c "from backend.scraper import get_price_comparison; print('Scraper loads successfully')"

# Check API client
python -c "from backend.api_client import get_price_comparison_api; print('API client loads successfully')"
```


##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2023 PricePulse

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```
