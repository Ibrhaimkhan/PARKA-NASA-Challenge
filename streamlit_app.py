import os
import pandas as pd
import streamlit as st

# Folder where your CSVs live
DATA_FOLDER = r'C:\Users\FireA\Documents\GitHub\SciSearch\Combined_data'

# Ensure the folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Path to the combined CSV
COMBINED_CSV_PATH = os.path.join(DATA_FOLDER, 'combined_df.csv')

# If combined_df.csv does not exist, create it
if not os.path.exists(COMBINED_CSV_PATH):
    csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.csv')]
    dfs = []

    if csv_files:
        for f in csv_files:
            file_path = os.path.join(DATA_FOLDER, f)
            try:
                df = pd.read_csv(file_path, on_bad_lines='skip')  # skip bad lines
                dfs.append(df)
                print(f"Loaded {f} with shape {df.shape}")
            except Exception as e:
                print(f"Error reading {f}: {e}")

        # Combine all CSVs safely
        if dfs:
            combined_df = pd.concat(dfs, ignore_index=True, sort=False)
        else:
            combined_df = pd.DataFrame({
                'Column1': ['A', 'B', 'C'],
                'Column2': [1, 2, 3]
            })
            print("No valid CSVs found. Created a dummy DataFrame.")
    else:
        # If no CSV files, create a dummy DataFrame
        combined_df = pd.DataFrame({
            'Column1': ['A', 'B', 'C'],
            'Column2': [1, 2, 3]
        })
        print("No CSVs found. Created a dummy DataFrame.")

    # Save the combined CSV
    combined_df.to_csv(COMBINED_CSV_PATH, index=False)
    print(f"Saved combined CSV at {COMBINED_CSV_PATH}")

# Now safely load the combined CSV
combined_df = pd.read_csv(COMBINED_CSV_PATH)
st.write("Data loaded successfully:", combined_df)
