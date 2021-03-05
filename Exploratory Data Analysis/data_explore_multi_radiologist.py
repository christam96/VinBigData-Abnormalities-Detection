import numpy as np
import pandas as pd 
import csv
import sys

train_csv = pd.read_csv('train.csv')

#read csv, and split on "," the line
csv_file = csv.reader(open('train.csv', "r"), delimiter=",")
#dont read first csv line
header = next(csv_file) 

# #arrays of unique and non unique ids
unique=[]
non_unique=[]

#loop through the csv list
for row in csv_file:
    non_unique.append(row[0])
    # to find unique ids, if row[0] not in unique list, add to list
    if row[0] not in unique:
        unique.append(row[0])

print("number of unique entries: "+str(len(unique)))
print("number of non-unique entries: "+str(len(non_unique)))

# can loop through unique ones identifies
unique_25 = unique[0:5] #first 25 unique entries 
print(unique_25)

for entry in unique_25:
    csv_file = csv.reader(open('train.csv', "r"), delimiter=",") # reset csv
    header = next(csv_file) #skip first line

    print("currently on entry: "+ entry)
    unique_rads = [] # unique radiologists for this specific scan
    #iterate through entire csv
    for row in csv_file:
        # check if this row matches entry considering currently 
        if row[0]==entry:
            #check if radiologist is in list of radiologists 
            if row[3] not in unique_rads:
                unique_rads.append(row[3])
                print("first abnormality detected by radiologist: "+row[3])
            else:
                #this means the same radiologist is identifying multiple from the same scan
                print("more than one abnormality detected from radiologist: "+row[3])
    print(unique_rads)
    unique_rads = [] # resetting radiologists array 

# ideas to show differences by radiologist:
    #-> number of things identified in scan by each radiologist (count how many entries from same R) 

