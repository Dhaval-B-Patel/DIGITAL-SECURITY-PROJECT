
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

while True:
	print("Enter 1 to send message   ")
	print("Enter 2 to recieve message")
	print("Enter 3 to Exit program")
	ch=int(input("choice -- "))
	if(ch==1):
		while True:
			print("------------------------------------------------------------")
			print("||||||||||||| Diffie-Hellman Key Exchange ||||||||||||||||||")
			print("------------------------------------------------------------")
			print("::::::::::::::::::::::: encodeing ::::::::::::::::::::::::::")

			sharedkey=int(input("Enter the prime number (shared key)        -- "))
			count=    int(input("How many numbers to generate         -- "))
			powe=    int(input("How many digit random number to generate   -- "))
			a    =    str(input("Enter the password [A] secret key          -- "))
			base =    int(input("Enter the value of base [b]                -- ")) 
			li=[]
			#---------------------------------------------------------------------------------------------------------------------------------------------
			#code to generate random numbers and choose the number

			if os.path.exists('../files/state.dat'):
			    # Restore the previously saved sate
			    print('Found state.dat, initializing random module')
			    with open('../files/state.dat', 'rb') as f:
			        state = pickle.load(f)
			    random.setstate(state)
			else:
			    # This is called when no state.dat file is found Use a well-known start state
			    print('No state.dat found seeding with-- ', end=''  )
			    print(sharedkey)
			    random.seed(sharedkey)

			# This code is to produce random values
			for i in range(count):
			    ra=(random.random())
			    no=math.floor(float(ra)*pow(10,powe))
			    li.append(no)

			# This code is to Save state for next time
			with open('../files/state.dat', 'wb') as f:
			    pickle.dump(random.getstate(), f)

			file=open("../files/RN.txt","w+")
			for i in li:
			    file.writelines(str(i))
			    file.write(';')
			file.close()

			#---------------------------------------------------------------------------------------------------------------------------------------------
			#convet password into number
			byte_array = a.encode()
			binary_int = int.from_bytes(byte_array, "big")
			binary_string = bin(binary_int)
			binary_string = binary_string[2:]
			#print(binary_string)
			#num respresent the integer form of the entered password
			num=int(binary_string,2)
			#val=list(map(int, str(num)))
			res=0
			nt=str(sharedkey)
			for i in range(0, len(nt)):
				res = (res * 10 + int(nt[i])) % count;
			print(nt)
			print("random number from list is ",end='')
			print(li[res])


			
			#---------------------------------------------------------------------------------------------------------------------------------------------
			#calculate a pow b mod m for large b and m
			#implement core logic of deffie-hellman and fernet little theroam implementation
			def power(x, y, p): 
				res = 1;
				#Update x if it is more than or equal to p 
				x = x % p; 
				#If y is odd, multiply x with the result
				while (y > 0): 
					if (y & 1): 
						res = (res * x) % p;
					#y must be even now 
					y = y >> 1; # y = y/2
					x = (x * x) % p; 
				return res;
			mod=str(sharedkey)
			num=str(num)
			a=str(base)
			rem=0
			for i in range(len(num)):
				#Reduce the number b to a small number using Fermat Little 
				rem = ((rem * 10 + ord(num[i]) - 48) % (sharedkey - 1));
			AB=power(base, rem, sharedkey)
			sendnumber=AB

			pat=str(input("Enter the path to store file -- "))
			f=open("../files/"+pat,"w")
			pathfiles=str(sharedkey)+";"+str(sendnumber)+";"+str(count)+";"+str(powe)+";"+str(li[res])
			pathfile=str(pathfiles)
			#print(pathfile)
			for k in pathfile:
				f.write(k)
			f.close()
			print(str(sharedkey)+";"+str(sendnumber)+";"+str(count)+";"+str(powe)+";"+str(li[res]))
			choi=str(input("Enter y to exit "))
			if(choi=='y'):
				print("exit to main menu")
				break

	if(ch==2):
		while True:
			#below 25 lines of code is to fetch the values of prime number from send message 
			print("------------------------------------------------------------")
			print("||||||||||||| Diffie-Hellman Key Exchange ||||||||||||||||||")
			print("------------------------------------------------------------")
			print("::::::::::::::::::::::: Decoding :::::::::::::::::::::::::::")
			pat=str(input("enter location of recieved message -- "))
			f=open("../files/"+pat,"r")
			for line in f:
				ar=line.split(";")
			sharedkey=int(ar[0])
			print(ar[0])
			count=    ar[2]
			powe=    ar[3]
			a    =    str(input("Enter the password [B] secret key          -- "))
			base =    int(ar[1])
			print("prime number mod  ") 
			print(ar[0])
			print("base number b - ") 
			print(ar[1])
			print("no of random numbers count -") 
			print(ar[2])
			print("digit of random number - ") 
			print(ar[3])
			print("The random number the sender has generated is -- ")
			print(ar[4])
			li=[]

			#---------------------------------------------------------------------------------------------------------------------------------------------
			#code to generate random numbers and choose the number

			if os.path.exists('../files/state.dat'):
			    # Restore the previously saved sate
			    print('Found state.dat, initializing random module')
			    with open('../files/state.dat', 'rb') as f:
			        state = pickle.load(f)
			    random.setstate(state)
			else:
			    # This is called when no state.dat file is found Use a well-known start state
			    print('No state.dat found seeding with-- ', end=''  )
			    print(sharedkey)
			    random.seed(sharedkey)

			# This code is to produce random values
			for i in range(int(count)):
			    ra=(random.random())
			    no=math.floor(float(ra)*pow(10,int(powe)))
			    li.append(no)

			# This code is to Save state for next time
			with open('../files/state.dat', 'wb') as f:
			    pickle.dump(random.getstate(), f)

			file=open("../files/RN.txt","w")
			for i in li:
			    file.writelines(str(i))
			    file.write(';')
			file.close()


			#---------------------------------------------------------------------------------------------------------------------------------------------
			#convet password into number
			byte_array = a.encode()
			binary_int = int.from_bytes(byte_array, "big")
			binary_string = bin(binary_int)
			binary_string = binary_string[2:]
			print(binary_string)
			#num is the integer representation of the string value
			num=int(binary_string,2)
			res=0
			nt=str(ar[0])
			for i in range(0, len(nt)):
				res = (res * 10 + int(nt[i])) % int(count)
			print("random number on your side -- ",end='')
			print(li[res])
			print("random number sender has send -- ",end='')
			print(ar[4])
			
			#---------------------------------------------------------------------------------------------------------------------------------------------

			#calculate a pow b mod m for large b and m
			#fernet little theroam implementation i.e implemeting core deffi hellman logic
			def power(x, y, p): 
				res = 1;
				x = x % p; 

				while (y > 0): 
					if (y & 1): 
						res = (res * x) % p; 
					y = y >> 1;
					x = (x * x) % p; 
				return res;
			mod=str(sharedkey)
			num=str(num)
			a=str(base)
			rem=0
			for i in range(len(num)): 
				rem = ((rem * 10 + ord(num[i]) - 48) % (sharedkey - 1));
			AB=power(base, rem, sharedkey)
			sendnumber=AB
			#store the generated values in the file
			pat=str(input("Enter the path to store file -- "))
			f=open("../files/"+pat,"w")
			pathfiles=str(sharedkey)+";"+str(sendnumber)+";"+str(count)+";"+str(powe)+";"+str(li[res])
			pathfile=str(pathfiles)
			for k in pathfile:
				f.write(k)
			f.close()
			print(str(sharedkey)+";"+str(sendnumber)+";"+str(count)+";"+str(powe)+";"+str(li[res]))
			choi=str(input("Enter y to exit "))
			if(choi=='y'):
				print("exit to main menu")
				break

	if(ch==3):
		print("Exiting program . Files will be destroyed in 5 seconds")
		#comment below line if dont want to clear screen after exiting
		os.system("cls")
		#removes the entered msg so that it can only be used once
		#os.remove("../files/"+pat)
		break