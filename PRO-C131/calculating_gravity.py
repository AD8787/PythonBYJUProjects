import csv
import pandas as pd

rows = []

with open("stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]

df = pd.read_csv("stars.csv")
solar_mass_list = df["solar_mass"].tolist()
solar_radius_list = df["solar_radius"].tolist()

solar_mass_list.pop(0)
solar_radius_list.pop(0)

solar_star_mass_si_unit = []

for data in solar_mass_list:
    si_unit = float(data)*1.989e+30
    solar_star_mass_si_unit.append(si_unit)

solar_star_radius_si_unit = []

for data in solar_radius_list:
    si_unit = float(data)*6.957e+8
    solar_star_radius_si_unit.append(si_unit)

print(solar_star_mass_si_unit)
print(solar_star_radius_si_unit)

star_masses = solar_star_mass_si_unit
star_radius = solar_star_radius_si_unit

star_names = df["star_names"].tolist()
star_names.pop(0)

star_gravity = []

for index,data in enumerate(star_names):
    gravity = (float(star_masses[index])*5.972e+24) / (float(star_radius[index])*float(star_radius[index])*6371000*6371000) * 6.674e-11
    star_gravity.append(gravity)

print(star_gravity)