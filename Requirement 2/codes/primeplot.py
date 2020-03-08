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
