import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",              # use the same user that worked in Step 3
    password="Victor1234.", # the same password that worked in Step 3
    database="cellulase_db"
)

# 1. Read the whole table
df = pd.read_sql("SELECT * FROM enzyme_activity", conn)
print("First 5 rows from MySQL:")
print(df.head().to_string(index=False))
print("Total rows:", len(df))

# 2. Filtering example: only sugarcane bagasse
bagasse = pd.read_sql("SELECT * FROM enzyme_activity WHERE substrate = 'Sugarcane bagasse'", conn)
print("\nSugarcane bagasse rows:", len(bagasse))

# 3. Aggregation example: mean activity per substrate, computed by SQL
query = """
SELECT substrate,
       ROUND(AVG(fpase_IU_ml), 3) AS mean_fpase,
       ROUND(AVG(endoglucanase_IU_ml), 3) AS mean_endoglucanase,
       ROUND(AVG(exoglucanase_IU_ml), 3) AS mean_exoglucanase
FROM enzyme_activity
GROUP BY substrate
"""
summary = pd.read_sql(query, conn)
print("\nMean activity by substrate (computed by MySQL):")
print(summary.to_string(index=False))

conn.close()
