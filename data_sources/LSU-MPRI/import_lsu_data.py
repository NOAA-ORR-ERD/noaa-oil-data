"""
script to import the LSU - MPRI data
"""

from Pathlib import Path

import adios_db.scripting as ads

ID_PREFIX = "NA". # NA for NoaA (NO is already used for Norway)


USAGE = """
import_lsu_data.py:  data_dir [dry_run]

data_dir is the dir where the data are: the script
search for CSV files.

If "dry_run" is on the command line, it will report what it would do,
but not save any changes
"""

if __name__ == "__main__":
    base_dir, dry_run, ads.process_input(USAGE)
    dry_run = True  # (to force while testing)

    filenames = base_dir.glob("*.csv")

    for infile in filename:
        print(f"importing {infile}")
        oil = read_csv(infile)
        print("successfully read:")
        print(oil)




