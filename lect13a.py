import pandas as pd

conn_uri = "postgresql://admin:admin@localhost:5433/fitdb"

customers = pd.read_sql("customers",conn_uri)
print(customers)

data1 = pd.read_sql_query(
    "select order_status,count(*) from orders group by order_status order by 2",
    conn_uri)
data1.to_csv("orders_counts.csv",index=False)
print(data1)