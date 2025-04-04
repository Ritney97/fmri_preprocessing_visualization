# This is the code used to standardize the values of the file. 
# It converts the 1d file to a csv file.
# Author @Ritney Coleman
# Date: April 4, 2025

import pandas as pd

# === File paths ===
input_path = "Caltech_0051456_rois_aal_with_stats.csv"
output_path = "Caltech_0051456_rois_aal_standardized.csv"

try:
    # === Load CSV file without headers ===
    df = pd.read_csv(input_path, header=None)

    # === Preserve first two rows and first column ===
    first_two_rows = df.iloc[:2, :]
    first_column = df.iloc[:, :1]  # Column with stat labels

    # === Extract data for standardization (excluding first two rows, first column, last four rows) ===
    df_data = df.iloc[2:-4, 1:].astype(float)

    # === Extract original stats for later comparison ===
    mean_values = df.iloc[-4, 1:].astype(float)
    std_dev_values = df.iloc[-3, 1:].astype(float)

    # === Standardize (Z = (X - Mean) / Std Dev) ===
    standardized_data = (df_data - mean_values) / std_dev_values

    # === Reconstruct standardized DataFrame ===
    standardized_df = pd.concat([
        first_two_rows,
        pd.concat([first_column.iloc[2:-4].reset_index(drop=True), standardized_data.reset_index(drop=True)], axis=1),
        df.iloc[-4:, :]  # Original stat rows (will be updated next)
    ], ignore_index=True)

    # === Recalculate stats ===
    new_mean = standardized_data.mean()
    new_std = standardized_data.std()
    new_lower = new_mean - 5 * new_std
    new_upper = new_mean + 5 * new_std

    # === Update last four rows (stat labels remain on first column) ===
    standardized_df.iloc[-4, 1:] = new_mean.values
    standardized_df.iloc[-3, 1:] = new_std.values
    standardized_df.iloc[-2, 1:] = new_lower.values
    standardized_df.iloc[-1, 1:] = new_upper.values

    # === Save standardized file ===
    standardized_df.to_csv(output_path, index=False, header=False)
    print(f"Standardized file saved: {output_path}")

except Exception as e:
    print(f"Error processing the file: {e}")