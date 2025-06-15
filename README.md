# My Project

## Description
**main.py**
# 🖼️ Image Search Web App

**Discover images instantly** with this lightweight web application built with Python and Streamlit. The Image Search App allows you to find and browse images online using simple keyword searches.

## Key Features

- 🔍 **Intuitive keyword search** - Enter any term to find related images
- 🖼️ **Gallery-style display** - Images appear in a responsive grid with hover effects
- 📖 **Pagination support** - Navigate through large result sets easily
- ✅ **Error handling** - Clear warnings for empty searches or no results
- 🚀 **Realtime feedback** - Loading spinners and success messages

## How It Works

The application:
1. Takes user input for any search term
2. Crawls the web for relevant images
3. Displays results in a clean gallery format
4. Organizes images in paginated groups (10 per page)
5. Provides visual feedback throughout the process

## Tech Stack

- Python 
- Streamlit (web framework)
- Custom web crawler implementation
- Responsive CSS styling

Simply run `main.py` to start the local server and begin searching for images! No complex setup required.

**crawler.py**
### Bing Image Crawler  
**Overview**  
A lightweight Python web crawler that retrieves image URLs from Bing Images based on a search keyword. Using `urllib` and `BeautifulSoup`, it scrapes Bing's image results and extracts up to 50 direct image URLs for quick integration into projects or research.  

**Key Features**  
- 🔍 **Keyword-Based Search**: Input any keyword to fetch related image URLs.  
- ⚡ **Efficient Parsing**: Extracts direct image links from Bing’s HTML using regex and `BeautifulSoup`.  
- 🛡️ **Basic Anti-Blocking**: Includes a user-agent header and SSL context to minimize request failures.  
- 💡 **Error Handling**: Returns clear error messages for connectivity or parsing issues.  

**Usage**  
```python
from crawler import WebCrawler

crawler = WebCrawler()
results = crawler.search_images("mountains")  # Replace with your keyword

# Print fetched URLs  
for url in results:  
    print(url)  
```  

**Dependencies**  
- Python 3.x  
- `beautifulsoup4` (`pip install beautifulsoup4`)  
- `lxml` or built-in `html.parser`  

**Note**  
⚠️ For educational use only. Respect Bing’s terms of service and robots.txt policies.

**requirements.txt**
### Project Description  
**Web Scraping & Interactive Data App**  

This project leverages Streamlit to create a user-friendly web application for extracting, processing, and displaying web data. It combines:  
- **BeautifulSoup** for parsing HTML/XML content  
- **lxml** as a high-performance parser backend  
- **Streamlit** for building an interactive frontend interface  

Key features include:  
1. **Effortless Scraping**: Extract structured data from websites using CSS selectors/XPaths  
2. **Dynamic Previews**: Clean and visualize scraped content in real-time  
3. **Export Capabilities**: Download results as CSV/JSON  
4. **Responsive UI**: Intuitive controls for configuring scraping parameters  

Ideal for quick data extraction tasks, content monitoring, or educational demonstrations. Simply run the app, input a target URL, and retrieve organized data without manual coding.  

---

**Setup**:  
```bash
pip install streamlit beautifulsoup4 lxml
streamlit run app.py
```

## Features
- **main.py**: 0 functions, 0 classes
- **crawler.py**: 0 functions, 0 classes
- **requirements.txt**: 0 functions, 0 classes
