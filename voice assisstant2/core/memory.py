# core/memory.py
import json
import os

FILE = "memory.json"

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {
        "contacts": {
            "hyma": "coresponding number",
        },
        "favorite_contact": "mom",
        "frequent_sites": []
    }

def save_memory():
    with open(FILE, "w") as f:
        json.dump(memory, f, indent=4)
