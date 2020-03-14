from PIL import Image
import random

x = 150;
y = 150;
value = 1;
j = 0;
im = Image.open('test.jpg') # Can be many different formats.
pix = im.load()
vav = pix[x,y] #RGP values
list = [0,0,0,0]
newVav = (0,0,0,0)
print (im.size)  # Get the width and hight of the image for iterating over
#print (vav)
#print (vav[0])
#print (vav[1])
#print (vav[2])
#print (vav[3])
for i in vav: # to take the RGP values and add them to a list
	list[j] = i
	j +=1

print (list)
random.shuffle(list) # shuffle a values ( must be a list )
print (list)

#for i in list: # changing the list values to tuples
#	newVav[j] = i
#	j +=1
#print (newVav)  

#pix[x,y] = newVav # Set the RGBA Value of the image (tuple)
#im.save('alive_parrot.png')  # Save the modified pixels as .png

