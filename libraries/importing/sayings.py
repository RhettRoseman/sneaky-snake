# making our own api
# f-strings (formatted string literals) are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.


# we define a main function
def main():
    hello("world")
    goodbye("world")

# we define a function called hello that takes a single argument called name. 
# The function prints a greeting to the console using an f-string. 
# The f-string contains the value of the name argument. 
def hello(name):
    # f-string
    print(f"Hello, {name}!")

# we define a function called goodbye that takes a single argument called name.
def goodbye(name):
    # f-string
    print(f"Goodbye, {name}!")

 # we dont want to call the main function all the time
 # so we call it only when the script is run directly
 # if underscore underscore name underscore underscore is equal to underscore underscore main underscore underscore, then we call the main function
if __name__ == "__main__":
    # calling our main function
    main()

# __name__ is a special variable in Python that is automatically set to the name of the module in which it is used.