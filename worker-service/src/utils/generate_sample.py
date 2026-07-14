import csv
import gzip
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INPUT_DIR = os.path.join(BASE_DIR, "..", "sample-data", "input")
os.makedirs(INPUT_DIR, exist_ok=True)

csv_path = os.path.join(INPUT_DIR, "sample.csv")
gz_path = os.path.join(INPUT_DIR, "sample.csv.gz")

rows = [
    ["timestamp", "voltage", "current", "power"],
    ["2026-07-14 10:00:00", "230", "5.2", "1196"],
    ["2026-07-14 10:01:00", "229", "5.1", "1168"],
    ["2026-07-14 10:02:00", "231", "5.3", "1224"],
]

with open(csv_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)

with open(csv_path, "rb") as f_in:
    with gzip.open(gz_path, "wb") as f_out:
        f_out.writelines(f_in)

print("✅ Created:", csv_path)
print("✅ Created:", gz_path)