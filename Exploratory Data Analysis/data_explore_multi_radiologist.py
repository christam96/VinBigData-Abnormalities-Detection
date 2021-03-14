import numpy as np
import pandas as pd 
import csv
import sys

#read csv, and split on "," 
train_csv = pd.read_csv('train.csv')
csv_file = csv.reader(open('train.csv', "r"), delimiter=",")
#dont read first csv line (column names)
header = next(csv_file) 

#arrays of unique and non unique image ids
unique=[]
non_unique=[]

#loop through the csv list
for row in csv_file:
    #add all entires to the list of non-unique
    non_unique.append(row[0])
    #to find unique ids, if row[0] not in unique list, add to list
    if row[0] not in unique:
        unique.append(row[0])

print("number of unique entries: "+str(len(unique)))
print("number of non-unique entries: "+str(len(non_unique)))

#count the number of disagreements among radiologists
disagreement_ctr = 0

#iteration counter
i=0

while i<15: #0-15
    #iterate through 1-1000,1000-2000,... 14000-15000
    unique_subset = unique[i*1000:(i+1)*1000]

    #loop through unique scans
    for entry in unique_subset:
        csv_file = csv.reader(open('train.csv', "r"), delimiter=",") # reset csv
        header = next(csv_file) #skip first line

        unique_rads = [] # unique radiologists for this specific scan
        current_abnormalities = [] # tuple list storing abnormality and radiologist
        #iterate through entire csv
        for row in csv_file:
            # check if this row matches entry considering currently 
            if row[0]==entry:
                current_abnormalities.append([row[3],int(row[2])])
                #check if radiologist is in list of radiologists 
                if row[3] not in unique_rads:
                    unique_rads.append(row[3])

        findings = []
        old_findings = []
        bool_consensus = 1 
        #comapre radiologist findings
        for radiologist in unique_rads:
            for each in current_abnormalities:
                if each[0] == radiologist:
                    findings.append(each[1])

            #check if findings is same as previous value
            if len(old_findings) > 0: #cant compare first radiologist to no one before them!
                if sorted(old_findings) != sorted(findings):
                    bool_consensus=0
       
            old_findings = findings #save old value
            findings = [] #reset findings

            if bool_consensus == 0:
                disagreement_ctr = disagreement_ctr+1
                break # stop looking at radiologists for this scan
            bool_consensus = 1 

        unique_rads = [] # resetting radiologists array 
    #final output    
    print("in this batch of " +str(len(unique_subset))+ " samples, "+str(disagreement_ctr)+" had disagreement among radiologists")
    print("iteration: "+str(i))
    i=i+1


