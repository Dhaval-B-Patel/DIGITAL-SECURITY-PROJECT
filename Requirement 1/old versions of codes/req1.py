"""
Requirement 1 of the assignment 2
"""

import random
import time
import sys
import datetime
import sympy
import math

f=open("no1.txt","w")
#st=open("state.txt","w")
f1=open("no2.txt","w")
count=0
#ran=random.seed(8683317618811886495518194401279999999)
#state=random.getstate()
#st.write(str(state))
#st.close()

t1=float(input("input time 1 "))
#endTime = datetime.datetime.now() + datetime.timedelta(minutes=t1)
while True:
    #if datetime.datetime.now() >= endTime:
        #break
    ra=(random.randrange(0,pow(2,15)))
    ra=math.floor(ra)
    tra=str(ra)
    f.write(tra)
    f.write(',')
    count+=1
    if(count==100000):
    	break

f.close()
count=0
t2=float(input("input time 2 "))
ran=random.seed(8683317618811886495518194401279999999)
#random.setstate(state)
#endTime = datetime.datetime.now() + datetime.timedelta(minutes=t2)
while True:
	#if datetime.datetime.now() >= endTime:
		#break
	ra1=(random.randrange(0,pow(2,15)))
	ra1=math.floor(ra1)
	tra1=str(ra1)
	f1.write(tra1)
	f1.write(',')
	count+=1
	if(count==1000000):
		break

f1.close()


