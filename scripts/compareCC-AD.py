"""
quick script to look for AD records that may be an exact match for CC records
"""

import adios_db.scripting as ads

CC_names = {}
for oil, path in ads.get_all_records("../data/oil/CC"):
    print(oil.metadata.name)
    CC_names[oil.metadata.name] = (oil.oil_id, oil.metadata.source_id)

num_name_matches = 0
num_full_matches = 0
matches = []
for oil, path in ads.get_all_records("../data/oil/AD"):
    for name, stuff in CC_names.items():
        if oil.metadata.name == name:
            num_name_matches += 1
            if oil.metadata.source_id == stuff[1]:
                num_full_matches += 1
                matches.append((name, stuff[0], stuff[1], oil.oil_id, ))
for match in matches:
    print(match)

with open("CC-AD-matches.txt", 'w') as outfile:
    for match in matches:
        print(match)
        for f in match:
            outfile.write(f"{f}\t")
        outfile.write("\n")

print(f"{num_name_matches=}")
print(f"{num_full_matches=}")





