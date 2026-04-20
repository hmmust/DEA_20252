import requests
import pandas as pd
customers_url= "https://raw.githubusercontent.com/hmmust/DEA_50251/refs/heads/master/customers_filtered.json"

resp= requests.get(customers_url)
print(resp.status_code)
if resp: #resp.status_code==200:
    customers=resp.json()
    customers_df = pd.DataFrame(customers)
    print(customers_df)
    