"""
Requirement 2 of the assignment 2
Generate prime numbers and store the content 
My approach a smart algorithm to calculate the number fast
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
fields = ['prime','start_time','stop_time','time_elasp','total_time']
csvwriter = csv.writer(f1)
csvwriter.writerow(fields)
print("----------------------------")
print("|  prime number generator  | ")
print("----------------------------")
t=float(input("Enter max time to discover prime [minutes] -- "))
#convert minutes to seconds
ti= t*60
counter = 1
num=0
t_total=0
while True:
	# start the clock
	t_start=timeit.default_timer() # start time with precision of nano second
	flag=0
	#code to find if number is prime or not
	if(counter%5==0):
		flag=1
	if(flag!=1):
		temp = math.floor(math.sqrt(counter)) 
		for i in range(2, 1 + temp):
			if(counter % i == 0):
				flag=1
				break
	# stop the clock 
	t_stop=timeit.default_timer() #stop time with precision of nanao second
	# calculate the time elasped
	t_elasp=t_stop-t_start
	t_total=t_total + t_elasp
	if(flag != 1):
		#write data into file if number is prime { }
		row = [counter,t_start,t_stop,t_elasp,t_total]
		csvwriter.writerow(row)
		flag=0

	# counter is incremented twice intentionally as every other is a even so divisible by 2
	counter = counter + 2
	#break if the total time reaches the input time of max time
	if(t_total>=ti):
		break


"""
while True:
	prime = sympy.randprime(0,pow(10,10))
	f2.write(str(prime))
	f2.write(',')
f2.close()
"""
