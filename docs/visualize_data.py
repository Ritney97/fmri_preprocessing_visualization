# This is the code used to create a visualization of the nii.gz file. 
# Author @Ritney Coleman
# Date: April 4, 2025

import nibabel as nib
import numpy as np
from nilearn import image, plotting
from nilearn.masking import compute_brain_mask

# Define file paths for ASD and control subjects
asd_file_path = "/Users/ritneycoleman/fmri_preprocessing_visualization/data/Caltech_0051456_func_preproc.nii.gz"

# Load the fMRI data (4D)
asd_fmri_img = nib.load(asd_file_path)

# Reduce 4D to 3D (average across time)
asd_mean_img = image.mean_img(asd_fmri_img)

# Apply a mask to keep only brain voxels and exclude noise
asd_brain_mask = compute_brain_mask(asd_mean_img)
asd_masked_img = image.math_img("img * mask", img=asd_mean_img, mask=asd_brain_mask)


# Plot the glass brain visualization for ASD subject
plotting.plot_glass_brain(asd_masked_img, threshold=3, display_mode='lyrz', colorbar=True, title="ASD Subject")

# Show the plots
plotting.show()