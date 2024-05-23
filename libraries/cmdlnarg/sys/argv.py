# we are going to use the command line arguments to run this code 
#sys.argv arg v is a fancy way of saying all of the words the ...
#... human typed in at the prompt before they hit enter


import sys 
# sys.argv is going to comb the command line arguments for a list of commands
print(" hello, my name is", sys.argv[1])

# note: there is no error handling here, so if you don't enter a name, you will get an error: line 8, in <module>  print(" hello, my name is", sys.argv[1])  ~~~~~~~~^^^ IndexError: list index out of range
# for error handling, see argv1.py
# exampe input:
# python3 argv.py Jackie Chan 
# expected output:
# hello, my name is Jackie Chan

# exampe input:
# python3 argv.py Bruce Le
# expected output:
# hello, my name is Bruce Lee
