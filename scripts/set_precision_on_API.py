#!/usr/bin/env python3

"""
script to go through all the data, and add an API if one is not already there

This could use a bit more polish:
  - flag to have it report what it will do, but not do it
  - pass in a single file or the whole dir

Testing! -- not entirely sure if it breaks the records!
"""

import sys

from oil_database.models.oil.cleanup.density import FixAPI
from oil_database.scripting import get_all_records

USAGE = """
set_precision_on_API.py data_dir [dry_run]

This sets the precision in the JSON to 2 decimal place.

data_dir is the dir where the data are: the script will recursively
search for JSON files

If "dry_run" is on the command line, it will report what it would do,
but not save any changes
"""


def main():
    try:
        sys.argv.remove("dry_run")
        dry_run = True
    except ValueError:
        dry_run = False

    try:
        base_dir = sys.argv[1]
    except IndexError:
        print(USAGE)
        sys.exit(1)

    for rec, pth in get_all_records(base_dir):
        print(rec.oil_id, rec.metadata.API)
        try:
            rec.metadata.API = round(rec.metadata.API, 2)
            print("Setting to:", rec.metadata.API)
        except TypeError:
            pass
        if not dry_run:
            print("Saving out:", pth)
            rec.to_file(pth)
        else:
            print("Nothing saved")


if __name__ == "__main__":
    main()





