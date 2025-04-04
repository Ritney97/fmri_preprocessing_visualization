

import os 
import pandas as pd

#Define the base directory where the main folders are stored 
base_dir = "/Users/ritneycoleman/Brain Imaging Data Revised/csv_converted_data_with_stats"

#Define the main folders to iterate through
main_folders = ['filt_global', 'filt_noglobal', 'nofilt_global', 'nofilt_noglobal']

#Define the subfolders tp process (excludes "no_filename")
subfolders = ["asd", "control"]

#Define the output directory for storing standardized files
standardized_dir = "/Users/ritneycoleman/Brain Imaging Data Revised/standardized_files"
os.makedirs(standardized_dir, exist_ok=True) #Ensure the output directory exists

#Iterate over each main folder separately 
for main_folder in main_folders:
    main_folder_path = os.path.join(base_dir, main_folder)

    #Create a corresponding output folder for the standardized files
    standardized_main_folder = os.path.join(standardized_dir, main_folder)
    os.makedirs(standardized_main_folder, exist_ok=True)

    #Iterate through only "asd" and "control" subfolders
    for subfolder in subfolders:
        subfolder_path = os.path.join(main_folder_path, subfolder)

        #Ensure the subfolder exists
        if os.path.isdir(subfolder_path):
            print(f"Processing subfolder: {subfolder}")

            #Create output subfolder 
            standardized_subfolder =os.path.join(standardized_main_folder, subfolder)
            os.makedirs(standardized_subfolder, exist_ok=True)

            #Iterate through CSV files in the subfolder
            for file in os.listdir(subfolder_path):
                if file.endswith(".csv"):
                    file_path = os.path.join(subfolder_path, file)
                    standardized_file_path = os.path.join(standardized_subfolder, file)

                    try:
                        print(f"Processing file: {file}") # Debug print

                        #Read the CSV file
                        df = pd.read_csv(file_path, header = None)

                        #Preserve first two rows and first column
                        first_two_rows = df.iloc[:2, :]
                        first_column = df.iloc[:, :1] #First column(stats)

                        #Extract data (exluding fist two rows and first column )
                        df_data = df.iloc[2:-4, 1:].astype(float) # Main numeric values

                        #Extract the statistical values (last four rows)
                        mean_values = df.iloc[-4, 1:].astype(float).values
                        std_dev_values = df.iloc[-3, 1:].astype(float).values

                        #Standardize the values (Z = (X - Mean) / Std Dev)
                        standardized_data = (df_data - mean_values) / std_dev_values

                        #Reconstruct the standardized Dataframe
                        standardized_df = pd.concat(
                            [first_two_rows,
                            pd.concat([first_column.iloc[2:-4], standardized_data],axis =1), df.iloc[-4:, :]],ignore_index=True)

                        #Save the standardized file
                        standardized_df.to_csv(standardized_file_path, index= False, header = False)
                        print(f"Standardized file saved: {standardized_file_path}")


                        # ----------------- UPDATE STATS AFTER STANDARDIZATION ----------------- #
                        # Re-read the standardized file for updating stats
                        df_standardized = pd.read_csv(standardized_file_path, header=None)

                        # Extract numeric values excluding the first column, first two rows, and last four rows
                        df_standardized_data = df_standardized.iloc[2:-4, 1:].astype(float)

                        # Recalculate statistics
                        new_mean_values = df_standardized_data.mean()
                        new_std_dev_values = df_standardized_data.std()
                        lower_bounds = new_mean_values - (5 * new_std_dev_values)
                        upper_bounds = new_mean_values + (5 * new_std_dev_values)

                        # Update the last four rows in the original DataFrame
                        df_standardized.iloc[-4, 1:] = new_mean_values.values
                        df_standardized.iloc[-3, 1:] = new_std_dev_values.values
                        df_standardized.iloc[-2, 1:] = lower_bounds.values
                        df_standardized.iloc[-1, 1:] = upper_bounds.values

                        # Save the updated file without modifying any other part
                        df_standardized.to_csv(standardized_file_path, index=False, header=False)
                        print(f"Updated statistics saved: {standardized_file_path}")
                    
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")