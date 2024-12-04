import sys
script, input_encoding, error = sys.argv

# defining the main function
def main(language_file, encoding, errors):
    # define the variable line
    line = language_file.readline()

    if line:
        # use the print_line function
        print_line(line, encoding, errors)
        return main (language_file, encoding, errors)

# define the print_line function
def print_line(line, encoding, errors):
    next_lang = line.strip()
    # encode applies a specific encoding to a string
    raw_bytes = next_mang.encode(encoding, errors=errors)
    # decode works opposite to the encode
    cooked_string = raw_byes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

