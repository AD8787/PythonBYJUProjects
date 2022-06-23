import pandas as pd
import csv

df = pd.read_csv('Data_merged.csv')
del df['Luminosity']
del df['Star_name']
del df['Distance']
del df['Mass']
del df['Radius']

df.to_csv('main.csv')