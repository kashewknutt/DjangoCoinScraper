# D:\Github\DjangoCoinScraper\coin_scraper\api\scraper.py
import requests
from bs4 import BeautifulSoup # type: ignore

class CoinMarketCapScraper:
    BASE_URL = 'https://coinmarketcap.com/currencies/'

    def scrape_coin(self, coin):
        url = f"{self.BASE_URL}{coin.lower()}/"
        response = requests.get(url)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        return self.parse_data(soup)

    def parse_data(self, soup):
        # Example extraction logic (modify as needed)
        price = soup.find('div', class_='priceValue').text.strip('$').replace(',', '')
        # Add more parsing logic as required
        return {
            'price': float(price),
            # Add more fields here
        }
