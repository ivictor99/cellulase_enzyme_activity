import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Victor1234.",
    database="cellulase_db",
)

df = pd.read_sql("SELECT * FROM enzyme_activity ORDER BY substrate, incubation_day, replicate", conn)
conn.close()

df.to_csv("final_enzyme_data.csv", index=False)
print("Saved: final_enzyme_data.csv")
print("Rows:", len(df))
print(df.head(3).to_string(index=False))
