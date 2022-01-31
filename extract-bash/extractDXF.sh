#!/bin/bash

# ./extractDXF.sh 07
month=$(date '+%B')
cities_file="villesCodesPostaux.txt"


log_file="log.txt"

unzip_directories () {
	code=$(echo $1 | rev | cut -c -5 | rev)
	dst_dir="unzip_codes_${month}/$code"
	mkdir -p $dst_dir
	unzip -o -j cadastres33_${month}.zip $code/* -d $dst_dir  >> $log_file
}

uncompress_bzip2 () {
	city=$(echo $1 | rev | cut -c6- | rev)
	code=$(echo $1 | rev | cut -c -5 | rev)
	src_dir="unzip_codes_${month}/$code"
	dst_dir="DXFfiles_${month}/$city"
	mkdir -p $dst_dir
	for compressedFiles in $src_dir/*; do
		tar -xf $compressedFiles -C $dst_dir >> $log_file
	done
}

main () {
	curl -o cadastres33_${month}.zip https://cadastre.data.gouv.fr/data/dgfip-pci-vecteur/latest/dxf/departements/dep33.zip >> $log_file
	echo "Latest zip downloaded !"
	for city_code in $(cat $cities_file); do
		unzip_directories $city_code
		uncompress_bzip2 $city_code
	done

	echo "Done !"
}

main