import random
import os
import pickle
import time
import sys
import datetime
import sympy
import math
# open all the files
st=open("state.txt","w")
# input the shared key that is to be used it is a prime number 
sharedKey=int(input("Enter the prime number(shared key) -- "))
# input how many numbers we want to generate using shared key
count=int(input("Enter how many numbers to be generated -- "))
# input how many digit long random number we want to generate using shared key
power=int(input("enter how many digit random number you need to generate -- "))
li=[]
li1=[]

if os.path.exists('state.dat'):
    # Restore the previously saved sate
    print('Found state.dat, initializing random module')
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # This is called when no state.dat file is found Use a well-known start state
    print('No state.dat, seeding')
random.seed(sharedKey)

# This code is to produce random values
for i in range(count):
    ra=(random.random())
    no=math.floor(float(ra)*pow(10,power))
    li.append(no)

# This code is to Save state for next time
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

# Produce more random values
print('\nAfter saving state:')
for i in range(count):
    ra=(random.random())
    no=math.floor(float(ra)*pow(10,power))
    li1.append(no)


f=open("no1.txt","w")
f1=open("no2.txt","w")
for i in li:
    f.writelines(str(i))
    f.write(';')
for i in li1:
    f1.writelines(str(i))
    f1.write(';')

print(li)
print("-----------------------------------------")
print(li1)
f.close()
f1.close()