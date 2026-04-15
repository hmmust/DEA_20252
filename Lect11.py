import pandas as pd

customers= pd.read_parquet("customer_filtered.parquet",
                           columns=["customer_id","customer_fullname"])
customers= pd.read_parquet("customer_filtered.parquet",
                           filters=[["customer_state","==","CA"]])
print(customers.sample(2))

