import json
import csv

metadata_file  = "data/raw/metadata.json"
output_valid   = "data/processed/observations_valid.csv"

# WCZYTANIE DANYCH
with open(metadata_file) as file:
    metadata = json.load(file)

with open(output_valid) as file:
    reader = csv.DictReader(file)
    valid_records = list(reader)

# FINALNY DATASET POD TRENING MODELU
model_input = [
    {key: record[key] for key in metadata['feature_columns']} 
    for record in valid_records
]

if model_input: # sprawdzam czy są jakiekolwiek dane
    feature_columns_check = list(model_input[0].keys()) == metadata['feature_columns']

    if(feature_columns_check):
        output_model_input = "data/processed/model_input.csv"
        with open(output_model_input, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=model_input[0].keys())
            writer.writeheader()
            writer.writerows(model_input)
        
        print("Successfuly exported:")
        print("\tdata/processed/model_input.csv")


