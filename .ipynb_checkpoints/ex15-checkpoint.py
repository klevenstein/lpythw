# import the argv module
from sys import argv

# tell argv what variables it needs when the script launches
script, filename = argv

# define the txt variable by telling it to open the file defined by filename
txt = open(filename)

# display the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

# prompt user to enter the file again
# print("Type the filename again:")
# file_again = input("> ")
# lets turn that into a single line of code:
file_again = input("Type the filename again: \n> ")

# define a second variable
txt_again = open(file_again)

# display contents of the file
print(txt_again.read())