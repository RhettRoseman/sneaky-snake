# add a while loop to the code in number2.py
# the while loop should keep asking the user for an integer value until the user enters a valid integer value
#  if the user entered a non-integer value, the program should print an error message and ask the question again
# if the user entered a valid integer value, the program should print the value and exit the loop
while True: 
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("X is not a valid integer")
    else:
        print(f"x is {x}")
        # break out of loop
        break
