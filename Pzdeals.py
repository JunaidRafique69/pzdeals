from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time


driver = webdriver.Chrome()

url = 'https://www.pzdeals.com'
driver.get(url)
# For single product
product_link = driver.find_element(By.XPATH,"//li[@class=' on-sale text-center']")
product_link.click()
product_links = driver.find_element(By.XPATH,"//div[@class='is_desktop']//a")
product_urls = []

url = product_links.get_attribute('href')
print(url)
driver.back()

# Loop
# xpath = ("//li[@class=' on-sale text-center']")
# products = driver.find_element(By.XPATH,xpath)
# for product in products:
#     WebDriverWait(driver,10).until(EC.element_to_beclickable((B)))
#     product.click()
#     product_link = driver.find_element(By.XPATH, "//div[@class='is_desktop']//a")
#     product_urls = []
#     url = product_link.get_attribute('href')
#     print(url)
#     product_urls.append(url)
#     time.sleep(1)
#     driver.back()

# # Products ke XPath input lena
# products_xpath = ("//li[@class=' on-sale text-center']")
#
# # Product page ka XPath input lena
# product_page_xpath = ("//div[@class='is_desktop']//a")
