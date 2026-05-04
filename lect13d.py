import pandas as pd
import json

conn_uri = "postgresql://admin:admin@localhost:5433/fitdb"

schemas = json.load(open("artists_db/schemas.json"))

print(type(schemas))
artist_schema= schemas["artists"]
print(schemas["artists"][0]["column_name"])
artist_schema= sorted(artist_schema,key=lambda a: a['column_position'])
cols=[column["column_name"] for column in artist_schema]
print(cols)
