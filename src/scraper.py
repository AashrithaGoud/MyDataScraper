import os
import shutil

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from datetime import datetime
from config import WEBSITE_URL
from src.models import Product
from src.storage import create_dataframe, send_data_api
from src.utils import find_element

driver = wd.Chrome()
driver.get(WEBSITE_URL)

products = driver.find_elements(By.CSS_SELECTOR, '#product-list-wrap > div')

product_list = []
for item in products:
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

driver.close()

df = create_dataframe(product_list)

date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name=f'products_data_{date}.json'
file = f'../data/raw/{file_name}'
df.to_json(file, orient='records', indent=4)

send_data_api(product_list)
# flask_api_project=r"C:\Users\aashr\PycharmProjects\FlaskAPIProject\Data\\"+file_name
# shutil.copy(file,flask_api_project)
