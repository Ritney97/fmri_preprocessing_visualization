import os
import pandas as pd

# Define the input directories as a dictionary
input_dirs = {
    "filt_global": "/Users/ritneycoleman/Brain Imaging Data/RawData/filt_global",
    "filt_noglobal":"/Users/ritneycoleman/Brain Imaging Data/RawData/filt_noglobal",
    "nofilt_global": "/Users/ritneycoleman/Brain Imaging Data/RawData/nofilt_global",
    "nofilt_noglobal": "/Users/ritneycoleman/Brain Imaging Data/RawData/nofilt_noglobal"
}

# Define the main output directory where CSVs will be stored
output_main_dir = "/Users/ritneycoleman/Brain Imaging Data/csv_converted_data"

# Ensure the main output directory exists
os.makedirs(output_main_dir, exist_ok=True)

# Function to convert .1D files to .csv while preserving folder structure
def convert_1D_to_csv(input_folder, output_folder):
    # Ensure output subfolder exists
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".1D"):  # Only process .1D files
            file_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".1D", ".csv"))

            try:
                # Load the .1D file, using whitespace as the delimiter
                df = pd.read_csv(file_path, delim_whitespace=True, header=None)

                # Rename columns starting from 1 instead of 2001, 2002, etc.
                df.columns = range(1, len(df.columns) + 1)

                # Save to CSV file without index but with headers
                df.to_csv(output_path, index=False, header=True)

                print(f"Converted {file} to {output_path}")

            except Exception as e:
                print(f"Error converting {file}: {e}")

# Process each folder separately
for folder_name, folder_path in input_dirs.items():
    output_subfolder = os.path.join(output_main_dir, folder_name)  # Create subfolder in output dir
    convert_1D_to_csv(folder_path, output_subfolder)

print("All .1D files have been converted and saved in respective folders.")