#importing the lib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import the dataset
dataset=pd.read_csv('Salary_Data.csv')
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,:2]