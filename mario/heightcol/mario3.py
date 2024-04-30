def main():
    # print a column of n bricks
    print_column(3)

# ~ note: you can change the internal implementation of the function at any point ~ as long as the function is still the same name ~ it will work wherever you have placed it as long as the contents make sense to the computer ~
def print_column(height):
    for _ in range(height):
    
        print("#\n" * height , end="")

main()

# expected output:
    #
    #
    #
    #
    #
    #
    #
    #
    #