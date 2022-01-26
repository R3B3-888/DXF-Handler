import wget
import sys
import zipfile

# Change this to get your departement number corresponding
zip_file_name = "dep33.zip"

base_url = "https://cadastre.data.gouv.fr/data/dgfip-pci-vecteur/latest/dxf/departements/"

if __name__ == '__main__':
    # Download phase
    full_url = base_url + zip_file_name
    zip_path = "../output/" + zip_file_name
    wget.download(full_url, zip_path)
    print(f"\n{zip_file_name} download at {full_url}\n")
    
    do_extraction = input(f"Do you want to extract {zip_file_name} ? y/n : ")
    if do_extraction != 'y':
        exit("No extraction")
    else:
        if zipfile.is_zipfile(zip_path) is False:
            exit(f"{zip_file_name} is not a zip")
        else:
            with zipfile.ZipFile(zip_path) as z:
                z.extractall("../output/" + zip_file_name[:-4]) 
                exit("Extraction done")
