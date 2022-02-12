import csv
import pandas as pd
import plotly_express as px

data = pd.read_csv("/Users/new/Documents/PythonBYJUProjects/PRO-C107/student_data.csv")
print(data.groupby(["level", "student_id"])["attempt"].mean())

plot_data = px.scatter(data, x = "student_id", y = "level", color = "attempt", size = "attempt")

plot_data.show()