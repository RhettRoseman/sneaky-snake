def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
            return x 
        except ValueError:
            print("X is not a valid integer")
                
main()

