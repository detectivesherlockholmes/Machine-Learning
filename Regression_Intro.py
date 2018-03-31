'''
Created on 31-Mar-2018

@author: mayank
'''
import pandas as pd
import quandl

df= quandl.get('WIKI/GOOGL')
print(df.head)
