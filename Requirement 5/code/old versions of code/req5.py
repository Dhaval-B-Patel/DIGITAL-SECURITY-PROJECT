from PIL import Image
import random
import os
import math
import pickle
import textwrap

path=str(input("Enter image name -- "))
prime=int(input("enter prime number -- "))


#------------------------------------------------------------------------------------------------------------------------------------------------

password=str(input("password -- "))
byte_array = password.encode()
binary_int = int.from_bytes(byte_array, "big")
binary_string = bin(binary_int)
binary_string = binary_string[2:]
num=int(binary_string,2)
print("number key is -- ",end='')
print(num)

#------------------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------------------------------
img = Image.open(path)
size=width,height=img.size
print("width -- ",end='')
print(width)    
print("height -- ",end='')
print(height)

count=width*height
powe=9
#------------------------------------------------------------------------------------------------------------------------------------------------
li=[]
if os.path.exists('../files/state.dat'):
    # Restore the previously saved sate
    print('Found state.dat, initializing random module')
    with open('../files/state-image.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # This is called when no state.dat file is found Use a well-known start state
    print('No state.dat found seeding with-- ', end=''  )
    print(prime)
    random.seed(prime)

# This code is to produce random values
for i in range(count):
    ra=(random.random())
    no=math.floor(float(ra)*pow(10,powe))
    li.append(no)

# This code is to Save state for next time
with open('../files/state-image.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

file=open("../files/RN.txt","w+")
for i in li:
    file.writelines(str(i))
    file.write(';')
file.close()
#------------------------------------------------------------------------------------------------------------------------------------------------
# shuffling algorithm and generating new shuffled image
path2=input("enter shuffle image name -- ")
sf=Image.open(path2)
rl=0
sl=[]
pl=[]
for i in range(0,height-1):
	print("row ",end='')
	print(i)
	for j in range(0,width-1):
		cor=int(i),int(j)
		pv=img.getpixel(cor)
		pl=list(pv)
		#divide random number into 3 equal size strings
		while len(str(li[rl]))!=len("123456789"):
				(li[rl])='0'+str(li[rl])
		if(len(str(li[rl]))!=9):
			sl=textwrap.wrap(str(li[rl]), 3)
			print(sl)
			for q in sl:
				if(len(q)==2):
					q='0'+str(q)
				if(len(q)==1):
					q='00'+str(q)
				if(len(q)==0):
					q='000'
		if(len(str(li[rl]))==9):
			sl=textwrap.wrap(str(li[rl]), 3)
			print(sl)
			for r in sl:
				if(len(r)==2):
					r='0'+str(r)
				if(len(r)==1):
					r='00'+str(r)
				if(len(r)==0):
					r='000'
		if(len(str(li[rl]))>9):
			print("Index greater than 9")
		print("----------------------")	
		#split random number into red blue and green tr tb tg
		plr=int(pl[0])
		plb=int(pl[1])
		plg=int(pl[2])
		#change random number in 3 each for rgb and mod to decrease its value 
		tr=(int(sl[0])%255)
		tb=(int(sl[1])%255)
		tg=(int(sl[2])%255)
		print("------------------")
		print("tr tb tg")
		print(tr)
		print(type(tr))
		print(tb)
		print(type(tb))
		print(tg)
		print(type(tg))
		print("-------------------")
		#doing XOR of the pixel and random 
		npxr=int((plr^tr)%255)
		npxb=int((plb^tb)%255)
		npxg=int((plg^tg)%255)
		print("------------------")
		print("npxr npxb npxg")
		print(npxr)
		print(type(npxr))
		print(npxb)
		print(type(npxb))
		print(npxg)
		print(type(npxg))
		print("-------------------")
		#modifying the value of pixels
		print(i,end='')
		print(" ")
		print(j)
		sf.putpixel((int(i),int(j)),(npxr,npxb,npxg))
		#taking next random number
		rl=rl+1
		
#------------------------------------------------------------------------------------------------------------------------------------------------
