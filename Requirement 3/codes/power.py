# Python3 program to find 
# (a^b)%m for b very large. 

# Function to find power 
def power(x, y, p): 
	res = 1; # Initialize result 

	# Update x if it is 
	# more than or equal to p 
	x = x % p; 

	while (y > 0): 
		
		# If y is odd, multiply 
		# x with the result 
		if (y & 1): 
			res = (res * x) % p; 

		# y must be even now 
		y = y >> 1; # y = y/2 
		x = (x * x) % p; 
		
	return res; 

# Driver Code 
a = 2; 

# String input as b 
# is very large 
b = "19937"; 

remainderB = 0; 
MOD = 3; 

# Reduce the number B 
# to a small number 
# using Fermat Little 
for i in range(len(b)): 
	remainderB = ((remainderB * 10 +
				ord(b[i]) - 48) %
				(MOD - 1)); 

print(power(a, remainderB, MOD)); 

