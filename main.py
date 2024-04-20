import argparse
from scraper import Scraper
from database import DatabaseManager
from notification import NotificationHandler
from settings import SettingsHandler
from authentication import Authentication
from retry import retry
from cache import Cache

class ScraperApp:
  def __init__(self, scraper, db_manager, notification_handler, settings_handler, authentication, cache):
    self.scraper = scraper
    self.db_manager = db_manager
    self.notification_handler = notification_handler
    self.settings_handler = settings_handler
    self.authentication = authentication
    self.cache = cache

  @retry
  def scrape_products(self):
    token = input("Enter authentication token: ")
    if not self.authentication.authenticate(token):
      print("Authentication failed. Exiting...")
      return
    products_data = []
    for page_num in range(1, self.settings_handler.page_limit + 1):
      page_url = f"https://dentalstall.com/shop/page/{page_num}/"
      products = self.scraper.scrape(page_url)
      products_data.extend(products)
    for product_data in products_data:
      if product_data:
        if not self.cache.check_cache(product_data['product_title'], product_data['product_price']):
          self.db_manager.save_data(product_data)
    self.notification_handler.notify(f"Scraping completed. Scraped {len(products_data)} products.")

def main():
  parser = argparse.ArgumentParser(description="Scraping Tool")
  parser.add_argument("--pages", type=int, default=5, help="Limit the number of pages to scrape")
  parser.add_argument("--proxy", type=str, help="Proxy string for scraping")
  args = parser.parse_args()

  scraper = Scraper(proxy={'http': args.proxy, 'https': args.proxy} if args.proxy else None)
  db_manager = DatabaseManager()
  notification_handler = NotificationHandler()
  settings_handler = SettingsHandler(page_limit=args.pages, proxy=args.proxy)
  authentication = Authentication()
  cache = Cache()

  app = ScraperApp(scraper, db_manager, notification_handler, settings_handler, authentication, cache)

  app.scrape_products()

if __name__ == "__main__":
  main()
