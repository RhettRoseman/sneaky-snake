# we set name = to the prompt
name = input("What's your name? ")

# ssave the value with open file function from python 
# programers technique to 'double click' on the file to open it

# we use the open function and pass the argument of names.txt file which will store all our names and the mode of writing to the file with "w"
# if the file does not exist it will be created
# we will assign this function to a variable called file

file = open("names.txt", "w")

# we use the write function on our file object to write our name to the file
file.write(name)
# will close and save the file object
file.close()

#This code only save the last name from user input to the file``