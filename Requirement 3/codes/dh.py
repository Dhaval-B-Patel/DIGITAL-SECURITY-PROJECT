
import sqlite3
import random
import os
import datetime
import time
from time import process_time 
import sys
import math
import csv
import timeit
import pickle


print("--------------------------------------------------")
print("||||||||| Diffie-Hellman Key Exchange ||||||||||||")
print("--------------------------------------------------")
print("::::::::::::::::::: operation ::::::::::::::::::::")
print("------------------- Encoding ---------------------")
print("[1] Create the random numbers pool                ")
print("[2] Enter the password secret key [a] or [b]      ")
print("[3] Enter the base and prime number               ")
print("------------------- Decoding ---------------------")
print("[4] Enter the number recieved [A] or [B]          ")
print("")

while True:
	choi=int(input("choice -- "))
	if(choi==1):
		"""
		#code to generate random numbers and choose the number
		"""
		# input the shared key that is to be used it is a prime number 
		sharedKey=int(input("Enter the prime number(shared key) -- "))
		# input how many numbers we want to generate using shared key
		count=int(input("Enter how many numbers to be generated -- "))
		# input how many digit long random number we want to generate using shared key
		power=int(input("enter how many digit random number you need to generate -- "))
		li=[]

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
		choi==3
	

	if(choi==2):
		#code to change the string in to integer 
		a=str(input("ENTER THE SECRET PASSWORD (A):-- "))
		byte_array = a.encode()
		binary_int = int.from_bytes(byte_array, "big")
		binary_string = bin(binary_int)
		binary_string = binary_string[2:]
		num=int(binary_string,2)
		print(num)
		snum=str(num)
		sn=0
		for i in snum:
			sn=sn+int(i)
		print(sn)
		choi=1
		

	if(choi==3):
		#code to choose base and generate shared prime number
		b=int(input("enter the value of base [b] -- "))
		#pt=(input("Enter the prime number(shared key) -- "))
		#sum the digits of prime number and choose sumth prime number from prime number table
		#ptt=int(sum([int(i) for i in str(pt)]))
		#path="../files/"+sys.argv[1]
		#conn = sqlite3.connect(path)
		#conn.row_factory = lambda cursor, row: row[0]
		#cur = conn.cursor()
		#cur.execute("SELECT * FROM prime")
		#rows=cur.fetchall()
		#for i in rows:
		#	p=rows[ptt]
		#print(p)



	if(choi==4):
		AB=int(input("Enter the value of [A] or [B] recieved -- "))








	break



	"""
	#end of code to generate random numbers 
	"""







#return it back to string
#binary_int = int(binary_string, 2)
#byte_number = binary_int.bit_length() + 7 // 8

#binary_array = binary_int.to_bytes(byte_number, "big")
#ascii_text = binary_array.decode()
#print(ascii_text)