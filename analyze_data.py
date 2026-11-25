import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("enzyme_data.csv")

print("Missing values per column:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

cols = ["fpase_IU_ml", "endoglucanase_IU_ml", "exoglucanase_IU_ml"]

print("\nMean activity by substrate (IU/ml):")
print(df.groupby("substrate")[cols].mean().round(3))

print("\nMean activity by incubation day (IU/ml):")
print(df.groupby("incubation_day")[cols].mean().round(3))

print("\nStandard deviation by substrate (IU/ml):")
print(df.groupby("substrate")[cols].std().round(3))

df.groupby("substrate")[cols].mean().plot(kind="bar")
plt.title("Mean Cellulase Activity by Substrate")
plt.ylabel("Activity (IU/ml)")
plt.xlabel("Substrate")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("graph1_activity_by_substrate.png")
plt.show()

for substrate in df["substrate"].unique():
    substrate_data = df[df["substrate"] == substrate]
    daily_mean = substrate_data.groupby("incubation_day")["fpase_IU_ml"].mean()
    plt.plot(daily_mean.index, daily_mean.values, marker="o", label=substrate)

plt.title("FPase Activity over Incubation Time")
plt.xlabel("Incubation day")
plt.ylabel("FPase activity (IU/ml)")
plt.legend()
plt.tight_layout()
plt.savefig("graph2_fpase_over_time.png")
plt.show()

print("\nGraphs saved: graph1_activity_by_substrate.png, graph2_fpase_over_time.png")
