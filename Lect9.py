import pandas as pd

customers= pd.read_json("customers.json")
del customers['customer_street']
customers.to_json("customer_filtered.json",
                 orient="records")
print(customers.sample(2))

