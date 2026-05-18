import pandas as pd
import numpy as np
products_df= pd.read_csv("products.csv")
products_df.sort_values(by=["product_category_id"],ascending=False,inplace=True)
products_df.sort_values(by=["product_category_id","product_price"],
                        ascending=False,inplace=True)
products_df.sort_values(by=["product_category_id","product_price"],
                        ascending=[False,True],inplace=True,kind="heapsort")
print(products_df.nlargest(10,["product_price"]))
print(products_df.nsmallest(10,["product_price"]))