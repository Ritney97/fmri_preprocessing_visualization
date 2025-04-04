import os
import pandas as pd

# Define the specific input file and output CSV path
input_file = "Caltech_0051456_rois_aal.1D"  # File included in the repository
output_file = "Caltech_0051456_rois_aal.csv"  # Desired CSV output name

try:
    # Load the .1D file using whitespace as the delimiter
    df = pd.read_csv(input_file, delim_whitespace=True, header=None)

    # Rename the columns to start at 1 instead of default numbers
    df.columns = range(1, len(df.columns) + 1)

    # Save to CSV with headers, without index
    df.to_csv(output_file, index=False, header=True)

    print(f"Successfully converted {input_file} to {output_file}")

except Exception as e:
    print(f"Error converting {input_file}: {e}")