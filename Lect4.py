import pandas as pd

customers= pd.read_csv("customers.csv",sep=",",engine='pyarrow')
customers['customer_name']= customers['customer_fname'] + " " +customers['customer_lname']
del customers['customer_fname']
del customers['customer_lname']
customers.to_csv("customer_filtered.csv",
                 index=False,columns=['customer_id','customer_name'])
print(customers.head(2))
print(customers.tail(2))
print(customers.sample(2))

