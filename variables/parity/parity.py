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
# % = divdie in this case but saying if the remainder is 0 then n is even 
# if the remainder is not 0 then n is odd so you return False 
 