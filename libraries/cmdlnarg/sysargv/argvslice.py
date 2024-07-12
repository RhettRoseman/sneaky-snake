# we want to print out multiple name tags in this example

# we impot sys
import sys

# then we will do an if statement using sys.argv 
# we will use sys.exit to print out the error message 
if len(sys.argv) < 2:
    sys.exit("too few arguments")


# here we are looping over the arguments and printing each one out

# for argument in user input slice  the list to subsets of the list (explanation of slice below)
for arg in sys.argv[1:]:
    # print out the name tag of each name
    print("hello, my name is", arg)

# this will print out the name tags of the user input 

# SLICE DEFINITION: subset of a data structure like a list

# example input:
# python3 argvslice.py 
# expected output:
# too few arguments

# example input: 
# python3 argvslice.py bobby david 
# expected output:
# hello, my name is bobby
# hello, my name is david