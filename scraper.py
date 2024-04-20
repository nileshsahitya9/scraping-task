import requests
from bs4 import BeautifulSoup

class Scraper:
  def __init__(self, proxy=None):
    self.proxy = proxy

  def scrape(self, page_url):
    try:
      response = requests.get(page_url, proxies=self.proxy)
      if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('li', class_='product')
        scraped_data = []
        for product in products:
          product_name = product.find('h2', class_='woo-loop-product__title').text.strip()
          product_price = float(soup.find('span', class_='woocommerce-Price-amount amount').text.strip().replace('₹', '').replace(',', ''))
          image_url = soup.find('img', class_='attachment-woocommerce_thumbnail')['src']
          scraped_data.append({'product_title': product_name, 'product_price': product_price, 'image_url': image_url})
        return scraped_data   
      else:
        print(f"Failed to scrape {page_url}. Status code: {response.status_code}")
        return None
    except Exception as e:
      print(f"Exception occurred while scraping {page_url}: {str(e)}")
      return None