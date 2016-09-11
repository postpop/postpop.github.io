#!/bin/bash
# declare STRING variable
DATUM="$(date +'%Y/%m/%d')"
echo $DATUM
FILELIST=(index read about)
ELEMENTS=${#FILELIST[@]}
for (( i=0;i<$ELEMENTS;i++)); do
   FILEBASE=${FILELIST[${i}]}
   echo $FILEBASE
	pandoc -o $FILEBASE.html -c style.css --data-dir . --template template.html --metadata date=$DATUM ./$FILEBASE.md
done 

