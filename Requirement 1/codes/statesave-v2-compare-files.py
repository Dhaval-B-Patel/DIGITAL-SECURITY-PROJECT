import os
import sys
import stat
import difflib

path1="../files/"+sys.argv[1]
path2="../files/"+sys.argv[2]
path3="../files/"+sys.argv[3]
fi1=open(path1,"r")
fi2=open(path2,"r")
fi3=open(path3,"w")
print("[1] files are compared bit by bit and difference is stored in another file ")
print("[2] read the files and print if they are identical or not ")
print("[3] EXIT compare program")
a=[]
b=[]
flag=0
temp=0
while True:
    choice = int(input("provide your choice -- "))
    if(choice == 1):
        with open(path1) as fi1:
            f1_text = fi1.read()
        with open(path2) as fi2:
            f2_text = fi2.read()
        # Find and print the diff:
        for line in difflib.unified_diff(f1_text, f2_text, fromfile=sys.argv[1], tofile=sys.argv[2], lineterm=''):
            fi3.write(str(line))
        fi1.close()
        fi2.close()
        fi3.close()

    elif(choice == 2):
        with open(path1,'r') as fi1:
        	for line in fi1:
        		for word in line.split(";"):
        			a.append(word)
       	fi1.close()
        with open(path2,'r') as fi2:
        	for line1 in fi2:
        		for word1 in line.split(";"):
        			b.append(word1)
        fi2.close()
        if(len(a)>len(b)):
        	flag=1
        if(len(b)>len(a)):
        	flag=1
        if(len(a)==len(b)):
            temp=len(a)

        for k in range(0,temp+1):
        	if(a[k]!=b[k]):
        		flag=1
        		break

        if(flag==1):
        	print(sys.argv[1],end='')
        	print(" is not equal to ",end='')
        	print(sys.argv[2])
        if(flag==0):
        	print(sys.argv[1],end='')
        	print(" is equal to ",end='')
        	print(sys.argv[2])

    if(choice == 3):
        print("Exit")
        break
