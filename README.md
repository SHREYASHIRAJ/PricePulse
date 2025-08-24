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

## Overview

PricePulse is a price comparison tool that helps you find the best deals across major Indian e-commerce platforms. It features a modern interface and dual data retrieval methods for simple, fast, and visually appealing price comparisons.

## Key Features

- **Dual Data Retrieval**: Web scraping (default) and API methods
- **Real-time Comparison**: Instant price comparisons across platforms
- **Smart Retry System**: Automatic retry mechanisms with exponential backoff
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Error Handling**: Clear error messages and recovery options

## Supported Platforms

| Platform | Method | Status |
|----------|--------|--------|
| Flipkart | Scraping | Rate Limited |
| Amazon India | Scraping | Working |
| Reliance Digital | Scraping | Structure Changes |

## Prerequisites

- Python 3.7 or higher
- Windows, macOS, or Linux
- Internet connection
- Modern web browser

## Installation

1. Clone or download the repository:
```bash
cd price-compare-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the application:
```bash
python backend/app.py
```

Or double-click `start_pricepulse.bat` on Windows.

Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

## How to Use

1. Enter a product name in the search box
2. Choose between Web Scraping or API method
3. Click "Search" or press Enter
4. Compare prices across platforms
5. Click product links to visit stores

## Troubleshooting

- **Flipkart 529 Error**: Anti-bot protection - wait 2-3 minutes and retry
- **No Products Found**: Try a different search term
- **Connection Failed**: Ensure the backend server is running
- **Slow Responses**: Normal for web scraping

## License

MIT License

Copyright (c) 2023 PricePulse