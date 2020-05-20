# Done on 04.05.20

# Lets me use os things
import os

# Asking the user what width and height will be used for the drawn cube
print("Width: ")
a = int(input())
print("Height: ")
b = int(input())

# Asking user what charset to use
print("Width charset: ")
ac = input()
print("Height charset: ")
bc = input()
print("Corner charset: ")
cc = input()
print("Body charset: ")
bc = input()

# Printing Ceiling with a single print using the chosen charsets
# Using a for loop to print the body structure using the chosen charsets
# Printing the Floor with a single print using the chosen charsets
print(cc + ac*a + cc)
for x in range(b):
	print(bc + bc*a + bc)
	print(bc + bc*a + bc)
print(cc + ac*a + cc)

# os method used to pause the cmd console, otherwise since the process has done it's job, it closes itself
os.system("pause")
