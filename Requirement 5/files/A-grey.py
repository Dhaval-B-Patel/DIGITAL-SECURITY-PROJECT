"""
import cv2
import sys
  
# importing library for plotting 
from matplotlib import pyplot as plt 
  
# reads an input image 
img = cv2.imread(sys.argv[1],0) 
  
# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
  
# show the plotting graph of an image 
plt.plot(histr) 
plt.show()
"""
import cv2
import sys
from matplotlib import pyplot as plt 
img = cv2.imread(sys.argv[1],0) 
  
# alternative way to find histogram of an image 
plt.hist(img.ravel(),256,[0,256]) 
plt.show() 