import sys
# here we are going to try to print hello, my name is <user input> "
try: 
    print("hello, my name is", sys.argv[1])
# we are handling the error if the user does not enter a name specifically the IndexError 
except IndexError:
    print("please enter a name")

# example input: 
    # python3 argv1.py Jackie Chan
# expected output:
    # hello, my name is Jackie

# example input: 
    # python3 argv1.py 
# expected output:
    # please enter a name

# example input: 
    # python3 argv1.py Jackie
# expected output:
    # hello, my name is Jackie