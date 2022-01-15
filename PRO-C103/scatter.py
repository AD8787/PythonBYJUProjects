import pandas as pd
import plotly_express as pe

df = pd.read_csv("data.csv")

covid_data = pe.scatter(df, x = "date", y = "cases", color = "country")
covid_data.show()