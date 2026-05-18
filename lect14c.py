import pandas as pd
import numpy as np
products_df= pd.read_csv("products.csv")
products_df['product_price_category'] = np.where( products_df['product_price'] > 100,"E","C" )
conditions = [
    (products_df['product_price'] >= 1000),
    ((products_df['product_price'] >= 800) & (products_df['product_price'] < 1000)),
    ((products_df['product_price'] >= 500) & (products_df['product_price'] < 800)),
    (products_df['product_price'] < 0),
]
values = ["E","M","C","VC"]
products_df['product_price_category'] = np.select( conditions,values,default="NA")

print(products_df.sample(50))


