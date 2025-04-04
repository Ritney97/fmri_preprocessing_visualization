# fMRI Preprocessing & Visualization

This project processes and visualizes fMRI brain imaging data. It includes:

- Downloading and loading raw fMRI data
- Converting 1D data to CSV
- Calculating key statistics (mean, std dev, bounds)
- Standardizing voxel intensities
- Visualizing brain activity with masks

All code is written in Python using `pandas`, `nilearn`, `nibabel`, and `numpy`.

## Folders

- **data/**: Raw and converted datasets
- **scripts/**: Python code for processing steps
- **results/**: Output images and stats