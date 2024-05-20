# this is my personal favorite way to write this solution
# easy to read and works the best i can see so far



def main():
    x = get_int()


def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            break 
        else:
            print(f"x is {x}")
            break
main()