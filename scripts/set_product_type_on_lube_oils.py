"""
Quick script to set the product type on lube oils
"""
import adios_db.scripting as ads


with open("Lube_records.txt", 'w') as outfile:

    outfile.write("ID\tName\tProduct Type\n")

    for oil, path in ads.get_all_records("../data/oil/CC"):
        md = oil.metadata

        ID, name, product_type = oil.oil_id, md.name, md.product_type

        if "hydraulic" in name.lower():
            new_pt = "Hydraulic Fluid"
        elif 'lubricating' in name.lower():
            new_pt = "Lube Oil"
        else:
            new_pt = None

        if new_pt:
            print(ID, name, product_type, new_pt)
            outfile.write(f"{ID}\t{name}\t{product_type}\t{new_pt}\n")
            md.product_type = new_pt
            oil.to_file(path)





