"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pylab as pl
from PIL import Image
import numpy as np
import pylab

img = Image.open('rgb.png').convert('L')
z   = np.asarray(img)
mydata = z[::1,::1]
fig = pl.figure(facecolor='w')
ax1 = fig.add_subplot(1,2,1)
im = ax1.imshow(mydata,interpolation='nearest',cmap=pl.cm.jet)
ax1.set_title('2D')

ax2 = fig.add_subplot(1,2,2,projection='3d')
x,y = np.mgrid[:mydata.shape[0],:mydata.shape[1]]
ax2.plot_surface(x,y,mydata,cmap=pl.cm.jet,rstride=1,cstride=1,linewidth=0.,antialiased=False)
ax2.set_title('3D')
ax2.set_zlim3d(0,100)
pl.show()
"""

import numpy as np
from matplotlib import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

def getimarray(path):
    im = Image.open(path,'r')
    return np.array(im)

def doplots(path='t2.png'):

    mydata = getimarray(path)
    mydata = mydata[::5,::5]
    fig = pl.figure(facecolor='w')
    ax1 = fig.add_subplot(1,2,1)
    im = ax1.imshow(mydata,interpolation='nearest',cmap=pl.cm.jet)
    ax1.set_title('2D')
    ax2 = fig.add_subplot(1,2,2,projection='3d')
    x,y = np.mgrid[:mydata.shape[0],:mydata.shape[1]]
    ax2.plot_surface(x,y,mydata,cmap=pl.cm.jet,rstride=1,cstride=1,linewidth=0.,antialiased=False)
    ax2.set_title('3D')
    ax2.set_zlim3d(0,255)

    return fig,ax1,ax2

if __name__ == '__main__':
    doplots()
