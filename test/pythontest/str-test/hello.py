# main function
def main():
    name = input("What's your name? ")
    # call hello function with user's name as argument
    print(hello(name))

# define hello function
# to = "world" will default to "world" if no argument is provided
def hello(to="world"):
    # return a greeting message with user's name in it
    return f"hello, {to}"

if __name__ == "__main__":
    # call the main function
    main()