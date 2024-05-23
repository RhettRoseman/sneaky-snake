def main():
    x = get_int("What's x?: ")
    print(f"x is {x}")

def get_int(prompt):
    # while True: print x is {user input} and return the value and leave the loop
    # except ValueError pass the error and ask the question again
    while True:
        try:
            # if user input is an integer then loop will end and return the value
            # if the input is not an integer then the loop will go to the ValueError
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            # This passes the errors messages from python and then the loop restarts
            pass


main()

