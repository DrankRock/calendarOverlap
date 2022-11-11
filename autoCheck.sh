#!/bin/bash

if [ $# -ne 1 ]
then
	echo "Usage : autoCheck.sh <your_csv_file>"
fi
i=1
while read line; do
	lineCut=$(echo $line | sed 's/,/ /g')
	echo "[${i}] -- ${lineCut}"
	python3 calendarOverlap.py -c $lineCut
	i=$((i+1))
done < $1