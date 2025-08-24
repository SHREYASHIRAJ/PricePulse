import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urljoin, quote_plus
import random

def scrape_with_retry(scraper_func, query, max_retries=2):
    """Helper function to retry scraping with exponential backoff"""
    for attempt in range(max_retries + 1):
        try:
            result = scraper_func(query)
            # Check if result contains actual data (not just errors)
            if isinstance(result, list):
                # Check if all items are errors
                all_errors = all(isinstance(item, dict) and 'error' in item for item in result)
                if not all_errors or attempt == max_retries:
                    return result
            else:
                return result
                
            # If we got here, all items were errors and we have retries left
            if attempt < max_retries:
                # Exponential backoff: 2s, 4s, 8s, etc.
                wait_time = 2 ** (attempt + 1)
                time.sleep(wait_time)
                
        except Exception as e:
            if attempt == max_retries:
                return [{"error": f"Failed after {max_retries + 1} attempts: {str(e)[:100]}..."}]
            # Wait before retry
            wait_time = 2 ** (attempt + 1)
            time.sleep(wait_time)
    
    return [{"error": "Max retries exceeded"}]

def scrape_flipkart_prices(query):
    """Scrape product prices from Flipkart with improved error handling and retry logic"""
    if not query:
        return [{"error": "Query parameter is required"}]
    
    # More realistic headers to avoid detection
    headers = {
        'User-Agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0'
    }
    
    try:
        search_url = f"https://www.flipkart.com/search?q={quote_plus(query)}"
        
        # Add a random delay to mimic human behavior
        time.sleep(random.uniform(1, 3))
        
        response = requests.get(search_url, headers=headers, timeout=25)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        # Try multiple container selectors (current and fallback patterns)
        container_patterns = [
            'div._13oc-S',  # Current common pattern
            'div._2kHMtA',  # Older pattern
            '[data-id]',    # Generic data attribute
            'div._1AtVbE',  # Another common pattern
            'div.col'       # Fallback
        ]
        
        product_containers = []
        for pattern in container_patterns:
            try:
                containers = soup.select(pattern)
                if len(containers) > 0:
                    product_containers = containers[:5]  # Limit to 5 products
                    break
            except:
                continue
        
        if not product_containers:
            return [{"error": "No products found on Flipkart. Website structure may have changed."}]
        
        # Try multiple selectors for product details
        for container in product_containers:
            try:
                # Try multiple name selectors
                name = None
                name_selectors = [
                    'a[title]',
                    'div._4rR01T',
                    'a.s1Q9rs',
                    'div._2WkVRV',
                    'a.IRpwTa'
                ]
                
                for selector in name_selectors:
                    try:
                        name_elem = container.select_one(selector)
                        if name_elem:
                            name = name_elem.get_text(strip=True)
                            if name:
                                break
                    except:
                        continue
                
                if not name:
                    continue
                
                # Try multiple price selectors
                price = None
                price_selectors = [
                    'div._30jeq3',
                    'div._25b18c',
                    'div._30jeq3._1_WHN1',
                    'div._1vC4OE'
                ]
                
                for selector in price_selectors:
                    try:
                        price_elem = container.select_one(selector)
                        if price_elem:
                            price_text = price_elem.get_text(strip=True)
                            if price_text:
                                price = price_text
                                break
                    except:
                        continue
                
                if not price:
                    continue
                
                # Try to get link
                link = "https://www.flipkart.com"
                try:
                    link_elem = container.find('a')
                    if link_elem and link_elem.get('href'):
                        link = urljoin("https://www.flipkart.com", link_elem['href'])
                except:
                    pass
                
                products.append({
                    "name": name[:100] + "..." if len(name) > 100 else name,
                    "price": price,
                    "link": link
                })
                
                if len(products) >= 3:
                    break
                    
            except Exception:
                # Skip this product if we can't extract data
                continue
        
        return products if products else [{"error": "No products found on Flipkart"}]
        
    except requests.Timeout:
        return [{"error": "Flipkart is taking too long to respond. Please try again later."}]
    except requests.ConnectionError:
        return [{"error": "Unable to connect to Flipkart. Check your internet connection."}]
    except requests.RequestException as e:
        return [{"error": f"Network error with Flipkart: {str(e)[:50]}..."}]
    except Exception as e:
        return [{"error": f"Error scraping Flipkart: {str(e)[:50]}..."}]

def scrape_amazon_prices(query):
    """Scrape product prices from Amazon with improved error handling and retry logic"""
    if not query:
        return [{"error": "Query parameter is required"}]
    
    # More realistic headers
    headers = {
        'User-Agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0'
    }
    
    try:
        search_url = f"https://www.amazon.in/s?k={quote_plus(query)}"
        
        # Add delay to mimic human behavior
        time.sleep(random.uniform(1, 3))
        
        response = requests.get(search_url, headers=headers, timeout=25)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        # Try multiple container selectors
        container_patterns = [
            'div[data-component-type="s-search-result"]',
            'div.s-result-item',
            'div.sg-col',
            'div.a-section'
        ]
        
        product_containers = []
        for pattern in container_patterns:
            try:
                containers = soup.select(pattern)
                if len(containers) > 0:
                    product_containers = containers[:5]
                    break
            except:
                continue
        
        if not product_containers:
            return [{"error": "No products found on Amazon. Website structure may have changed."}]
        
        # Try to extract product details
        for container in product_containers:
            try:
                # Try multiple name selectors
                name = None
                name_selectors = [
                    'h2 a span',
                    'span.a-size-base-plus',
                    'h2 span.a-text-normal',
                    'div.a-row a span'
                ]
                
                for selector in name_selectors:
                    try:
                        name_elem = container.select_one(selector)
                        if name_elem:
                            name_text = name_elem.get_text(strip=True)
                            if name_text and len(name_text) > 2:
                                name = name_text
                                break
                    except:
                        continue
                
                if not name:
                    continue
                
                # Try multiple price selectors
                price = None
                price_selectors = [
                    'span.a-price-whole',
                    'span.a-offscreen',
                    'span.a-price span.a-offscreen'
                ]
                
                for selector in price_selectors:
                    try:
                        price_elem = container.select_one(selector)
                        if price_elem:
                            price_text = price_elem.get_text(strip=True)
                            if price_text and ('₹' in price_text or price_text.replace(',', '').replace('.', '').isdigit()):
                                price = "₹" + price_text if not price_text.startswith("₹") else price_text
                                break
                    except:
                        continue
                
                if not price:
                    continue
                
                # Try to get link
                link = "https://www.amazon.in"
                try:
                    link_elem = container.select_one('h2 a, a.a-link-normal')
                    if link_elem and link_elem.get('href'):
                        link = urljoin("https://www.amazon.in", link_elem['href'])
                except:
                    pass
                
                products.append({
                    "name": name[:100] + "..." if len(name) > 100 else name,
                    "price": price,
                    "link": link
                })
                
                if len(products) >= 3:
                    break
                    
            except Exception:
                # Skip this product if we can't extract data
                continue
        
        return products if products else [{"error": "No products found on Amazon"}]
        
    except requests.Timeout:
        return [{"error": "Amazon is taking too long to respond. Please try again later."}]
    except requests.ConnectionError:
        return [{"error": "Unable to connect to Amazon. Check your internet connection."}]
    except requests.RequestException as e:
        return [{"error": f"Network error with Amazon: {str(e)[:50]}..."}]
    except Exception as e:
        return [{"error": f"Error scraping Amazon: {str(e)[:50]}..."}]

def scrape_reliance_prices(query):
    """Scrape product prices from Reliance Digital with improved error handling and retry logic"""
    if not query:
        return [{"error": "Query parameter is required"}]
    
    headers = {
        'User-Agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        ]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        search_url = f"https://www.reliancedigital.in/search?q={quote_plus(query)}:relevance"
        
        # Add delay
        time.sleep(random.uniform(1, 3))
        
        response = requests.get(search_url, headers=headers, timeout=25)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        # Try multiple container selectors
        container_patterns = [
            'li.product-item',
            'div.plp-product-details',
            'div.product-item',
            'div.col-md-3'
        ]
        
        product_containers = []
        for pattern in container_patterns:
            try:
                containers = soup.select(pattern)
                if len(containers) > 0:
                    product_containers = containers[:5]
                    break
            except:
                continue
        
        if not product_containers:
            return [{"error": "No products found on Reliance Digital. Website structure may have changed."}]
        
        # Extract product details
        for container in product_containers:
            try:
                # Try to get name
                name_elem = None
                name_selectors = [
                    'p.sp__name',
                    'div.product-name',
                    'h3.product-title a'
                ]
                
                for selector in name_selectors:
                    try:
                        elem = container.select_one(selector)
                        if elem:
                            name_elem = elem
                            break
                    except:
                        continue
                
                if not name_elem:
                    continue
                    
                name = name_elem.get_text(strip=True)
                
                # Try to get price
                price_elem = None
                price_selectors = [
                    'span.sc__price--current',
                    'span.price',
                    'div.price'
                ]
                
                for selector in price_selectors:
                    try:
                        elem = container.select_one(selector)
                        if elem:
                            price_elem = elem
                            break
                    except:
                        continue
                
                if not price_elem:
                    continue
                    
                price = price_elem.get_text(strip=True)
                
                # Try to get link
                link = "https://www.reliancedigital.in"
                try:
                    link_elem = container.find('a')
                    if link_elem and link_elem.get('href'):
                        link = urljoin("https://www.reliancedigital.in", link_elem['href'])
                except:
                    pass
                
                products.append({
                    "name": name[:100] + "..." if len(name) > 100 else name,
                    "price": price,
                    "link": link
                })
                
                if len(products) >= 3:
                    break
                    
            except Exception:
                # Skip this product if we can't extract data
                continue
        
        return products if products else [{"error": "No products found on Reliance Digital"}]
        
    except requests.Timeout:
        return [{"error": "Reliance Digital is taking too long to respond. Please try again later."}]
    except requests.ConnectionError:
        return [{"error": "Unable to connect to Reliance Digital. Check your internet connection."}]
    except requests.RequestException as e:
        return [{"error": f"Network error with Reliance Digital: {str(e)[:50]}..."}]
    except Exception as e:
        return [{"error": f"Error scraping Reliance Digital: {str(e)[:50]}..."}]

def get_price_comparison(query):
    """Get price comparison from all websites with improved error handling and retry logic"""
    if not query:
        return {"error": "Query parameter is required"}
    
    # Get results from all scrapers with retry logic
    flipkart_results = scrape_with_retry(scrape_flipkart_prices, query)
    amazon_results = scrape_with_retry(scrape_amazon_prices, query)
    reliance_results = scrape_with_retry(scrape_reliance_prices, query)
    
    # Check if all scrapers failed with errors
    all_failed = True
    
    for results in [flipkart_results, amazon_results, reliance_results]:
        if isinstance(results, list) and len(results) > 0:
            # Check if all items are errors
            all_errors = all(isinstance(item, dict) and 'error' in item for item in results)
            if not all_errors:
                all_failed = False
                break
    
    if all_failed:
        return {
            "error": "Unable to fetch data from any e-commerce platform. This may be due to:\n" +
                     "1. Websites blocking our requests (anti-bot measures)\n" +
                     "2. Website structure changes\n" +
                     "3. Network connectivity issues\n" +
                     "4. Temporary server issues\n\n" +
                     "Try again later or search for a different product.\n\n" +
                     "SUGGESTED ACTIONS:\n" +
                     "- Wait 2-3 minutes before retrying\n" +
                     "- Try a more generic search term\n" +
                     "- Check your internet connection\n" +
                     "- Restart the application"
        }
    
    return {
        "Flipkart": flipkart_results,
        "Amazon": amazon_results,
        "Reliance Digital": reliance_results
    }
