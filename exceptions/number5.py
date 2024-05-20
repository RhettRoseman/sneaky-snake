# lets shorten number4.py

def main():
    x = get_int()

def get_int():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("X is not a valid integer")
    
    
main()

# expected output:
# Enter a number: a
# X is not a valid integer


# Enter a number: 4
# Enter a number: 4