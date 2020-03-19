import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import PIL
from PIL import Image
from matplotlib import pyplot as plt

"""
img = cv2.imread(sys.argv[1])
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

"""

im = Image.open(sys.argv[1])  
w, h = im.size  
colors = im.getcolors(w*h)

def hexencode(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    return '#%02x%02x%02x' % (r,g,b)

for idx, c in enumerate(colors):
    plt.bar(idx, c[0], color=hexencode(c[1]))

plt.show()