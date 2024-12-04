# importing the argument variable module
from sys import argv
# read the wyss section for how to run this
script, first, second, third = argv
# in english: take what is assigned in argv
# unpack it
# assign it to the listed variables in order

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

variable = input("Should I repeat the first, second, or third variable? > ")
print(variable)