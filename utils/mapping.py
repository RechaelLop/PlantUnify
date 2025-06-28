import json
import os

MAPPING_DIR = "data/mappings"

def load_mapping(plant_name):
    path = os.path.join(MAPPING_DIR, f"{plant_name}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def save_mapping(plant_name, mapping_dict):
    os.makedirs(MAPPING_DIR, exist_ok=True)
    path = os.path.join(MAPPING_DIR, f"{plant_name}.json")
    with open(path, "w") as f:
        json.dump(mapping_dict, f, indent=4)

def apply_mapping(df, mapping_dict):
    return df.rename(columns=mapping_dict)
