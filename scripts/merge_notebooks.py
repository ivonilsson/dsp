import os
import glob
import nbformat
import re

def merge_notebooks_in_directory(directory):
    """
    Merges all notebooks
    """
    pattern = os.path.join(directory, "task*.ipynb")
    notebook_files = sorted(glob.glob(pattern))

    if not notebook_files:
        print(f"No notebooks found in {directory}. Skipping.")
        return

    merged_nb = nbformat.v4.new_notebook()

    for nb_file in notebook_files:
        try:
            with open(nb_file, "r", encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)
            merged_nb.cells.extend(nb.cells)
            print(f"Merged {nb_file} with {len(nb.cells)} cells.")
        except Exception as e:
            print(f"Error processing {nb_file}: {e}")
    
    output_dir = os.path.join(directory, "final_ipynb")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "group_number_2.ipynb")

    output_file = os.path.join(directory, output_file)
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            nbformat.write(merged_nb, f)
        print(f"Final merged notebook saved to {output_file}")
    except Exception as e:
        print(f"Error writing output file in {directory}: {e}")

def merge_notebooks_for_all_directories():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    
    for item in os.listdir(repo_root):
        dir_path = os.path.join(repo_root, item)

        if os.path.isdir(dir_path) and re.match(r'^a\d+$', item):
            print(f"Processing directory: {dir_path}")
            merge_notebooks_in_directory(dir_path)

if __name__ == "__main__":
    merge_notebooks_for_all_directories()
