import csv
import json

battery_groups = {}


for i in range(0, 100, 10):
    battery_groups[f"{i}-{i+10}"] = []

with open("data/vehicles.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        battery = int(row["battery"])

        start = (battery // 10) * 10
        if battery == 100:
            start = 90

        key = f"{start}-{start+10}"
        battery_groups[key].append(row)

with open("data.json", "w") as f:
    json.dump(battery_groups, f, indent=4)
