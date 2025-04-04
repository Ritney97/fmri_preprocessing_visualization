Step-by-Step Instructions

1. Convert .1D Data to .csv

Script: convert1D_to_csv.py
Input File: Caltech_0051456_rois_aal.1D (in /data)
Output File: Caltech_0051456_rois_aal.csv (saved in /results)

Purpose: This script reads the .1D file and converts it into a readable .csv format with properly named column headers.

2. Append Statistical Summaries

Script: appendstats.py
Input File: Caltech_0051456_rois_aal.csv
Output File: Caltech_0051456_rois_aal_with_stats.csv (saved in /results)

Purpose: Adds summary statistics (mean, standard deviation, lower and upper bounds) as additional rows to the dataset.

3. Standardize the Data

Script: standardize.py
Input File: Caltech_0051456_rois_aal_with_stats.csv
Output File: Caltech_0051456_rois_aal_standardized.csv (saved in /results)

Purpose: Standardizes the voxel intensity data using Z-score normalization. Also updates the summary statistics to match the now standardized values. 

4. Visualize Brain Activity

Script: visualize_data.py
Input File: Caltech_0051456_func_preproc.nii.gz (in /data)
Output: A 3D glass brain plot showing activated regions (output.png in /results)

Purpose: Reduces 4D fMRI data to 3D, applies a brain mask, and visualizes the data as a glass brain image.

Final Notes
	•	All intermediate .csv outputs are stored in the results/ folder.
	•	Scripts are housed in the docs/ folder.
	•	Raw input files are located in the data/ folder.
	•	Final image output (output.png) is automatically saved after running the visualization script.