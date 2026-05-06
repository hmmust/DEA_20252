import pandas as pd
import json
import glob
conn_uri = "postgresql://admin:admin@localhost:5433/fitdb"

schemas = json.load(open("artists_db/schemas.json"))
#FILES = ["artists_db/artists/artists-01.csv","artists_db/artists/artists-02.csv"]
FILES = glob.glob("artists_db/artists/*")
print(type(schemas))
artist_schema= schemas["artists"]
print(schemas["artists"][0]["column_name"])
artist_schema= sorted(artist_schema,key=lambda a: a['column_position'])
cols=[column["column_name"] for column in artist_schema]
for file in FILES:
    file1= pd.read_csv(file,names=cols)
    file1.to_sql("artists",conn_uri,index=False,if_exists="append")
    print("File ",file, " Loaded to Database.. ")
print(cols)
