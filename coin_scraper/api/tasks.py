from celery import shared_task
from .scraper import CoinMarketCapScraper

@shared_task
def scrape_coin_data(coins):
    results = []
    total_coins = len(coins)
    
    print(f"Scraping data for {total_coins} coins...:")
    print(coins)
    
    for index, coin in enumerate(coins, start=1):
        print(f"Scraping data for coin {index}/{total_coins}: {coin}")
        
        scraper = CoinMarketCapScraper(coin)
        coin_data = scraper.scrape()
        
        results.append({
            'coin': coin,
            'output': coin_data
        })
        
        print(f"Data scraped successfully for coin {index}/{total_coins}: {coin}")
    
    print("Data scraping completed for all coins.")
    
    return results
