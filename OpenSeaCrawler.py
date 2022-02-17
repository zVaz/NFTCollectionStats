from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import time

TIMEOUT_WAIT_ELEMENT = 15

BUY_NOW_CLASS_SELECTOR               = ".btgkrL.FeaturedFilter--item"
CURRENCY_SELECT_CLASS_SELECTOR       = ".cJLIjY"
CURRENCY_SELECT_ETH_CLASS_SELECTOR   = ".QbTKh .glymPt"
CURRENCY_SELECT_MAX_CLASS_SELECTOR   = ".fXxmev.Input--framed .Input--main input[placeholder='Max']"
CURRENCY_SELECT_APPLY_CLASS_SELECTOR = ".dpXlkZ"
NUM_OF_ITEMS_CLASS_SELECTOR          = ".kejuyj"

class OpenSeaCrawler():
   def __init__(self, opensea_collection_id: str):
      self.opensea_collection_id = opensea_collection_id

   def __enter__(self, chrome_driver_path: str = './chromedriver'):
      self.driver = webdriver.Chrome(chrome_driver_path)
      self.driver.minimize_window()
      self.driver.get(f"https://opensea.io/collection/{self.opensea_collection_id}")
      return self

   def __exit__(self, type, value, traceback):
      self.driver.close()

   def set_filter_buy_now(self) -> None:
      buy_now_element = WebDriverWait(self.driver, TIMEOUT_WAIT_ELEMENT).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, BUY_NOW_CLASS_SELECTOR))
      )
      buy_now_element.click()
   
   def set_filter_eth_max_price(self, max_price: float) -> None:
      currency_price_filter_select_element = WebDriverWait(self.driver, TIMEOUT_WAIT_ELEMENT).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, CURRENCY_SELECT_CLASS_SELECTOR))
      )
      currency_price_filter_select_element.click()

      currency_price_filter_select_eth_elements = WebDriverWait(self.driver, TIMEOUT_WAIT_ELEMENT).until(
         EC.presence_of_all_elements_located((By.CSS_SELECTOR, CURRENCY_SELECT_ETH_CLASS_SELECTOR))
      )
      currency_price_filter_select_eth_elements[1].click()

      max_price_filter_element = WebDriverWait(self.driver, TIMEOUT_WAIT_ELEMENT).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, CURRENCY_SELECT_MAX_CLASS_SELECTOR))
      )
      max_price_filter_element.clear()
      max_price_filter_element.send_keys(f"{max_price - 0.0001:.4f}")

      apply_price_filter_element = WebDriverWait(self.driver, TIMEOUT_WAIT_ELEMENT).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, CURRENCY_SELECT_APPLY_CLASS_SELECTOR))
      )
      apply_price_filter_element.click()

   def get_num_of_items_str(self) -> str:
      WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, NUM_OF_ITEMS_CLASS_SELECTOR), 'Loading items...'))
      items_count_element_element = WebDriverWait(self.driver, TIMEOUT_WAIT_ELEMENT).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, NUM_OF_ITEMS_CLASS_SELECTOR))
      )
      return items_count_element_element.text

   def get_opensea_stats(self) -> dict:
      r = requests.get(f"https://api.opensea.io/api/v1/collection/{self.opensea_collection_id}/stats")
      return r.json()['stats']