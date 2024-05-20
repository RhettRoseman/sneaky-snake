## All loops learned so far are present here



# define main function
def main():
    #  define number as get_number function
    number = get_number()
    #print meow (n) times
    meow(number)

# define get_number function using while loop
def get_number():
    # ask user to input a number greater than 0
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
    # return user input number outside of loop but inside function
    return n
# print meow n times using for loop
# function then uses the input from the prompt thrown by get_number function and returns meow n times 
def meow(n):
    for _ in range(n):
        print("meow")

main()

# expected export :
    #Ex: What's n? 3
        # meow
        # meow
        # meow