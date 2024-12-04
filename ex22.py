import sys
# the usual command line argument handling
script, input_encoding, error = sys.argv

# defining the main function which is called at the end of the script
def main(language_file, encoding, errors):
    # read a single line from the input file
    line = language_file.readline()

    # ooh it's an if statement
    # if the line has content, it calls print_line
    # otherwise it does not run print_line or return main
    if line:
        # use the print_line function
        print_line(line, encoding, errors)
        return main (language_file, encoding, errors)
        # calling main inside main jumps back to the top of the script
        # the if statement keeps the loop from becoming infinite

# define the print_line function
def print_line(line, encoding, errors):
    # strip the trailing \n
    next_lang = line.strip()
    # encode the line into raw bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # decode works opposite to the encode
    # decode the bytes to get the encoded string
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # print the results to see what they look like
    print(raw_bytes, "<===>", cooked_string)

# opens the languages file
languages = open("languages.txt", encoding="utf-8")

# runs the main function with the correct params
main(languages, input_encoding, error)

