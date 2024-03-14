import csv
from scrapy.utils import response
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

driver = webdriver.Chrome()
url = 'https://www.pzdeals.com'
driver.get(url)


product_urls = []
# products = driver.find_elements(By.XPATH, "//li[@class=' on-sale text-center']")
# index = 0
# while index < len(products):
#     product = products[index]
#     product.click()
#     product_link = driver.find_element(By.XPATH, "//div[@class='is_desktop']//a")
#     url = product_link.get_attribute('href')
#     print(url)
#     product_urls.append(url)
#     time.sleep(1)
#     driver.back()
#     # Refresh products list after going back
#     products = driver.find_elements(By.XPATH, "//li[@class=' on-sale text-center']")
#     index += 1
#
#     with open('product_urls.csv','w',newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['Product URL'])
#         for url in product_urls:
#             writer.writerow([url])
#
# driver.quit()
# print('Product urls stored in "product_urls.csv"')

while True:
    products = driver.find_elements(By.XPATH, "//li[@class=' on-sale text-center']")
    for product in products:
        product.click()
        product_link = driver.find_element(By.XPATH, "//div[@class='is_desktop']//a")
        url = product_link.get_attribute('href')
        print(url)
        product_urls.append(url)
        time.sleep(1)
        driver.back()

    # Check if there's a next page
    next_page_button = driver.find_element(By.XPATH, "//a[@class='next page-numbers']")
    if 'disabled' in next_page_button.get_attribute('class'):
        break  # Exit the loop if there's no next page

    with open('product_urls.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Product URL'])
        for url in product_urls:
            writer.writerow([url])

driver.quit()
print('Product urls stored in "product_urls.csv"')

    # Click on the next page
    # next_page_button.click()
# def extract_links():
#     product_urls = []
#     products = driver.find_elements(By.XPATH, '//*[@id="pzdeals"]/main/div/div[3]/div[1]/div/ul[1]')
#     for product in products:
#         # WebDriverWait(driver,10).until(EC.element_to_beclickable((B)))
#         product.click()
#         product_link = driver.find_element(By.XPATH, "//div[@class='is_desktop']//a")
#         url = product_link.get_attribute('href')
#         print(url)
#         product_urls.append(url)
#         time.sleep(1)
#         driver.back()
#     return product_urls
#
#
# extract_links()

# # Products ke XPath input lena
# products_xpath = ("//li[@class=' on-sale text-center']")
#
# # Product page ka XPath input lena
# product_page_xpath = ("//div[@class='is_desktop']//a")
# For single product
# product_link = driver.find_element(By.XPATH,"//li[@class=' on-sale text-center']")
# product_link.click()
# product_links = driver.find_element(By.XPATH,"//div[@class='is_desktop']//a")
# product_urls = []
#
# url = product_links.get_attribute('href')
# print(url)
# driver.back()
#
# index = 0
# # while index <len(product_link):
#
# Loop