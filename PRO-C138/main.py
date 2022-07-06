import pandas as pd
import numpy as np

df1 = pd.read_csv("PROC138_datasets/shared_articles.csv")
df2 = pd.read_csv("PROC138_datasets/users_interactions.csv")

print(df1.head())
print(df2.head())