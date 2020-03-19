"""
#from matplotlib.pyplot import pyplot as plt
#from matplotlib import style
from matplotlib import pyplot as plt
import csv
import sys
from numpy import genfromtxt
#style.use('ggplot')
path='../files/'+sys.argv[1]
x=[]
y=[]
plt.plot(x,y, marker='o')
plt.title('prime number generation rate')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
"""
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import plotly.graph_objects as go
 
 
 
numFiles = 1 #Number of CSV files in your directory
separator = "," #Character that separates each value inside file
fExtension = ".csv" #Extension of the file storing the data
dataframe = sorted(glob('prime*.csv'))
pd.concat((pd.read_csv(file).assign(filename = file)
           for file in dataframe), ignore_index  = True) 
plt.plot(list(str(dataframe)) )
plt.show()