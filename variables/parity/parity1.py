
#Even or odd 2

# define main (i.e. function)
def main():
    x = int(input("What's x?"))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Boolean values
def is_even(n):
    if n % 2 == 0:
        return True if n % 2 == 0 else False
    
main()
