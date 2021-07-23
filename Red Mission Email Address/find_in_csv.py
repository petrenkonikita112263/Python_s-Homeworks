import pandas as pd

df = pd.read_csv("download_link.csv", header=None)
# print(df)
# print(df[2])
print("".join(df[2]))
