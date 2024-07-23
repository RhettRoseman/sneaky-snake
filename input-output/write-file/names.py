

# names is a variable set to an empty list 
names = []
# we make a for loop so that we can get x names from the user in this case 3
for _ in range(3):
    names.append(input("What's your name? ")) # we append the names to the empty list
   
# we sort the list of names in alphabetical order
for name in sorted(names):
    print(f"hello, {name}") # we print the names in alphabetical order we use name as a separator

# we want to save this information to a file look at names1.py for the next steps
