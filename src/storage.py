import pandas as pd
import requests
from src.config import PRODUCT_API_BASEURL

def create_dataframe(products):
    data = []
    for product in (products or []):
        data.append(product.to_dict())
    return pd.DataFrame(data)

def send_data_api(products):
    products_json= []
    for product in products:
        products_json.append(product.to_dict())

    response = requests.post(PRODUCT_API_BASEURL+'/products', json=products_json)


