import os
import csv
from acdh_handle_pyutils.client import HandleClient
from rdflib import Graph, URIRef, Namespace, Literal

ARCHE = Namespace("https://vocabs.acdh.oeaw.ac.at/schema#")
HANDLE_USERNAME = os.environ.get("HANDLE_USERNAME")
HANDLE_PASSWORD = os.environ.get("HANDLE_PASSWORD")
CSV_FILE = "update_ids.csv"

cl = HandleClient(HANDLE_USERNAME, HANDLE_PASSWORD)
reader = csv.DictReader(open("update_ids.csv"))

g = Graph()

print("updating pids")
for row in reader:
    cl.update_handle(row["handle_id"], row["arche_id"])
    g.add((
        URIRef(row["arche_id"]), ARCHE["hasPid"], Literal(f"{row['handle_id']}")
    ))
g.serialize("handles.ttl")

