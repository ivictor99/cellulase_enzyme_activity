import numpy as np
import pandas as pd

np.random.seed(42)

substrates = ["Sugarcane bagasse", "Rice husks", "Eucalyptus sawdust"]
days = [2, 4, 6, 8, 10, 12]
replicates = [1, 2, 3]

level = {
    "Sugarcane bagasse": 1.0,
    "Rice husks": 0.75,
    "Eucalyptus sawdust": 0.55,
}

rows = []
for substrate in substrates:
    for day in days:
        for replicate in replicates:
            time_effect = np.exp(-((day - 7) ** 2) / 18)
            base = level[substrate] * time_effect
            fpase = base * 0.9 + np.random.normal(0, 0.04)
            endoglucanase = base * 1.6 + np.random.normal(0, 0.06)
            exoglucanase = base * 0.5 + np.random.normal(0, 0.03)
            rows.append([
                substrate,
                day,
                replicate,
                round(fpase, 3),
                round(endoglucanase, 3),
                round(exoglucanase, 3),
            ])

df = pd.DataFrame(
    rows,
    columns=[
        "substrate",
        "incubation_day",
        "replicate",
        "fpase_IU_ml",
        "endoglucanase_IU_ml",
        "exoglucanase_IU_ml",
    ],
)
df.insert(0, "sample_id", range(1, len(df) + 1))
df.to_csv("simulated_enzyme_data.csv", index=False)

print(df.head(10).to_string(index=False))
print("...")
print("Total rows:", len(df))
