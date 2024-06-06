# D:\Github\DjangoCoinScraper\coin_scraper\api\tasks.py
from celery import shared_task
from .scraper import CoinMarketCapScraper

@shared_task
def scrape_coin_data(coin):
    scraper = CoinMarketCapScraper()
    return scraper.scrape_coin(coin)
