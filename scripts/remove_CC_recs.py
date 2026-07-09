from pathlib import Path
import os

infile = open("CC-AD-matches.txt")

for line in infile:
    ID = line.split("\t")[1]
    fn = Path("../data/oil/CC/") / (ID + ".json")

    print("removing:", fn)
    cmd = f"git rm {fn}"
    os.system(cmd)

