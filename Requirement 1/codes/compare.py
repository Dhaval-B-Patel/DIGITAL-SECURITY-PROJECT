import os
import sys
import stat
import difflib

while True:
    print("[1] files are compared bit by bit and difference is stored in another file ")
    print("[2] read the files and print if they are identical or not ")
    print("[3] EXIT compare program")
    a=[]
    b=[]
    flag=0
    temp=0
    choice = int(input("provide your choice -- "))
    if(choice == 1):
        path1="../files/"+sys.argv[1]
        path2="../files/"+sys.argv[2]
        path3="../files/"+sys.argv[3]
        fi1=open(path1,"r").readlines()
        fi2=open(path2,"r").readlines()
        fi3=open(path3,"w")
        #print(fi1)
        #print("*********************************************")
        #print(fi2)
        # Find and print the diff:
        for line in difflib.unified_diff(fi1,fi2):
            fi3.write(str(line))
        fi3.close()
        if(os.stat(path3).st_size == 0):
            print("differnce file size 0 KB as there is no difference between them")


    elif(choice == 2):
        ds=input("enter file 1 -- ")
        ds1=input("enter file 2 -- ")
        #ds2=input("save differnce as -- ")
        path1="../files/"+ds
        path2="../files/"+ds1
        #path3="../files/"+ds2
        fi1=open(path1,"r")
        #fi2=open(path2,"r")
        #fi3=open(path3,"w")
        with open(path1,'r') as fi1:
        	for line in fi1:
        		for word in line.split(";"):
        			a.append(word)
        fi1.close()
        fi2=open(path2,"r")
        with open(path2,'r') as fi2:
        	for line1 in fi2:
        		for word1 in line1.split(";"):
        			b.append(word1)
        fi2.close()
        if(len(a)>len(b)):
        	flag=1
        if(len(b)>len(a)):
        	flag=1
        if(len(a)==len(b)):
            temp=len(a)
        for k in range(0,temp):
            if(flag!=1):
                if(a[k]!=b[k]):
                    flag=1
                    break
            if(flag==1):
                break

        if(flag==1):
        	print(ds,end='')
        	print(" is not equal to ",end='')
        	print(ds1)
        if(flag==0):
        	print(ds,end='')
        	print(" is equal to ",end='')
        	print(ds1)

    if(choice == 3):
        print("Exit")
        break
