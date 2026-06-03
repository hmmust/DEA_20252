import pandas as pd
import numpy as np
import math
products_df= pd.read_csv("products2.csv")
print(products_df.info())

print(products_df.isnull().sum())

#products_df['product_price']= products_df['product_price'].fillna(10)
#products_df['product_price']= products_df['product_price'].fillna(products_df['product_price'].median())
#products_df['product_price']= products_df['product_price'].bfill()
products_df['product_price']= products_df['product_price'].ffill()

#products_df.dropna(axis=0,inplace=True)
#products_df.dropna(axis=1,inplace=True)

print(products_df.isnull().sum())
print(products_df['product_price'].value_counts())