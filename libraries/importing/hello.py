
# we import sys
import sys
# we import functions from sayings.py
from sayings import hello

# we get the user's name from the command line arguments
if len(sys.argv) == 2:
    hello(sys.argv[1])

