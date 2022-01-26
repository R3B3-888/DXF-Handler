import os, csv, shutil

dep_name = "dep33/"
dep_path = "../output/" + dep_name
cities_path = "../output/cities/"
csv_cities_name = "../input/villesCodesPostaux.csv"

def copy_dxf_tbz2_to (code, base_dst):
    base_src = dep_path + code
    for dxf_tbz2 in os.listdir(base_src):
        src = base_src + "/" + dxf_tbz2
        dst = base_dst + dxf_tbz2
        shutil.copyfile(src, dst)

if __name__ == '__main__':
    with open(csv_cities_name) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            os.mkdir(os.path.join(cities_path, row["city"]))
            os.mkdir(os.path.join(cities_path + row["city"], "tar_bz2_files"))
            copy_dxf_tbz2_to(row["code"], cities_path + row["city"] + "/tar_bz2_files/")
    print("All city of csv file were created with their dxf tbz2 ready to extract")

