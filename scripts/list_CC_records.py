"""
Quick script to look for AD records that may be an exact match for CC records
"""

import adios_db.scripting as ads

with open("CC_recs_2-20-2025.txt", 'w') as outfile:

    outfile.write("ID\tName\tSource ID\tProduct Type\n")

    for oil, path in ads.get_all_records("../data/oil/CC"):
        md = oil.metadata
        rec = oil.oil_id, md.name, md.source_id, md.product_type

        print(rec)
        for f in rec:
            outfile.write(f"{f}\t")
        outfile.write("\n")




