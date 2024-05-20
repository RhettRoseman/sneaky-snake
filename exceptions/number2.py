# except in python is used to catch and handle exceptions aka error handling 
# Name Error handling 
# Name Errors occur when you try to use a variable that has not been defined.
# problem with this is that the variable is not defined 

# try to find an integer variable from user 
try:
    x = int(input("Enter a number: "))  
# if the variable is not an integer then print message
except ValueError:
    print("X is not a valid integer")
# if the variable is an integer then print message 
# {x} is the variable from user
else:
    print(f"x is {x}")
