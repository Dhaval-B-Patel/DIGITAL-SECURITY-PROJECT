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
with open(path1) as f1:
    f1_text = fi1.read()
with open(path2) as f2:
	f2_text = fi2.read()
        # Find and print the diff:
for line in difflib.unified_diff(f1_text, f2_text, fromfile=sys.argv[1], tofile=sys.argv[2], lineterm=''):
	fi3.write(str(line))
for line in difflib.unified_diff(f1_text, f2_text, fromfile=sys.argv[1], tofile=sys.argv[2], lineterm=''):
	fi3.write(str(line))