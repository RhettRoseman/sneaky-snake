def main():
    x = get_int("What's x?: ")
    print(f"x is {x}")

def get_int(prompt):
    # while True: print x is {user input} and return the value and leave the loop
    # except ValueError pass the error and ask the question again
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            pass


main()

