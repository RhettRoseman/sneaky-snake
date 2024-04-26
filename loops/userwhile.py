# user input prompts using while loop
# we are trying to complete the goal of creating a loop where the user inputs a number and the program will keep asking for a number until the user inputs a number greater than 0


# This will be succesful 
while True:
    n = int(input("What's n?"))
    # test to show what not to do here 
    if n < 0:
        continue
    else: 
        break

# asks a question no export 