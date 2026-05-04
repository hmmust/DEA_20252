import pandas as pd

conn_uri = "postgresql://admin:admin@localhost:5433/fitdb"
cols= ["customer_id","customer_fname","customer_lname","customer_email","customer_password","customer_street","customer_city","customer_state","customer_zipcode"]
raghad_df = pd.read_csv("customer2.csv",header=None)#,names=cols)
raghad_df.columns=cols
print(raghad_df)

raghad_df.to_sql("customers",conn_uri,index=False, if_exists="append")