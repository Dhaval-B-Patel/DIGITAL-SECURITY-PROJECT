
#code to choose base and generate shared prime number
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
a    =    str(input("Enter the password [A] secret key          -- "))
byte_array = a.encode()
binary_int = int.from_bytes(byte_array, "big")
binary_string = bin(binary_int)
binary_string = binary_string[2:]
print(binary_string)
num=int(binary_string,2)
print(len(str(num)))
print(num)