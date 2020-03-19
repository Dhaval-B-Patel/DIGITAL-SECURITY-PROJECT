
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
			nt=str(num)
			for i in range(0, len(nt)):
				res = (res * 10 + int(nt[i])) % count;
			print(nt)
			print("random number from list is ",end='')
			print(li[res])


			
			#---------------------------------------------------------------------------------------------------------------------------------------------
			#calculate a pow b mod m for large b and m
			#fernet little theroam
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

			pat=str(input("Enter the path to store file -- "))
			f=open("../files/"+pat,"w")
			pathfiles=str(sharedkey)+";"+str(sendnumber)+";"+str(count)+";"+str(powe)
			pathfile=str(pathfiles)
			#print(pathfile)
			for k in pathfile:
				f.write(k)
			f.close()
			print(str(sharedkey)+";"+str(sendnumber)+";"+str(count)+";"+str(powe))
			choi=str(input("Enter y to exit "))
			if(choi=='y'):
				print("exit to main menu")
				break

	if(ch==2):
		while True:
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
			
			#---------------------------------------------------------------------------------------------------------------------------------------------

			#calculate a pow b mod m for large b and m
			#fernet little theroam
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

			pat=str(input("Enter the path to store file -- "))
			f=open("../files/"+pat,"w")
			pathfiles=str(sharedkey)+";"+str(sendnumber)+";"+str(count)+";"+str(powe)
			pathfile=str(pathfiles)
			for k in pathfile:
				f.write(k)
			f.close()
			print(str(sharedkey)+";"+str(sendnumber)+";"+str(count)+";"+str(powe))
			choi=str(input("Enter y to exit "))
			if(choi=='y'):
				print("exit to main menu")
				break

	if(ch==3):
		print("Exiting program .it will be destroyed in 5 seconds")
		break








	#---------------------------------------------------------------------------------------------------------------------------------------------

	"""
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
				sn=int(sn)+int(i)
			sn=int(sn)
			print(sn)
			print(li[sn])
					

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
			A= math.pow(b,sn)%int(sharedkey)
			print(A)
			
	  

		if(choi==4):
			AB=int(input("Enter the value of [A] or [B] recieved -- "))
			#get no from choice 2 to compute (A pow a) mod p
			sharedkey=int(sharedkey)
			temp1=math.pow(AB,sn)
			temp2=int(sharedkey)
			sk= temp1%temp2

		if(choi==5):
			#concate string with + and share them
			msgs=str(sk)+str('+')+str(sharedkey)+str('+')+str(power)
			print(msgs)

		if(choi==6):
			#recieved message
			msgrt=input("Enter the message recieved -- ")
			msgr=msgrt.split('+')
			print("shared number -- {}".format(msgr[0]))
			print("prime number -- {}".format(msgr[1]))
			print("no of digits in random generator -- {}".format(msgr[2]))
			power=msgr[2]
			sharedKey=msgr[1]

		if(choi==7):
			break



		
		#end of code to generate random numbers 
		
	"""
	#return it back to string
	#binary_int = int(binary_string, 2)
	#byte_number = binary_int.bit_length() + 7 // 8

	#binary_array = binary_int.to_bytes(byte_number, "big")
	#ascii_text = binary_array.decode()
	#print(ascii_text)