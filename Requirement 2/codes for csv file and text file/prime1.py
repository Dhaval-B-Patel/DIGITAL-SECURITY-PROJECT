"""
Requirement 2 of the assignment 2
Generate prime numbers and store the content in the file
default approach of trial divisor approach
"""
import datetime
import os
import time
from time import process_time 
import sys
import math
import csv
import timeit

path="../files/"+sys.argv[1]
f1=open(path,"w", newline='')
fields = ['prime','start_time','stop_time','time_elasp','time_total']
csvwriter = csv.writer(f1)
csvwriter.writerow(fields)
print("----------------------------")
print("|  prime number generator  | ")
print("----------------------------")
t=float(input("Enter max time to discover a single prime[minutes] -- "))
#convert minutes to seconds
ti=t*60
counter = 3
num=0
flag=0
t_total=0
while True:
	# start the clock
	t_start=timeit.default_timer()
	for i in range(1,counter):
		if(counter%i==0 and i!=1 and i!=counter):
			flag=1
	# stop the clock 
	t_stop=timeit.default_timer()

	# calculate the time elasped
	t_elasp=t_stop-t_start
	#total time to generate random numbers
	t_total=t_total + t_elasp
	# counter is incremented twice intentionally as every other is a even so divisible by 2
	if(flag != 1):
		#write data into file if number is prime
		row = [counter,t_start,t_stop,t_elasp,t_total]
		csvwriter.writerow(row)
		flag=0
	counter = counter + 1
	if(t_total>=ti):
		break


"""
generate prime in range using sympy library
while True:
	prime = sympy.randprime(0,pow(10,10))
	f2.write(str(prime))
	f2.write(',')
f2.close()
"""
