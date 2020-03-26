#Ciphers an image by shuffling its pixels using a Henon Map

from PIL import Image
import os
import random
import os
import math
import pickle
import textwrap
import matplotlib.pyplot as plt

import cv2 as cv
import numpy as np
from imageio import imread
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches



path=str(input("Enter original image name -- "))
password=str(input("password -- "))
byte_array = password.encode()
binary_int = int.from_bytes(byte_array, "big")
binary_string = bin(binary_int)
binary_string = binary_string[2:]
num=int(binary_string,2)
print("number key is -- ",end='')
print(num)

im = Image.open("../../files/"+path)
px = im.load()
w, h = im.size
count=w*h
#--------------------------------------------------------------------------------------------------------------------------------------------
li=[]
if os.path.exists('../../files/state.dat'):
    # Restore the previously saved sate
    print('Found state.dat, initializing random module')
    with open('../../files/state-image.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # This is called when no state.dat file is found Use a well-known start state
    print('No state.dat found seeding with-- ', end=''  )
    print(num)
    random.seed(num)

# generate random numbers
print("generating total of random numbers -- ",end='' )
print(count)
for i in range(count+1):
    ra=(random.random())
    li.append(ra)

# This code is to Save state for next time
with open('../../files/state-image.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

file=open("../../files/RN.txt","w+")
for i in li:
    file.writelines(str(i))
    file.write(';')
file.close()
#--------------------------------------------------------------------------------------------------------------------------------------------    
vals = []
vals2 = []
xrl=[]
yrl=[]
rxrl=[]
ryrl=[]
for i in range(0, h * w):
    #generate random parameters for hanaon map
    li[i]=1+li[i]
    li[i+1]=1+li[i+1]
    if li[i+1]>li[i]:
        temp=li[i+1]
        li[i+1]=li[i]
        li[i]=temp
    y0=li[i]
    x0=li[i+1]
    #implement haenon map
    #a=1.4 b=0.3
    x = 1 - 1.4 * pow(x0, 2) + y0
    y = 0.3 * x0
    xr = int(('%.11f' % (x))[4:9]) % w
    yr = int(('%.11f' % (y))[4:9]) % h
    vals.append((xr, yr))
    xrl.append(xr)
    yrl.append(yr)
    #uncomment part below if you want to see how algo works but only for 10*10 pixel image
    #plt.plot(xrl,yrl)
    #plt.show()
    #ucommnet below lines when testing this code for image with pixels greater than 10*10 pixels
    #fig="../../gif/fig"+str(i)
    #plt.savefig(fig)
    #plt.clf()
#plt.show()


vals.reverse()
for i in range(0, h * w):
    (xr, yr) = vals[i]
    j = h * w - i - 1
    p = px[j % w, int(j / w)]
    pr = px[xr, yr]
    px[j % w, int(j / w)] = pr
    px[xr, yr] = p
    #rxrl.append(j)
    #ryrl.append(p)
    #vals2.append((rxrl,ryrl))
#red value is represented by blue
#blue value is represented by green
#green value is represented by orange3
    #plt.plot(rxrl,ryrl)
    #plt.show()
    #plt.clf()

path2=str(input("Save as -- "))
im.save('../../files/'+path2)
t2='../../files/'+path2
t1='../../files/'+path

#--------------------------------------------------------------------------------------------------------------------------------------------
#plot centeroid color of the image
#uncomment the code in commnets if you want to find most dominating color in a pixel averages
image = imread(t1)
plt.imshow(image)
img  = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
rows, cols, _ = img.shape
#color_B = 0
#color_G = 0
#color_R = 0
#color_N = 0 # neutral/gray color
bl=0
gr=0
re=0
for i in range(rows):
    for j in range(cols):
        k = img[i,j] 
        bl=bl+k[0]
        gr=gr+k[1]
        re=re+k[2]
        #if k[0] > k[1] and k[0] > k[2]:
        #    color_B = color_B + 1
        #    continue
        #if k[1] > k[0] and k[1] > k[2]:
        #    color_G = color_G + 1
        #    continue        
        #if k[2] > k[0] and k[2] > k[1]:
        #    color_R = color_R + 1
        #    continue
        #color_N = color_N + 1

pix_total = rows * cols
#print('the most dominanat channel average in image is-  ')
#print('Blue:', (color_B/pix_total)*255, 'Green:', (color_G/pix_total)*255, 'Red:',  (color_R/pix_total)*255, 'Gray:',  (color_N/pix_total)*255)
print('centroid of image is at - ')
print('Blue:', (bl/pix_total), 'Green:', (gr/pix_total), 'Red:',  (re/pix_total))
red='Red: '+ str(re/pix_total)
green='Green: '+str(gr/pix_total)
blue='Blue: '+ str(bl/pix_total)
#grey='grey: '+ str((color_N/pix_total)*255)
labt="CENTROID"
red_patch = mpatches.Patch(color='red', label=red)
blue_patch = mpatches.Patch(color='blue', label=blue)
green_patch = mpatches.Patch(color='green', label=green)
#grey_patch = mpatches.Patch(color='grey', label=grey)
lab=mpatches.Patch(color='white', label=labt)
plt.legend(handles=[lab,red_patch,blue_patch,green_patch])
#plt.plot(color_R,color_G,color_B)
plt.show()
plt.clf()

#plot centroid after encryption
image = imread(t2)
plt.imshow(image)
img  = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
rows, cols, _ = img.shape
#color_B = 0
#color_G = 0
#color_R = 0
#color_N = 0 # neutral/gray color
bl=0
gr=0
re=0
for i in range(rows):
    for j in range(cols):
        k = img[i,j] 
        bl=bl+k[0]
        gr=gr+k[1]
        re=re+k[2]
        #if k[0] > k[1] and k[0] > k[2]:
        #    color_B = color_B + 1
        #    continue
        #if k[1] > k[0] and k[1] > k[2]:
        #    color_G = color_G + 1
        #    continue        
        #if k[2] > k[0] and k[2] > k[1]:
        #    color_R = color_R + 1
        #    continue
        #color_N = color_N + 1

pix_total = rows * cols
#print('the most dominanat channel average in image is-  ')
#print('Blue:', (color_B/pix_total)*255, 'Green:', (color_G/pix_total)*255, 'Red:',  (color_R/pix_total)*255, 'Gray:',  (color_N/pix_total)*255)
print('centroid of image is at - ')
print('Blue:', (bl/pix_total), 'Green:', (gr/pix_total), 'Red:',  (re/pix_total))
red='Red: '+ str(re/pix_total)
green='Green: '+str(gr/pix_total)
blue='Blue: '+ str(bl/pix_total)
#grey='grey: '+ str((color_N/pix_total)*255)
labt="CENTROID"
red_patch = mpatches.Patch(color='red', label=red)
blue_patch = mpatches.Patch(color='blue', label=blue)
green_patch = mpatches.Patch(color='green', label=green)
#grey_patch = mpatches.Patch(color='grey', label=grey)
lab=mpatches.Patch(color='white', label=labt)
plt.legend(handles=[lab,red_patch,blue_patch,green_patch])
#plt.plot(color_R,color_G,color_B)
plt.show()
plt.clf()