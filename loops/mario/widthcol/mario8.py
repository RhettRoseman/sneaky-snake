def main():
    print_square(3)

def print_square(size):
    # # For each brick in row
    for i in range(size):
        print_row(size)
       
# print rows of # by the width of the print square function
def print_row(width):
    print("#" * width)

main()