#Code is designed to append 1 column in the beginning of each file and 4 rows that have the calculations of the 
#Mean, Std Dev, and Lower/Upper Bounds for each column to find outliers 
#Feb 22, 2025


import os 
import pandas as pd

#Define paths
base_dir = "/Users/ritneycoleman/Brain Imaging Data Revised/csv_converted_data"
output_dir = "/Users/ritneycoleman/Brain Imaging Data Revised/csv_converted_data_with_stats"

#Ensure output directory exists
os.makedirs(output_dir, exist_ok= True)

#Define the main folders and subfolders
folders = ["filt_global", "filt_noglobal", "nofilt_global", "nofilt_noglobal"]
subfolders = ["asd", "control",]


#Iterate through all folders and subfolders
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    output_folder_path = os.path.join(output_dir, folder)

    #Create output folder
    os.makedirs(output_folder_path, exist_ok = True)

    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        output_subfolder_path = os.path.join(output_folder_path, subfolder)

        #Ensure the output subfolder exists 
        os.makedirs(output_subfolder_path, exist_ok= True)

        #Process each CSV file
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                if file.endswith(".csv"):
                    file_path = os.path.join(subfolder_path, file)
                    output_file_path = os.path.join(output_subfolder_path, file)

                    try:
                        #Read full file to keep the first two rows
                        df_all = pd.read_csv(file_path, header=None)

                        #Read data starting from the third row (skip the first two rows)
                        df_data = pd.read_csv (file_path, header = None, skiprows=2)

                        #Compute Statistics
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

                        #Save modified file in the new folder
                        df_final.to_csv(output_file_path, index = False, header = False)

                        print(f"Processed file: {output_file_path}")
                    
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")


