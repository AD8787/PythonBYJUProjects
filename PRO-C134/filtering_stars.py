import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("stars.csv")

rows = []
with open("stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]

star_data = rows[1:]

star = []
for distance in df.Distance:
    if distance == 100:
      star.append(True)
    else:
        star.append(False)

is_dist = pd.Series(star)

star_dist = df[is_dist]

star_dist.reset_index(inplace = True, drop = True)
print(star_dist.head())


gravity_star = []

for i in star_dist.Gravity:
    if i >= 150 and i <350:
        gravity_star.append(True)
    else:
        gravity_star.append(False)

gravity_star = pd.Series(gravity_star)

final_stars = star_dist[gravity_star]

df.to_csv("filtered_stars.csv")