# This script appends summary statistics (Mean, Std Dev, Lower/Upper Bounds)
# to a single CSV file.
# Author @Ritney Coleman
# Date: April 4, 2025

import pandas as pd

# Define the file path
input_path = "Caltech_0051456_rois_aal.csv"
output_path = "Caltech_0051456_rois_aal_with_stats.csv"

try:
    # Read full data to preserve header rows
    df_all = pd.read_csv(input_path, header=None)

    # Read data from the 3rd row down for stats
    df_data = pd.read_csv(input_path, header=None, skiprows=2)

    # Compute stats
    mean_vals = df_data.mean()
    std_vals = df_data.std()
    lower_bounds = mean_vals - (5 * std_vals)
    upper_bounds = mean_vals + (5 * std_vals)

  #Create a summary row with an empty first column
    summary_row = pd.DataFrame([mean_vals, std_vals, lower_bounds, upper_bounds],
        index = ["Mean", "Std Dev", "Lower Bound", "Upper Bound"])
                        
    #Add a blank first column to the summary row 
    summary_row.insert(0, "", ["Mean", "Std Dev", "Lower Bound", "Upper Bound"])

    #Shift data to the right by adding a blank column at the start
    df_all.insert(0, "", "")

    #Append summary rows 
    df_final = pd.concat([df_all, summary_row], ignore_index=True)

    # Save it
    df_final.to_csv(output_path, index=False, header=False)
    print("Stats appended successfully.")

except Exception as e:
    print(f"Error processing the file: {e}")

