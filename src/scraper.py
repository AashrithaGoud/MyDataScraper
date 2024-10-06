from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from config import WEBSITE_URL
from src.models import Product
from src.utils import find_element

driver = wd.Chrome()
driver.get(WEBSITE_URL)

products = driver.find_elements(By.CSS_SELECTOR, '#product-list-wrap > div')
product_list = []

for item in products[1:]:
    name = item.find_element(By.XPATH, 'div/div[1]/a/div[2]/div[1]').text
    price = item.find_element(By.XPATH, 'div/div[1]/a/div[2]/div[2]/span[2]').text
    discount = find_element(item, By.XPATH, 'div/div[1]/a/div[2]/div[2]/span[3]')
    old_price = 0
    if discount is not None:
        discount = discount.text
        old_price = item.find_element(By.XPATH, 'div/div[1]/a/div[2]/div[2]/span[2]').text
    else:
        discount = 0

    p = Product(name, price, discount, old_price)
    product_list.append(p)

for product in product_list:
    print(product)

driver.close()
