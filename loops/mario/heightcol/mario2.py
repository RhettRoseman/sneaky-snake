# building out multiple functions
# def main function --  we are using a function here call print_column
def main():
    print_column(3)

#define print_column function -- we are using this function to print a column of bricks - for variable in the range of height
def print_column(height):
     for _ in range(height):
        print("#")

# at the end of the program we call the main function ~ note: this will  complete the program
main()

# expected output:
    #
    #
    #
# note: output will be 1 column of hashtags 