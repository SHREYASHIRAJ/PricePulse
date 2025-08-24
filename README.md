# PricePulse - Price Comparison App

A beautiful web application that compares prices of products across multiple e-commerce platforms including Flipkart, Amazon, and Reliance Digital.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-Beta-orange" alt="Status">
</p>

## 🌟 Features

- **Beautiful Modern UI**: Sleek design with gradient backgrounds and smooth animations
- **Dual Method Approach**: Switch between web scraping and API methods
- **Real-time Price Comparison**: Compare prices across multiple platforms instantly
- **Intelligent Retry System**: Smart retry functionality with exponential backoff
- **Generic Search Fallback**: Alternative search when specific queries fail
- **Responsive Design**: Works beautifully on all devices
- **Comprehensive Error Handling**: Clear error messages with actionable advice
- **Platform-specific Styling**: Unique colors for each e-commerce platform

## 🚀 Quick Start

1. Clone or download this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python backend/app.py
   ```
4. Open your browser and go to `http://localhost:5000`

## 🛒 Supported Platforms

- Flipkart (Web Scraping)
- Amazon (Web Scraping)
- Reliance Digital (Web Scraping)

## 🎨 Beautiful UI Features

PricePulse features a modern, visually appealing interface with:

- **Gradient Headers**: Beautiful color gradients in the header
- **Animated Loading**: Spinning loader with status messages
- **Platform Icons**: Unique icons and colors for each platform
- **Hover Effects**: Smooth animations on interactive elements
- **Responsive Cards**: Elegant product display cards with hover effects
- **Method Switching**: Toggle between scraping and API methods

## 🔧 Two Approaches to Data Retrieval

### 1. Web Scraping (Default)
- **How it works**: Directly extracts data from website HTML
- **Pros**: No API keys required, can access all public data
- **Cons**: Sites may block requests, structure changes break scrapers
- **Best for**: When API access is not available

### 2. API Method (Conceptual)
- **How it works**: Uses official e-commerce APIs when available
- **Pros**: More reliable, faster, less likely to break
- **Cons**: Requires API keys, limited availability for Indian e-commerce
- **Best for**: When API credentials are available

**Note**: Most Indian e-commerce platforms don't have publicly available APIs for price comparison. The API method is included as a conceptual implementation for future use.

## 🔄 Enhanced Retry Functionality

### Backend Improvements
- **Exponential Backoff**: Automatic retries with increasing delays (2s, 4s, 8s)
- **Smart Validation**: Checks if retry results contain actual data
- **Rate Limiting Prevention**: Built-in delays to prevent overwhelming requests

### Frontend Improvements
- **Persistent Query Storage**: Remembers last search for retries
- **Visual Feedback**: Loading messages during retry delays
- **Dual Retry Options**: "Retry Search" and "Try Generic Search" buttons
- **Method Switching**: Easily switch between scraping and API methods
- **Animated Transitions**: Smooth animations between states

## 🛠️ Technical Details

### Scraper Enhancements
- **Multiple CSS Selectors**: 3-5 fallback selectors per platform
- **Random User-Agents**: Rotates between browser identifiers
- **Human-like Delays**: 1-3 second random delays between requests
- **Extended Timeout**: 25-second timeout for slow responses
- **Comprehensive Error Handling**: Specific messages for different failures

### Frontend Technologies
- **Modern CSS**: CSS variables, flexbox, and grid layouts
- **Font Awesome Icons**: Beautiful iconography throughout
- **Responsive Design**: Mobile-first approach with media queries
- **Smooth Animations**: CSS transitions and keyframe animations

## 📱 User Experience Improvements

1. **Clear Visual Hierarchy**: Important information stands out
2. **Helpful Tips Section**: Guiding users for better results
3. **Error Recovery**: Multiple paths to success when errors occur
4. **Loading States**: Visual feedback during long operations
5. **Accessible Design**: Proper contrast and readable fonts
6. **Method Switching**: Choose between scraping and API approaches

## 🐛 Troubleshooting Common Issues

### "Error fetching details" Solutions

1. **529 Server Errors (Flipkart)**: Anti-bot protection - try again later
2. **No Products Found (Reliance)**: Site structure may have changed
3. **Wait and Retry**: Built-in 3-second delay before retries
4. **Generic Search**: Alternative search with common terms
5. **Method Switching**: Try switching between scraping and API methods
6. **Rate Limiting**: Automatic delays prevent overwhelming servers

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgements

- Flask for the web framework
- BeautifulSoup for web scraping
- Font Awesome for icons