#!/bin/bash

OUTPUT=$(python /content/generatePathsBrokenImgs.py)

IFS=' ' read -ra array <<< "$OUTPUT"

for i in "${array[@]}"; do
  kaggle competitions download -c vinbigdata-chest-xray-abnormalities-detection -f train/$i 
  unzip $i
  rm $i".zip"
  mv $i "/content/gdrive/MyDrive/VinBigData/train_data/"
done

pwd