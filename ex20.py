from sys import argv

script, filename = argv

input_file = open(filename)

# function that prints the entire file
def print_all(f):
    print(f.read())

# function that sets the reference point the the beginning
def rewind(f):
    f.seek(0)

# function that prints a line one at a time, with numbers
def print_a_line(line_count, f):
    print(line_count, f.readline())

# the readline method returns a single line from the file

current_file = open(filename)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

# calls the function again
# updates current_line to the result from the previous call

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# += is the same thing as self + 1