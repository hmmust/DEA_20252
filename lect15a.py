import pandas as pd
import numpy as np
import math
products_df= pd.read_csv("products.csv")
def calc_distcount(price):
    net_price = price
    if price <50:
        net_price = net_price*0.95
    elif price <100:
        net_price = net_price * 0.9
    elif price < 500:
        net_price = net_price * 0.85
    else:
        net_price = net_price * 0.8
    return net_price

products_df['product_price_discount'] = products_df['product_price'].map(calc_distcount)
products_df['product_price_discount'] = products_df['product_price_discount'].map(lambda p: round(p,2))
products_df['product_name'] = products_df['product_name'].map(str.lower)

print(products_df)
