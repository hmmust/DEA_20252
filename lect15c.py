import pandas as pd
import numpy as np
import math
products_df= pd.read_csv("products2.csv")
print(products_df.info())
print(products_df.isnull().sum())

