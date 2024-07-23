# this code should be the remedy of only getting the last name of user input

# variable called name exceptes the user input 
name = input("What's your name? ")

# we want to make sure that the user input is saved in a txt file so we append with 'a'

# open("filename.txt", 'letter')
file = open("name.txt", 'a')
# use an f string and write the input from name variable in the new file we use \n to create a new line
file.write(f"{name}\n")
# close the file to save the changes
file.close()