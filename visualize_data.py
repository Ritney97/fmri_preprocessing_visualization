import nibabel as nib
import numpy as np
from nilearn import image, plotting
from nilearn.masking import compute_brain_mask

# Define file paths for ASD and control subjects
asd_file_path = "/Users/ritneycoleman/Brain Imaging Data Revised/Caltech_0051456_func_preproc.nii.gz"
control_file_path = "/Users/ritneycoleman/Brain Imaging Data Revised/Caltech_0051476_func_preproc.nii.gz"

# Load the fMRI data (4D)
asd_fmri_img = nib.load(asd_file_path)
control_fmri_img = nib.load(control_file_path)

# Reduce 4D to 3D (average across time)
asd_mean_img = image.mean_img(asd_fmri_img)
control_mean_img = image.mean_img(control_fmri_img)

# Apply a mask to keep only brain voxels and exclude noise
asd_brain_mask = compute_brain_mask(asd_mean_img)
asd_masked_img = image.math_img("img * mask", img=asd_mean_img, mask=asd_brain_mask)

control_brain_mask = compute_brain_mask(control_mean_img)
control_masked_img = image.math_img("img * mask", img=control_mean_img, mask=control_brain_mask)

# Plot the glass brain visualization for ASD subject
plotting.plot_glass_brain(asd_masked_img, threshold=3, display_mode='lyrz', colorbar=True, title="ASD Subject")

# Plot the glass brain visualization for Control subject
plotting.plot_glass_brain(control_masked_img, threshold=3, display_mode='lyrz', colorbar=True, title="Control Subject")

# Show the plots
plotting.show()