# CMSE 492 Homework 01 – Professionalizing a Small Data Science Project

## Overview

This project demonstrates how to organize a small data science analysis into a reproducible project structure.  
The analysis reads sales data and customer lookup information, generates a regional summary table, and produces a revenue visualization.

The goal of the assignment is to structure the project so that another user can easily reproduce the results.

---

## Project Structure

```bash
cmse492-hw01-starter
│   HW01-STUDENT.ipynb
│   README.md
│
├───data
│   └───raw
│           customer_lookup.csv
│           sales_jan.csv
│
├───notebooks
│       output_examples.ipynb
│       quick_run_demo.ipynb
│
├───outputs
│       .gitkeep
│       revenue_by_region.png
│       summary_by_region.csv
│
├───random_data
│       weather_small.csv
│
├───scripts
│   └───my_scripts
│       │   clean_data_v1.py
│       │   plot_helpers.py
│       │
│       └───__pycache__
│               clean_data_v1.cpython-313.pyc
│               plot_helpers.cpython-313.pyc
│
└───src
    │   analysis.py
    │
    └───utility
        │   file_stuff.py
        │
        └───__pycache__
                file_stuff.cpython-313.pyc
```


---

## Data

Two datasets are used in this project:

- **sales_jan.csv**  
  Contains transaction-level sales data for January.

- **customer_lookup.csv**  
  Maps customer IDs to geographic regions.

Both datasets are located in:

```bash
data/raw/
```

---

## Environment Setup

Two environment setup options are provided.

### Option 1 – pip

Create an environment and install dependencies:

```bash
pip install -r requirements.txt
```

### Option 2 – conda

Create the conda environment:
```bash
conda env create -f environment.yml
conda activate cmse492-hw01
```

## Run the Analysis

To reproduce the results, run:

```bash
python src/analysis.py
```

## Outputs

Running the analysis will generate the following files:

```bash
outputs/summary\_by\_region.csv  
outputs/revenue\_by\_region.png
```

- summary_by_region.csv – aggregated revenue by region

- revenue_by_region.png – visualization of revenue distribution