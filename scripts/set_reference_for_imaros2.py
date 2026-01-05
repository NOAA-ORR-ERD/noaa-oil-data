"""
Quick script to set the reference for IMAROS 2 oils
"""
import adios_db.scripting as ads


imaros2_ref = """Fanny Chever, Karine Tréguer, Justine Receveur, Julien Guyomarch, Marijke Neyts and Koen Parmentier (2025).
Summary report of WP3: Characterisation and impacts, deliverable D3.1, 38pp."""

for oil, path in ads.get_all_records("../data/oil/IM"):
    md = oil.metadata

    print(oil.oil_id)
    print(md.name)
    if "(IMAROS 2)" in md.name:
        md.reference.reference = imaros2_ref
        oil.to_file(path)




    # ID, name, product_type = oil.oil_id, md.name, md.product_type

    # if "hydraulic" in name.lower():
    #     new_pt = "Hydraulic Fluid"
    # elif 'lubricating' in name.lower():
    #     new_pt = "Lube Oil"
    # else:
    #     new_pt = None

    # if new_pt:
    #     print(ID, name, product_type, new_pt)
    #     outfile.write(f"{ID}\t{name}\t{product_type}\t{new_pt}\n")
    #     md.product_type = new_pt
    #     oil.to_file(path)





