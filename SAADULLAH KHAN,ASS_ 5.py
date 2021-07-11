#!/usr/bin/env python
# coding: utf-8

# In[ ]:


QS 4

My_Dict = {
        'person_1': {'name': 'Abdul Rafay', 'age': 22, 'Interests': ['football,cricket'],
                     'amount_deposited': [24000, 26000]},
        'person_2': {'name': 'Nancy James', 'age': 23, 'Interests': ['baseball,cricket'],
                     'amount_deposited': [24000, 27000]},
        'person_3': {'name': 'Selena Gomez', 'age': 26, 'Interests': ['baseball,table tennis'],
                     'amount_deposited': [24000, 28000]}
    }
def process(MY_Dic):
   alp = [chr(i) for i in range(97,104) if chr (i) not in [115,109,107]]
   alp = tuple(alp)
  
   mapping = list(map(lambda x : "Mr. "+x if str(x).lower().startswith(alp) else "Mrs. "+x, [My_Dict[i]["name"] for i in My_Dict]))
   return mapping


 s_m_k = [chr(x) for x in [115,109,107]]

 filtered_data= list(filter(lambda x : x.split(' ')[1][0].lower() not in s_m_k, process(My_Dict)))
 print(filtered_data)
    
from  functools import reduce
def processing(elements):
   #red_func = functools.reduce (lambda x,y: x[1]['amount_deposited'][0]+y[1]['amount_deposited'][1], elements.items() )

  for person  in elements.keys():
    elements[person]['amount_deposited'] = reduce(lambda x,y:x+y,list(elements[person]['amount_deposited']))
    
    print(person)
    print(str(elements[person]['amount_deposited']))
  

  # return red_func



print(processing(My_Dict))



QS 5

import csv

labels = ['Name', 'Age', 'Interests','Year', 'Amount Deposited'] dct_arr = [ {'Name': 'Mr. Abdul Rafay', 'Age': 22,'Interests':'baseball,cricket','Year':1997,'Amount Deposited':50000}, {'Name': 'Ms. Nancy James', 'Age': 23,'Interests':'baseball,cricket','Year':1998,'Amount Deposited':51000} ]

try: with open('names.csv', 'w') as f: writer = csv.DictWriter(f, fieldnames=labels) writer.writeheader() for elem in dct_arr: writer.writerow(elem) except IOError: print("I/O error")

#viewing csv file...

import pandas as pd pd.read_csv('names.csv')

