# sys.exit is in a way the error message for the command line arguments.


import sys

try:
    print("hello, my name is" , sys.argv[1])
except IndexError:
    print("too few arguments")
    sys.exit(1)