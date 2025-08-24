# PricePulse - Minimal Directory Structure

## Essential Files Only

```
price-compare-app/
├── backend/
│   ├── app.py          # Flask web server
│   └── scraper.py      # Web scraping logic
├── frontend/
│   ├── index.html      # Beautiful UI interface
│   └── favicon.ico     # Application icon
├── requirements.txt    # Python dependencies
├── README.md          # Project overview
└── start_pricepulse.bat # Startup script
```

## File Purposes

1. **backend/app.py** - Runs the Flask web server that serves the frontend and handles API requests
2. **backend/scraper.py** - Contains the web scraping logic for Flipkart, Amazon, and Reliance Digital
3. **frontend/index.html** - The beautiful modern user interface with gradients and animations
4. **requirements.txt** - Lists the Python packages needed (Flask, requests, beautifulsoup4, flask-cors)
5. **README.md** - Basic project information
6. **start_pricepulse.bat** - Double-click to start the application

## How to Use

1. Double-click `start_pricepulse.bat` to start the server
2. Open browser and go to `http://localhost:5000`
3. Search for products and compare prices