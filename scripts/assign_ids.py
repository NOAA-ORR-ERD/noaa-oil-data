#!/usr/bin/env python
"""
script to assign IDs to new records

python assign_ids.py PREFIX save

Where PREFIX is one of the 2 char codes, e.g.

AD, EC, ...

It will look for records in the XX dir

It should be run in this directory
"""
import sys
from pathlib import Path
import adios_db.scripting as ads


if __name__ == "__main__":

    oil_path = Path() / ".." / "data/oil"
    prefix = sys.argv[1]
    if len(prefix) != 2:
        raise ValueError("expecting a two char prefix")
    else:
        prefix = prefix.upper()

    print(f"Assigning to ID in: {prefix}")

    last_id = ads.find_highest_id(prefix, oil_path)
    id_num = int(last_id[2:])
    for rec in (oil_path / 'XX').glob("XX?????.json"):
        id_num += 1
        oil = ads.Oil.from_file(rec)
        new_id = f"{prefix}{id_num:05}"
        oil.oil_id = new_id
        print(f"setting new id: {new_id}")
        new_path = oil_path / prefix / f"{new_id}.json"
        print("saving to:", new_path)
        if 'save' in sys.argv:
            oil.to_file(new_path)
        else:
            print("not saving")


def test_find_highest_id():
    oil_path = Path() / ".." / "data/oil"

    hid = ads.find_highest_id("AD", oil_path)

    assert hid == "AD02611"

