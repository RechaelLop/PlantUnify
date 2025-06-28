import os
from utils.ingest import load_plant_data
from utils.mapping import load_mapping, apply_mapping
from utils.clean import clean_dataframe

RAW_DIR = "data/raw"
MAPPING_DIR = "data/mappings"
OUTPUT_DIR = "data/standardized"

# Make sure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop through all plant files
for i in range(1, 8):
    plant_name = f"plant_{i}"
    file_path = os.path.join(RAW_DIR, f"{plant_name}.xlsx")

    print(f"\n📄 Processing: {plant_name}.xlsx")

    # Step 1: Load file
    df_raw = load_plant_data(file_path)
    if df_raw is None:
        print(f"❌ Failed to load {file_path}")
        continue
    print("   ✔ Loaded raw file")
    print(f"   Columns: {df_raw.columns.tolist()}")

    # Step 2: Load mapping
    mapping = load_mapping(plant_name)
    if not mapping:
        print(f"   ⚠️  Mapping not found for {plant_name}. Skipping...")
        continue
    df_mapped = apply_mapping(df_raw, mapping)
    print("   ✔ Applied column mapping")

    # Step 3: Clean
    df_clean = clean_dataframe(df_mapped, plant_name=plant_name)
    print("   ✔ Cleaned data")

    # Step 4: Save
    output_path = os.path.join(OUTPUT_DIR, f"{plant_name}_clean.csv")
    df_clean.to_csv(output_path, index=False)
    print(f"   ✅ Saved cleaned data to {output_path}")
