# we define the main function
def main():
    # prompt the user for a number, use square function to calculate the square of the number, and print the result
    x = int(input("What's x? "))
    # call the square function with x as the argument and print the result of the square operation
    print("x squared is", square(x))
# we define the square function below
def square(n):
    # return the square of the number by multiplying n by itself
    return n * n
# run the program if terms are met
if __name__ == "__main__":
    main()
