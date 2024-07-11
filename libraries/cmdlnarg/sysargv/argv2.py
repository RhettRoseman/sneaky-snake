import sys 

# we are going to u se an if elif loop here
# if the length of the user input is less than 2
if len(sys.argv) <  2:
    # using the if statement to print out the error message
    print("too few arguments")
elif len(sys.argv) > 2:
    # using the elif statement to print out the error message
    print("too many arguments")
else:
    # using the else statement to print out the user input
    print("hello, my name is", sys.argv[1])

# example input:
    # python3 argv2.py 
# expected output:
    # too few arguments

# example input:
    # python3 argv2.py bobby daniels
# expected output:
    # too many arguments

# example input:
    # python3 argv2.py bobby
# expected output:
    # hello, my name is bobby    
