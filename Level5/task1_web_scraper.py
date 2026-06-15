# task1_web_scraper.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url: str):
    """Basic web scraper using BeautifulSoup."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Python Internship Project - Sysslan IT Solutions)'
    }
    
    try:
        print(f"🌐 Scraping website: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("\n" + "="*70)
        title = soup.title.string.strip() if soup.title and soup.title.string else "No Title Found"
        print(f"📑 Page Title: {title}")
        print("="*70)
        
        print("\n🔍 Main Headings:")
        for i, heading in enumerate(soup.find_all(['h1', 'h2'])[:8], 1):
            text = heading.get_text().strip()
            if text:
                print(f"{i:2d}. {heading.name.upper()}: {text[:100]}")
        
        print("\n🔗 Important Links:")
        count = 0
        for link in soup.find_all('a', href=True):
            if count >= 10:
                break
            text = link.get_text().strip()
            if text and len(text) > 2:
                full_url = urljoin(url, str(link['href']))
                print(f"   • {text[:60]} → {full_url}")
                count += 1
        
        print(f"\n✅ Scraping completed successfully! ({count} links found)")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection Error: {e}")
        print("💡 Tip: Check your internet or try https://example.com")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    print("🕸️  Web Scraper using BeautifulSoup")
    print("=" * 60)
    
    url_input = input("Enter website URL (default: https://example.com): ").strip()
    
    # Safe URL handling
    if not url_input:
        url: str = "https://example.com"
    elif not url_input.startswith(("http://", "https://")):
        url: str = "https://" + url_input
    else:
        url: str = url_input
    
    scrape_website(url)