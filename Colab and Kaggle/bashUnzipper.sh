#!/bin/bash

for i in {0..124}; do
  pathToCorruptedZipDrive="/content/drive/MyDrive/VinBigData/train/dataset.part"$i
  pathToCorruptedZipColab="/content/dataset.part"$i
  pathToColab="/content/"
  pathToFixedZipColab="/content/drive/MyDrive/VinBigData/train_data/"
  echo "copying part "$i
  mv $pathToCorruptedZipDrive $pathToColab
  zip -FF $pathToCorruptedZipColab --out $pathToCorruptedZipColab".zip"
  rm $pathToCorruptedZipColab
  unzip $pathToCorruptedZipColab".zip" -d $pathToFixedZipColab
  rm $pathToCorruptedZipColab".zip"
done

