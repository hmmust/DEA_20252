import pandas as pd
import numpy as np
import math
products_df= pd.read_csv("products.csv")
def calc_discount(product):
    net_price = product['product_price']
    if product['product_price'] <50:
        net_price = net_price*0.95
    elif product['product_price'] <100:
        net_price = net_price * 0.9
    elif product['product_price'] < 500:
        net_price = net_price * 0.85
    else:
        net_price = net_price * 0.8
    
    if product['product_category_id']==2:
        net_price = net_price * 0.9
    return net_price

products_df['product_price_discount'] = products_df.apply(calc_discount,axis=1)
print(products_df)
