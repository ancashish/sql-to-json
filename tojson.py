import mysql.connector
import pandas as pd
import json


# Set up MySQL connection
# Replace <username>, <password>, <host>, and <database> with your own MySQL server details
mysql_conn = mysql.connector.connect(
    user='username',
    password='password',
    host='host',
    database='db_name'
)

# Read data from MySQL into a pandas dataframe
sql_query = "SELECT * FROM <table name>"
df = pd.read_sql(sql_query, mysql_conn)

# Convert dataframe to JSON format
json_data = df.to_json(orient='records')

# Write JSON data to a file - file_name.json
with open('<file_name.json>', 'w') as f:
    json.dump(json.loads(json_data), f, indent=4)
