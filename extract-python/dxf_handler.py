import wget
import sys, os
import csv
import zipfile
import tarfile

from City import City

try:
    from Input.input_settings import *
except ImportError:
    sys.path.append(sys.path[0] + '/..')
    from Input.input_settings import *


def dl_dep_zip():
    wget.download(BASE_URL + ZIP_FILE_NAME, OUTPUT_PATH + ZIP_FILE_NAME)

def unzip_dep():
    if zipfile.is_zipfile(OUTPUT_PATH + ZIP_FILE_NAME) is False:
        exit(f"Error on {ZIP_FILE_NAME} path or file")
    else:
        with zipfile.ZipFile(OUTPUT_PATH + ZIP_FILE_NAME) as z:
            z.extractall(OUTPUT_PATH + ZIP_FILE_NAME[:-4])


def create_city_objects():
    global cities
    cities = {}
    with open(INPUT_PATH + CITIES_FILE) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            name = row['city']
            cities[name] = City(name, row['code']) 

def generate_dir_archi():
    CITIES_ROOT = OUTPUT_PATH + CITIES_FILE[:-4]
    os.mkdir(os.path.join(OUTPUT_PATH, CITIES_FILE[:-4]))
    for i in cities:
        os.mkdir(os.path.join(CITIES_ROOT, cities[i].get_name()))
        cities[i].set_path(CITIES_ROOT)


def extract_dxf_in_archi():
    DEP_ROOT = OUTPUT_PATH + ZIP_FILE_NAME[:-4] + "/"
    for i in cities:
        code = cities[i].get_code()
        dst = OUTPUT_PATH + CITIES_FILE[:-4] + "/" + cities[i].get_name() + "/"
        for dxf_tbz2 in os.scandir(DEP_ROOT + code):
            with tarfile.open(dxf_tbz2) as d:
                d.extractall(dst)
                

if __name__ == '__main__':
    dl_dep_zip()
    print(f"{ZIP_FILE_NAME} has been download in Output/{ZIP_FILE_NAME}")
    unzip_dep()
    print(f"{ZIP_FILE_NAME} has been extracted in Output/{ZIP_FILE_NAME[:-4]}")

    create_city_objects()

    generate_dir_archi()
    print(f"All architecture of {CITIES_FILE[:-4]} has been setup in {OUTPUT_PATH}")

    extract_dxf_in_archi()
    print("Extraction of all the dxf files is finished !")
