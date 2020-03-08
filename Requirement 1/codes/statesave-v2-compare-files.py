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
while True:
    choice = int(input("provide your choice -- "))
    if(choice == 1):
        with open(path1) as f1:
            f1_text = fi1.read()
        with open(path2) as f2:
            f2_text = fi2.read()
        # Find and print the diff:
        for line in difflib.unified_diff(f1_text, f2_text, fromfile=sys.argv[1], tofile=sys.argv[2], lineterm=''):
            fi3.write(str(line))

    elif(choice == 2):
        with open(path1) as f:
            flat_list1=[word for line in f for word in line.split(';')]
        with open(path2) as f:
            flat_list2=[word for line in f for word in line.split(';')]
        a=flat_list1.sort()
        b=flat_list2.sort()
        if(a==b):
            print("files are equal")
        else:
            print("files are different")
    if(choice == 3):
        print("Exit")
        break
