# Assignment-5

import csv

labels = ['Name', 'Age', 'Interests','Year', 'Amount Deposited'] 
dct_arr = [
  {'Name': 'Mr. Abdul Rafay', 'Age': 22,'Interests':'baseball,cricket','Year':1997,'Amount Deposited':50000},
  {'Name': 'Ms. Nancy James', 'Age': 23,'Interests':'baseball,cricket','Year':1998,'Amount Deposited':51000}
  ]

try:
    with open('names.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in dct_arr:
            writer.writerow(elem)
except IOError:
    print("I/O error")

#viewing csv file...

import pandas as pd
pd.read_csv('names.csv')
