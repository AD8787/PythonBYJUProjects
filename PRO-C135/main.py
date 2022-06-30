import csv
import pandas as pd
import matplotlib.pyplot as plt

rows = []

with open("filtered_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
headers[0] = "Index"

df = pd.read_csv("filtered_stars.csv")

star_name = df["Star Name"].tolist()
star_name.pop(0)

mass = df["Mass"].tolist()
mass.pop(0)

radius = df["Radius"].tolist()
radius.pop(0)

distance = df["Distance"].tolist()
distance.pop(0)

gravity = df["Gravity"].tolist()
gravity.pop(0)

plt.figure(figsize = (10, 5))
plt.title("Stars vs. Mass")
plt.xlabel("Name")
plt.ylabel("Mass")
plt.bar(star_name[0:9] , mass[0:9])

plt.figure(figsize = (10, 5))
plt.title("Stars vs. Radius")
plt.xlabel("Name")
plt.ylabel("Radius")
plt.bar(star_name[0:9] , radius[0:9])

plt.figure(figsize = (10, 5))
plt.title("Stars vs. Distance")
plt.xlabel("Name")
plt.ylabel("Distance")
plt.bar(star_name[0:9] , distance[0:9])

plt.figure(figsize = (10, 5))
plt.title("Stars vs. Gravity")
plt.xlabel("Name")
plt.ylabel("Gravity")
plt.bar(star_name[0:9] , gravity[0:9])

plt.show()



