#Even or odd 
def main():
    x = int(input("What's x?"))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()

# note 
# Pythonic = the act of doing anything in python
# % = divide 