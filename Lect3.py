import pandas as pd

customers= pd.read_json("customers.json")
del customers['customer_street']
customers.to_json("customer_filtered.json",
                 index=False)
print(customers.head(2))
print(customers.tail(2))
print(customers.sample(2))

