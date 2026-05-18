import pandas as pd
import numpy as np
orders_df= pd.read_csv("orders.csv")
orders_df= orders_df.astype({"order_id": np.int16 , "order_customer_id": np.int16})
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'],errors="coerce")
print(orders_df.dtypes)

