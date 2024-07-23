# with statement is used to open a file and automatically close it when the block of code is done executing
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
