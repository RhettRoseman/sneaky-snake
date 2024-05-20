def main():
    x = get_int()

def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("X is not a valid integer")
        else:
            print(f"x is {x}")
            break
    return x 

main()