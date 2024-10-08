import pandas as pd


def create_dataframe(products):
    data = []
    for product in (products or []):
        data.append(product.to_dict())
    return pd.DataFrame(data)