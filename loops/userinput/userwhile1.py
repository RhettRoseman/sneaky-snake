## Tightened up user input code 

# user input must be greater than 0 or loop will keep running 
while True:
    # n = user input
    n = int(input("What's n?"))
    # if n is greater than 0 then break the loop
    if n > 0:
        break
# when loop is broken with a positive value then print meow n times ---
# n = user input
for _ in range(n):
    print("meow")

# expected export :
    # meow as many times as user input
# note --- user input must be greater than 0 or loop will keep running
#example : user input 3 
    # expected export : 
        # meow
        # meow
        # meow