import sys

# we are saying to the computer we want to import the sayings.py file and import the goodbye function
from sayings import goodbye


# if the user entered a name as a command line argument, we will call the goodbye function with that name
if len(sys.argv) == 2:
    goodbye(sys.argv[1])


# example input: python3 hello.py world
# example output: Goodbye, world!