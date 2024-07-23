# we want to read the file names.txt
# we use the with function to get the file and read it

with open("names.txt", "r") as file:
    # we make a variable called lines and use readlines to read the file
    # each line in the file is a new element in the lines list
    lines = file.readlines()
    #line in this for loop is the new list lines is a new element in the line list
    for line in lines:
        print("hello,", line.rstrip()) # we strip any whitespace from the line and print it


# expected input: python3 names3.py 
# expected output: 
# hello, Harry
# hello, Hermionie
# hello, Draco
# hello, Ron