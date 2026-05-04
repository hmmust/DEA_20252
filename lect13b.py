import pandas as pd

conn_uri = "postgresql://admin:admin@localhost:5433/fitdb"

sanad_df = pd.read_csv("customer1.csv")
sanad_df.to_sql("customers",conn_uri,index=False, if_exists="append")