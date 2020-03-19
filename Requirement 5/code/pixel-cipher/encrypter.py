#Ciphers an image by shuffling its pixels using a Henon Map

from PIL import Image
import os
import random
import os
import math
import pickle
import textwrap


path=str(input("Enter image name -- "))
password=str(input("password -- "))
byte_array = password.encode()
binary_int = int.from_bytes(byte_array, "big")
binary_string = bin(binary_int)
binary_string = binary_string[2:]
num=int(binary_string,2)
print("number key is -- ",end='')
print(num)

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

# generate two random numbers
for i in "12":
    ra=(random.random())
    li.append(ra)
    print(ra)

# This code is to Save state for next time
with open('../../files/state-image.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

file=open("../../files/RN.txt","w+")
for i in li:
    file.writelines(str(i))
    file.write(';')
file.close()
#--------------------------------------------------------------------------------------------------------------------------------------------    

im = Image.open("../../files/"+path)
px = im.load()
w, h = im.size
li[0]=1+li[0]
li[1]=1+li[1]
#y0 = 1
#x0 = 1.0000001
if li[1]>li[0]:
	temp=li[1]
	li[1]=li[0]
	li[0]=temp
y0=li[0]
x0=li[1]
vals = []
for i in range(0, h * w):
    x = 1 - 1.4 * pow(x0, 2) + y0
    y = 0.3 * x0
    xr = int(('%.11f' % (x))[4:9]) % w
    yr = int(('%.11f' % (y))[4:9]) % h
    vals.append((xr, yr))
    x0 = float('%.14f' % (x))
    y0 = float('%.14f' % (y))

vals.reverse()
for i in range(0, h * w):
    (xr, yr) = vals[i]
    j = h * w - i - 1
    p = px[j % w, int(j / w)]
    pr = px[xr, yr]
    px[j % w, int(j / w)] = pr
    px[xr, yr] = p

path2=str(input("Save as -- "))
im.save('../../files/'+path2)

#--------------------------------------------------------------------------------------------------------------------------------------------