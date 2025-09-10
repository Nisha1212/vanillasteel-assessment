
# Task B — RFQ Similarity

Hi! This is my submission for Task B, where I worked on finding similar RFQs (Request for Quotations) using the reference properties dataset. I also included some bonus analyses like alternative metrics, ablation analysis, and clustering. Below, I explain what I did step by step, why I did it this way, and what we learned.

---

## **Step 1: Load and Inspect Data**

I loaded `rfq.csv` and `reference_properties.tsv` and checked the columns.  

- This helps me understand what features are available.  
- I could see which features are numeric, categorical, or have missing values.  

**Outcome:** I know the structure of the data and which columns to process next.

---

## **Step B.1 — Reference Join & Missing Values**

- I normalized RFQ grades and reference grades (lowercase, stripped spaces) to match exactly.  
- I parsed numeric ranges like `2.5-3.0` or `≤5` into min, max, and mid values.  
- RFQs were merged with reference data on normalized grades.  
- Missing references were flagged to know which RFQs don’t have reference properties.  

**Why:** Normalization ensures matching; parsing numeric ranges lets us compute numeric similarity.  
**Assumptions:** If max value is missing, I set max = min.  
**Outcome:** RFQs now have corresponding reference data with missing ones flagged.

---

## **Step B.2 — Feature Engineering**

- Created min, max, and mid columns for numeric dimensions and grades.  
- Filled missing max values with min.  
- Kept categorical features like `coating`, `finish`, `form`, `surface_type`.  

**Why:** This allows numeric similarity computations and categorical comparisons.  
**Outcome:** RFQs have clean numeric and categorical features ready for similarity calculations.

---

## **Step B.3 — Similarity Calculation**

- **Numeric similarity:** Computed **Interval IoU** for each numeric dimension.  
- **Categorical similarity:** 1 if values match, 0 if different, averaged across all categories.  
- **Grade similarity:** Ratio of smaller/larger for numeric grade properties.  
- Combined all similarities using weighted average: dimensions 0.5, categorical 0.2, grades 0.3.  
- Extracted **top-3 most similar RFQs** per RFQ.  

**Why:** Weighted combination captures all aspects of similarity.  
**Assumptions:** Equal importance per numeric dimension, exact match for categorical features.  
**Outcome:** `top3.csv` with RFQ ID, top-3 matches, and similarity scores.

---

## **Step B.4 — Alternative Metrics & Ablation Analysis (Bonus)**

- Used **cosine similarity** for numeric features and **Jaccard similarity** for categorical features.  
- Weighted combination of dimensions, grades, and categorical features.  
- Ablation analysis: tested dropping one feature group at a time to see the impact.  

**Why:** To check if other metrics improve similarity and which features contribute most.  
**Outcome:** `top3_bonus.csv` and plots showing feature impact.

---

## **Step B.5 — Clustering RFQs (Bonus)**

- Standardized numeric features and combined with one-hot encoded categorical features.  
- Used **KMeans** to cluster RFQs into 5 clusters.  
- Visualized clusters using **PCA** in 2D.  
- Saved `rfq_with_clusters.csv` and `pca_coordinates.csv`.  

**Why:** Helps understand structure and group similar RFQs together.  

---

## **Assumptions & Issues Faced**

- Missing numeric values: filled with 0 for similarity or min = max.  
- Some reference columns missing in the dataset; handled dynamically.  
- Performance: iterating over all RFQs is slow; used `tqdm` to monitor progress.  

---

## **Outputs**

- `top3.csv` — Top-3 most similar RFQs (Task B).  
- `top3_bonus.csv` — Top-3 using alternative metrics.  
- `rfq_with_clusters.csv` — RFQs with cluster assignments.  
- `pca_coordinates.csv` — 2D PCA coordinates for plotting clusters.  

---

## **How to Run the Pipeline**

- Everything is in `TaskB_notebook.ipynb` and can be executed end-to-end.  
- Alternatively, use `run.py` to execute the full pipeline in one go.  
- All outputs will be saved in the `outputs/` folder.

# Setup and Run Instructions
1. Python Environment

These notebooks are written in Python 3.

It is recommended to use Conda to manage your environment and dependencies.

## To create a new environment, you can run:

conda create -n vanillasteel python=3.10
conda activate vanillasteel


## Install required packages using pip or conda. Here are the main libraries used in the notebooks:

pandas

numpy

openpyxl

matplotlib

seaborn

scikit-learn

re (regular expressions)

## Any other standard Python libraries

You can install them with:

pip install pandas numpy openpyxl matplotlib seaborn scikit-learn

## 2. Folder Structure

Make sure your project folder is organized like this:

vanillasteel-assessment/
│
├── notebooks/          # All Task A, Task B, Bonus Task notebooks
├── data/               # Supplier files and any other input data
├── outputs/            # Folder to save processed CSV files
├── README-taskA.txt
├── README-taskB.txt
├── bonus_task_output/  # Folder to save outputs from the bonus task
├── README-Bonus.md


The data folder contains supplier files (e.g., supplier_data1.xlsx, supplier_data2.xlsx) needed for Task A.

The outputs folder is where the CSV files generated by the notebooks (e.g., inventory_dataset.csv, top3.csv) will be saved. Ensure this folder already exists.

## 3. Running the Notebooks
## Task B

Task B is in a separate notebook.

Open the Task B notebook and run cells sequentially.

The output file top3.csv will be saved in the outputs folder.

Task B does not depend on the outputs of Task A.

Note: CSV files are saved using UTF-8 with BOM (utf-8-sig) encoding so that special characters like German letters (ü, ö, ß) display correctly in Excel.
## 4. Notes on CSV and Excel

If opening CSV files in Excel, make sure to choose UTF-8 encoding to view German characters correctly.

In Excel:

Open Excel.

Go to Data → Get Data → From Text/CSV.

Select the file and set File Origin to UTF-8.

This ensures columns like description and finish display correctly without garbled text.

## 5. Optional

If using Jupyter Notebook, make sure your kernel is set to the Python environment you installed with the required libraries.

Always check the outputs folder to ensure CSV files are generated correctly after running the notebooks.
