import pandas as pd
import numpy as np
products_df= pd.read_csv("products.csv")
product_cat3_more100= products_df[ ((products_df['product_category_id'] == 3) & (products_df['product_price'] > 100)) ]
print(product_cat3_more100)
product_cat3_4_5_more100= products_df[ ((products_df['product_category_id'].isin([3,4,5])) & (products_df['product_price'] > 100)) ]
print(product_cat3_4_5_more100['product_price'].mean())


