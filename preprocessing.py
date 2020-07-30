# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:33:16 2020

@author: lucab
"""
import pandas as pd
import numpy as np
data=pd.read_csv('FakeNamesCanada.csv',delimiter=';')
'''
1.Convert data to right format
some balance entries have some text ('Mastercard')
dates have problems
zip code has problems
2. Move NaN and other non expected data
3. Check format of zip code
4. Check for upper and lower limits of birthday
...
Also do homework:
'''
#to find out the problematic entries one only needs to check the 
#length of the list in which you append the new values
from datetime import datetime
date=[]
balance=[]
Balance=[]
defect=[23076,65536,121363]
for i in range(len(data.Birthday)):
    if i in defect:
        pass
    else:
        date_time_str = data.Birthday[i]
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
        date.append(date_time_obj)
    s=data.Balance[i]
    balance.append(s.replace('$',''))
    S=balance[i]
    Balance.append(S.replace(',',''))
balance=[]#to avoid having too many lists, I just reset this
#since we don't need it anymore
[defect.append(i) for i in range(23068,23077)]
defect.append(190807)
for i in range(len(Balance)):
    if i in defect:
        pass
    else:    
        balance.append(float(Balance[i]))
#Check format of zip code
import re
for i in range(len(data.ZipCode)):
    matched = re.match("[A-Z][0-9][A-Z] [0-9][A-Z][0-9]", data.ZipCode[i])
    is_match = bool(matched)
    if is_match==False:
        defect.append(i)
 #check date limits
delta=[]
for i in range(len(date)):
    delta.append((datetime.today()-date[i]).days)
    if delta[i]<4000: #11 y old
        defect.append(i)
    elif delta[i] > 40000: #110 y old:
        defect.append(i)    
#interest rate
Data=data.drop(defect)
Data=Data.set_index(np.arange(len(Data.Birthday)))
rate=[]
Rate=[]
for i in range(len(Data)):
    Rate.append(Data.InterestRate[i].replace('%',''))
    rate.append(float(Rate[i])/100)
    
'''
Now we have presumably identified all defects and need to figure
out what to do with them, probably some of them can be fixed,
but being len(defect)=74, which is very small compared to the
dataset, I think the rows should be just eliminated.
'''

Date=[]
balance=[]
alance=[]
Balance=[]
for i in range(len(Data.Birthday)):
    Date.append(datetime.strptime(Data.Birthday[i], '%Y-%m-%d'))
    s=Data.Balance[i]
    balance.append(s.replace('$',''))
    S=balance[i]
    alance.append(S.replace(',',''))
    Balance.append(float(alance[i]))
Data=Data.drop(['Birthday'],axis=1)
Data=Data.drop(['Balance'],axis=1)
Data=Data.drop(['InterestRate'],axis=1)
Data=Data.drop(['Number'],axis=1)
Data['InterestRate']=rate
Data['Balance']=Balance
Data['Birthday']=Date
Data.to_csv('processed_FakeNamesCanada.csv')
Data.to_excel('processed_FakeNamesCanada.xlsx')