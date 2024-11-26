import pandas as pd

df = pd.read_excel("continent_mapping.xlsx")

null_counts = df.isnull().sum()

print(null_counts)
