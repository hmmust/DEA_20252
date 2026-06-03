import pandas as pd
import numpy as np
orders_df = pd.read_csv( 'orders.csv', sep=',',header=0, encoding='utf-8')
customers_df = pd.read_csv( 'customers.csv', sep=',',header=0, encoding='utf-8')

order_customers_df = pd.merge(orders_df,customers_df,
                              left_on='order_customer_id',
                              right_on='customer_id',
                              left_index=False,right_index=False)
print(order_customers_df)
print(order_customers_df.groupby('customer_city').agg(
    {
        'order_id':['count'],
    }
))