import numpy as np
import pandas as pd

np.random.seed(42)  # same seed = same data every time

substrates = ["Sugarcane bagasse", "Rice husks", "Eucalyptus sawdust"]
days = [2, 4, 6, 8, 10, 12]
replicates = [1, 2, 3]

# each substrate has a different production level (bagasse best, has sawdust worst)
level = {"Sugarcane bagasse": 1.0, "Rice husks": 0.75, "Eucalyptus sawdust": 0.55}

rows = []
for sub in substrates:
    for day in days:
        for rep in replicates:
            # activity rises to a peak around day 6-8, then falls
            time_effect = np.exp(-((day - 7) ** 2) / 18)
            base = level[sub] * time_effect
            fpase = base * 0.9 + np.random.normal(0, 0.04)
            endo  = base * 1.6 + np.random.normal(0, 0.06)
            exo   = base * 0.5 + np.random.normal(0, 0.03)
            rows.append([sub, day, rep, round(fpase, 3), round(endo, 3), round(exo, 3)])

df = pd.DataFrame(rows, columns=["substrate", "incubation_day", "replicate",
                                 "fpase_IU_ml", "endoglucanase_IU_ml", "exoglucanase_IU_ml"])
df.insert(0, "sample_id", range(1, len(df) + 1))
df.to_csv("simulated_enzyme_data.csv", index=False)

print(df.head(10).to_string(index=False))
print("...")
print("Total rows:", len(df))
