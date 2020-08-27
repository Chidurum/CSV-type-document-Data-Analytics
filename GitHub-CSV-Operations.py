# PYTHON NUMPY CODING DEMO - DATA ANALYTICS
#OBJECTIVE - To import comma-separated value (csv) files as dataframes
# To see how we can use real table fxn of pandas, how we use partial rows of a csv file into pandas
# how we can select specific column values of a csv file and import into a dataframe
# Where CSV means comma-separated values
# Start by preparing a CSV document in MS Notepad and save as Demo.csv
#Initialize this document by opening in Ms Excel template
#importing çsv as dataframe
#using readtable of pandas
#reading partial rows of .csv file
#Dumping data into a new CSV file
#selecting specific columns of a csv file

import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame
#dframe = pd.read_csv('demo1.csv')

dframe = pd.read_csv('demo1.csv',header=None)
print dframe
dframe2 = pd.read_table('demo1.csv',sep=',',header=None)
print dframe2
#Importing partial rows now
print pd.read_csv('demo1.csv',nrows=2,header=None)
dframe2.to_csv('outputCSV.csv',sep='!')

#NEXT - Selecting specific columns
dframe.to_csv('dataoutput.csv',columns=[1,0])
