from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCapScraper:
    def __init__(self, coin):
        self.coin = coin
        self.base_url = f"https://coinmarketcap.com/currencies/{self.coin.lower()}/"
        self.data = {}

    def scrape(self):
        print(f"Scraping data for {self.coin}...")
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        try:
            driver.get(self.base_url)
            self.data['price'] = self.get_text(driver, By.XPATH, "//span[@class='sc-d1ede7e3-0 fsQm base-text']")
            self.data['price_change'] = self.get_text(driver, By.XPATH, "//*[@id=\"section-coin-overview\"]/div[2]/div/div/p")
            self.data['market_cap'] = self.get_text(driver, By.XPATH, "//*[@id=\"__next\"]/div[2]/div/div[1]/div/div[2]/section/div/section/div/div/div[2]/div/div[3]/div")
            self.data['volume'] = self.get_text(driver, By.XPATH, "//*[@id=\"__next\"]/div[2]/div/div[1]/div/div[2]/section/div/section/div/div/div[2]/div/div[4]/div")
            self.data['circulating_supply'] = self.get_text(driver, By.XPATH, "//*[@id=\"section-coin-stats\"]/div/dl/div[4]/div[1]/dd")
            self.data['contracts'] = self.get_contracts(driver)
            self.data['official_links'] = self.get_official_links(driver)
            self.data['socials'] = self.get_social_links(driver)
        except Exception as e:
            print(f"Error scraping data for {self.coin}: {e}")
        finally:
            driver.quit()
        print(f"Data scraping completed for {self.coin}.")
        return self.data

    def get_text(self, driver, by, value):
        try:
            element = driver.find_element(by, value)
            return element.text
        except Exception as e:
            print(f"Error getting text for {value}: {e}")
            return None

    def get_contracts(self, driver):
        contracts = []
        try:
            contract_elements = driver.find_elements(By.XPATH, "//div[@class='contractRow']")
            for element in contract_elements:
                contract_name = element.find_element(By.XPATH, "//div[@class='contractRowName']").text
                contract_address = element.find_element(By.XPATH, "//div[@class='contractRowValue']").text
                contracts.append({"name": contract_name, "address": contract_address})
        except Exception as e:
            print(f"Error getting contracts: {e}")
        return contracts

    def get_official_links(self, driver):
        links = []
        try:
            official_link_elements = driver.find_elements(By.XPATH, "//div[@class='officialLinks']//a")
            for element in official_link_elements:
                link_name = element.text
                link_url = element.get_attribute('href')
                links.append({"name": link_name, "link": link_url})
        except Exception as e:
            print(f"Error getting official links: {e}")
        return links

    def get_social_links(self, driver):
        socials = []
        try:
            social_link_elements = driver.find_elements(By.XPATH, "//div[@class='socialLinks']//a")
            for element in social_link_elements:
                social_name = element.text
                social_url = element.get_attribute('href')
                socials.append({"name": social_name, "url": social_url})
        except Exception as e:
            print(f"Error getting social links: {e}")
        return socials


# Example usage:
scraper = CoinMarketCapScraper("bitcoin")
data = scraper.scrape()
print(data)