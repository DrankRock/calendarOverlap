#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color # Source --> https://stackoverflow.com/a/5947802

if [ $# -ne 1 ]
then
	echo "Usage : autoCheck.sh <your_csv_file>"
fi
i=1
while read line; do
	lineCut=$(echo $line | sed 's/,/ /g')
	# echo -e "${RED} [${i}] -- ${lineCut} ${NC} --> $result"
	# echo "[${i}] -- ${lineCut}"
	result=$(python3 calendarOverlap.py -c ${lineCut})

	if [[ ${result} ]]; then
		echo -e "${RED}[${i}] -- ${lineCut} ${NC} --> $result"
	else
		echo -e "${GREEN}[${i}] -- ${lineCut} ${NC}"
	fi
	i=$((i+1))
done < $1