from celery import shared_task
import logging
from .scraper import CoinMarketCapScraper

logger = logging.getLogger(__name__)

@shared_task
def scrape_coin_data(coins):
    results = []
    for coin in coins:
        scraper = CoinMarketCapScraper(coin)
        coin_data = scraper.scrape()
        results.append({
            'coin': coin,
            'output': coin_data
        })
    return results
