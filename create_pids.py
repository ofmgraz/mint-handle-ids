import os
import csv
from acdh_handle_pyutils.client import HandleClient


HANDLE_USERNAME = os.environ.get("HANDLE_USERNAME")
HANDLE_PASSWORD = os.environ.get("HANDLE_PASSWORD")
CSV_FILE = "create_ids.csv"

cl = HandleClient(HANDLE_USERNAME, HANDLE_PASSWORD)
reader = csv.DictReader(open("create_ids.csv"))

data = []
for row in reader:
    data.append([row["arche_id"], cl.register_handle(row["arche_id"], full_url=True)])

with open(CSV_FILE, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["arche_id", "handle_id"])
    for row in data:
        writer.writerow(row)
