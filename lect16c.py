import pandas as pd
import numpy as np
df = pd.read_csv( 'orders.csv', sep=',',header=0, encoding='utf-8')
df['order_date']= pd.to_datetime(df['order_date'],errors='coerce')
print(df.groupby('order_status')['order_id'].count())
print(df.groupby('order_status').agg(
    ['count','max']
))
print(df.groupby('order_status').agg(
    {
        'order_id':[np.size],
        'order_date':['max']
    }
))