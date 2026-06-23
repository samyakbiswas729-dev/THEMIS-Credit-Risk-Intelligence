import pandas as pd

df = pd.read_csv("data/german_credit_data.csv")

for col in df.columns:
    print("\n")
    print(col)
    print(df[col].unique())