
# README — Task A: Cleaning and Combining Supplier Data

## What I Did
The goal of this task was to clean and combine two supplier datasets into one final inventory dataset named inventory_dataset.csv.

Supplier 1 and Supplier 2 provide similar information, but in different formats and with slightly different fields. Supplier 1 includes details like quality, grade, finish, thickness, width, description, weight, quantity, and some mechanical properties. Supplier 2 provides material, description, weight, quantity, and reserved status.

I cleaned both datasets, standardized their columns, handled missing values, and fixed encoding issues so that the data is consistent, complete, and ready for further analysis.

## Steps I Followed
I first read both datasets and checked that the files loaded correctly. I then created a function to process each supplier dataset individually. This function maps the supplier-specific column names to a common format, ensures consistent naming using snake_case, and fills missing columns with empty values when needed.

For columns that exist in one supplier but not in the other, I kept them as empty so that both datasets align when combined. I also preserved important free-text columns like description. After cleaning, I combined the two datasets into a single inventory dataset.

I paid special attention to German characters such as ü, ö, and ß, which sometimes display incorrectly due to encoding issues. By saving the final CSV in UTF-8 format with a BOM (utf-8-sig), these characters now display correctly in Excel.

Finally, I normalized the reserved column to True/False to make the dataset more business-friendly. I also validated the dataset to check for missing values, row counts per supplier, and basic statistics for numeric columns.

Issues Faced and How I Solved Them
German characters like ü were appearing incorrectly as Ã¼. This was caused by encoding problems when saving or opening the file in Excel. I resolved this by saving the final CSV with UTF-8 encoding including a BOM, which ensures that Excel correctly displays German letters.

The description column appeared empty in some cases. This was because sometimes Excel files contain cells that look filled but are read as blank by pandas. I made sure to preserve any existing text and only leave cells empty when they are genuinely missing.

The Quality/Choice column from Supplier 1 was showing NaN in Jupyter Notebook. This was caused by differences in column naming or extra spaces in the original dataset. I mapped it carefully to the final column name quality_choice and ensured whitespace was removed so that the values display correctly. For Supplier 2, this column remains empty because it is not provided, which is expected.

## Assumptions I Made
Since Supplier 2 does not provide thickness, width, finish, or mechanical properties, I left these fields empty for their rows. Similarly, Supplier 1 does not provide Article ID, so I left it blank for Supplier 1 rows.

I assumed that Description, even if it is free-text or in German, is useful information, so I preserved it as-is for both suppliers.

I standardized all column names to snake_case for consistency and clarity. For missing values in any column, I kept them empty rather than trying to guess or fill values, to maintain data accuracy.

For the Reserved column in Supplier 2, I normalized the values to True/False to make it easier to interpret and analyze later.

Finally, I assumed that the final dataset should retain all available information from both suppliers without losing any key columns, even if some are empty for one supplier.

## Outcome
The final inventory dataset has all columns aligned, cleaned, and standardized. Missing values are handled properly. German characters display correctly in Excel. Free-text columns like description are preserved, and numeric fields have been validated. The dataset is ready for further analysis or use in Task B.

This work demonstrates careful data cleaning, thoughtful handling of missing values and special characters, and attention to business relevance, making the dataset reliable and useful for analysis.

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
## Task A

Open the Task A notebook in Jupyter Notebook.

Run each cell sequentially from top to bottom.

The final output, inventory_dataset.csv, will be saved in the outputs folder.

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
