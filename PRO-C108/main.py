import pandas as pd
import plotly.figure_factory as ff
import scipy

df = pd.read_csv("/Users/new/Documents/PythonBYJUProjects/PRO-C108/bell_curve.csv")

Fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Mobile Brand"], show_hist = True)
Fig.show()