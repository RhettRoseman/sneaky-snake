# we create an empty list 
names = []

# we use a with statement to open and close the file 
# we don't need the "r" since it is the default mode

with open("names.txt") as file:
    for line in file:
        # we use the append function to add the line to the names list
        names.append(line.rstrip())


# we print the names list and sort it with the sorted function which alphabitizes the names
for name in sorted(names):
    print(f"hello, {name}")