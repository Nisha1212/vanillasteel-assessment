#!/usr/bin/env python3
"""
run.py

Run the Task B notebook and check / create outputs.
Designed for this project layout:

vanillasteel-assessment/
  data/
    rfq.csv
    reference_properties.tsv
  notebooks/
    taskB_RFQ_similarity.ipynb
  outputs/
    top3.csv
    README-Task B.md    # (optional)
  run.py                # <-- this file
"""

import os
import sys
import subprocess
import shutil

def get_paths():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(project_dir, "data")
    notebooks_dir = os.path.join(project_dir, "notebooks")
    outputs_dir = os.path.join(project_dir, "outputs")

    notebook_path = os.path.join(notebooks_dir, "taskB_RFQ_similarity.ipynb" )
    readme_path = os.path.join(outputs_dir, "README-Task B.md")
    top3_path = os.path.join(outputs_dir, "top3.csv")

    return {
        "project_dir": project_dir,
        "data_dir": data_dir,
        "notebooks_dir": notebooks_dir,
        "outputs_dir": outputs_dir,
        "notebook_path": notebook_path,
        "readme_path": readme_path,
        "top3_path": top3_path,
    }


def run_notebook(notebook_path):
    """
    Try to execute the notebook in-place.

    Tries 'jupyter nbconvert' first; if not available, falls back to
    'python -m nbconvert'. Raises on failure.
    """
    args = ["nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path]

    # Try 'jupyter' first
    jupyter_cmd = shutil.which("jupyter")
    if jupyter_cmd:
        cmd = ["jupyter"] + args
    else:
        # fallback: python -m nbconvert
        cmd = [sys.executable, "-m", "nbconvert"] + args

    print(f"Running notebook with command: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    print("Notebook executed successfully.")


def ensure_outputs_dir(outputs_dir):
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir, exist_ok=True)
        print(f"Created outputs directory: {outputs_dir}")


def create_default_readme(readme_path):
    """
    Create a default README if the user doesn't have one in outputs/.
    """
    default_text = f
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(default_text)
    print(f"Default README written to: {readme_path}")


def main():
    paths = get_paths()
    project_dir = paths["project_dir"]
    print(f"Project dir: {project_dir}")

    # Ensure outputs dir exists
    ensure_outputs_dir(paths["outputs_dir"])

    # Basic checks
    if not os.path.isdir(paths["data_dir"]):
        print(f"WARNING: data/ directory not found at expected location: {paths['data_dir']}")
    else:
        print(f"Found data/ at: {paths['data_dir']}")

    if not os.path.isdir(paths["notebooks_dir"]):
        print(f"ERROR: notebooks/ directory not found at expected location: {paths['notebooks_dir']}")
        print("Please ensure your notebook is in notebooks/ and retry.")
        sys.exit(1)

    if not os.path.isfile(paths["notebook_path"]):
        print(f"ERROR: Notebook not found: {paths['notebook_path']}")
        print("Make sure the file name matches the NOTEBOOK_NAME in this script.")
        sys.exit(1)

    # Run the notebook
    try:
        print("\n--- Executing notebook ---")
        run_notebook(paths["notebook_path"])
    except subprocess.CalledProcessError as e:
        print("ERROR: Notebook execution failed.")
        print("Command returned non-zero exit status.")
        print("Details:", e)
        sys.exit(1)
    except Exception as e:
        print("ERROR: Unexpected error while running notebook:", e)
        sys.exit(1)

    # Check for top3 result and README in outputs/
    print("\n--- Checking outputs ---")
    if os.path.isfile(paths["top3_path"]):
        print(f"✅ Found top3 results: {paths['top3_path']}")
    else:
        print(f"⚠ top3 file not found at {paths['top3_path']}.")
        print("If the notebook should produce top3.csv, check the notebook cell that writes outputs/top3.csv")

    if os.path.isfile(paths["readme_path"]):
        print(f"✅ README found in outputs: {paths['readme_path']}")
    else:
        print(f"⚠ README not found at {paths['readme_path']}. Creating a default README now.")
        try:
            create_default_readme(paths["readme_path"])
        except Exception as e:
            print("ERROR: Could not create default README:", e)

    print("\nAll done. Check the outputs/ folder for results.")
    print("If anything is missing, open the notebook, run the cells manually and inspect the cells that save files.")

if __name__ == "__main__":
    main()