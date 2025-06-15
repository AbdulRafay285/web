# crawler.py
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import ssl
import re

class WebCrawler:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }
        self.ssl_context = ssl._create_unverified_context()

    def search_images(self, keyword):
        query = urlencode({'q': keyword})
        search_url = f"https://www.bing.com/images/search?{query}"
        req = Request(search_url, headers=self.headers)

        try:
            with urlopen(req, timeout=10, context=self.ssl_context) as response:
                html = response.read().decode("utf-8", errors="ignore")
        except Exception as e:
            return [f"Error fetching images: {e}"]

        soup = BeautifulSoup(html, "html.parser")
        images = []

        for img_tag in soup.find_all("a", {"class": "iusc"}, limit=50):
            m = re.search(r'"murl":"(.*?)"', img_tag.get("m", ""))
            if m:
                images.append(m.group(1))

        return images if images else ["No images found."]
