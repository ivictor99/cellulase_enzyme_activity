import pandas as pd
import mysql.connector

df = pd.read_csv("enzyme_data.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Victor1234.",
    database="cellulase_db",
)
cursor = conn.cursor()

sql = """INSERT INTO enzyme_activity
         (sample_id, substrate, incubation_day, replicate,
          fpase_IU_ml, endoglucanase_IU_ml, exoglucanase_IU_ml)
         VALUES (%s, %s, %s, %s, %s, %s, %s)"""

cursor.execute("DELETE FROM enzyme_activity")

for row in df.itertuples(index=False):
    record = (
        int(row.sample_id),
        row.substrate,
        int(row.incubation_day),
        int(row.replicate),
        float(row.fpase_IU_ml),
        float(row.endoglucanase_IU_ml),
        float(row.exoglucanase_IU_ml),
    )
    cursor.execute(sql, record)

conn.commit()

cursor.execute("SELECT COUNT(*) FROM enzyme_activity")
print("Rows in table:", cursor.fetchone()[0])

cursor.close()
conn.close()
