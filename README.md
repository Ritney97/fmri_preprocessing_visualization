# fMRI Preprocessing & Visualization

This page includes code and data for preprocessing and visualizing brain activity in an ASD subject using Python. The goal is to standardize the voxel intensities from fMRI data and visualize the result using a glass brain image.

---

## Overview

This project includes the following steps:
1. **Convert** `.1D` data to `.csv`
2. **Append** summary statistics (mean, std dev, lower & upper bounds)
3. **Standardize** voxel intensities
4. **Visualize** brain activity (glass brain image)

---

## Project Structure

- `data/` – Raw input files (`.1D`, `.nii.gz`)
- `docs/` – Scripts used for each step of preprocessing and visualization
- `results/` – Generated `.csv` files and final brain visualization

---

## Dependencies

Install dependencies with:

```bash
pip install -r requirements.txt