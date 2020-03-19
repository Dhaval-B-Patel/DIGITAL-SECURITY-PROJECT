

#Ciphers an image by shuffling its pixels using a Henon Map
#it shows chaotic behavior for 1.4 and 0.3 values which are classical values
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

for i in range(0, h * w):
    li[i]=1+li[i]
    li[i+1]=1+li[i+1]
    if li[i+1]>li[i]:
        temp=li[i+1]
        li[i+1]=li[i]
        li[i]=temp
    y0=li[i]
    x0=li[i+1]
    x = 1 - 1.4 * pow(x0, 2) + y0
    y = 0.3 * x0
    x0 = float('%.14f' % (x))
    y0 = float('%.14f' % (y))
    xr = int(('%.11f' % (x))[4:9]) % w
    yr = int(('%.11f' % (y))[4:9]) % h

    p = px[i % w, int(i / w)]
    pr = px[xr, yr]
    px[i % w, int(i / w)] = pr
    px[xr, yr] = p

path2=str(input("Save as -- "))
im.save('../../files/'+path2, optimize=False, progressive=False, quality=100)

