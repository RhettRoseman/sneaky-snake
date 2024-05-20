def main():
    print_square(5)

# same as in mario6.py except we are condensing the information and dont have the for loop within the for loop

def print_square(size):
    for i in range(size):
        print("#" * size) 

main()