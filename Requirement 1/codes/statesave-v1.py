import random
import os
import pickle
import time
import sys
import math
# open all the files
st=open("../files/state.txt","w")
# input the shared key that is to be used it is a prime number 
sharedKey=int(input("Enter the prime number(shared key) -- "))
# input how many numbers we want to generate using shared key
count=int(input("Enter how many numbers to be generated -- "))
# input how many digit long random number we want to generate using shared key
power=int(input("enter how many digit random number you need to generate -- "))
li=[]

#store the state in the file
stateTemp=random.getstate()
st.writelines("-----------------------------------------------------\n")
st.writelines("The state before the random numbers are generated \n")
st.writelines("-----------------------------------------------------\n")
st.write(str(stateTemp))
st.close()

if os.path.exists('../files/state.dat'):
    # Restore the previously saved sate
    print('Found state.dat, initializing random module')
    with open('../files/state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # This is called when no state.dat file is found Use a well-known start state
    print('No state.dat found seeding with-- ', end=''  )
    print(sharedKey)
random.seed(sharedKey)

# This code is to produce random values
for i in range(count):
    ra=(random.random())
    no=math.floor(float(ra)*pow(10,power))
    li.append(no)

# This code is to Save state for next time
with open('../files/state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

file=open("../files/RN.txt","w")
for i in li:
    file.writelines(str(i))
    file.write(';')
file.close()

#appending new states to file
st=open("../files/state.txt","a")
stateTemp=random.getstate()
st.writelines("\n-----------------------------------------------------\n")
st.writelines("The state after the random numbers are generated \n")
st.writelines("-----------------------------------------------------\n")
st.write(str(stateTemp))
st.close()