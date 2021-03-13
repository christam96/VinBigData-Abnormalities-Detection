#!/bin/bash

OUTPUT=$(python /content/bashGenerator.py)

IFS='*' read -ra array <<< "$OUTPUT"

for i in "${array[@]}"; do
  eval "$i"
done

pwd
