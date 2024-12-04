from os.path import exists

from_file = "test.txt"
to_file = "new_test.txt"

# print(f"Copying from {from_file} to {to_file}.")

# we could do these in one line, how?
in_file = open(from_file)
# indata = in_file.read()

print(f"The input file is {len(in_file)} bytes long.")

# print(f"Does the output file exist? {exists(to_file)}")
# print(f"Ready? Hit RETURN to continue, CTRL-C to abort.")
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print("All right, all done.")

from_file.close()
# to_file.close()