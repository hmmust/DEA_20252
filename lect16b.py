import pandas as pd
import numpy as np
import math
products_df= pd.read_csv("products2.csv")
products_df['is_id_duplicated'] = products_df.duplicated(subset=['product_id'],keep="first")
print(products_df)
products_df.drop_duplicates(subset=['product_id'],keep="first",inplace=True)
print(products_df)

products_df['is_name_cat_duplicated'] = products_df.duplicated(
    subset=['product_category_id','product_name'],keep="first")
print(products_df)
