## problem => we want to make sure that if a user puts in a non-integer value then we will be able to keep the program from breaking


## solution => we can use a try/except block to handle the error

try: 
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("X is not a valid integer")

# expected output 

   # input: 4
   # output: x is 4

   # input: 4.5
   # output: X is not a valid integer

   # input: hello
   # output: X is not a valid integer