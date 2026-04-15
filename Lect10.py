import pandas as pd

customers= pd.read_json("customers.json")
del customers['customer_street']
customers.to_parquet("customer_filtered.parquet",compression="snappy")
print(customers.sample(2))

