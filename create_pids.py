import os
import csv
from acdh_handle_pyutils.client import HandleClient
from rdflib import Graph, URIRef, Namespace, Literal

ARCHE = Namespace("https://vocabs.acdh.oeaw.ac.at/schema#")
HANDLE_USERNAME = os.environ.get("HANDLE_USERNAME")
HANDLE_PASSWORD = os.environ.get("HANDLE_PASSWORD")
CSV_FILE = "create_ids.csv"

cl = HandleClient(HANDLE_USERNAME, HANDLE_PASSWORD)
data = []
with open(CSV_FILE) as f:
    reader = csv.DictReader(f,delimiter=',')
    for row in reader:
        print(row["arche_id"])
        data.append([row["arche_id"], cl.register_handle(row["arche_id"], full_url=True)])

with open(CSV_FILE, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["arche_id", "handle_id"])
    for row in data:
        writer.writerow(row)

print("creating ttl")
g = Graph()
for x in data:
    g.add((
        URIRef(x[0]), ARCHE["hasPid"], Literal(f'{x[1]}')
    ))
g.serialize("handles.ttl")
