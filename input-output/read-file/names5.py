# create empty list 
names = []
# we open empty list/ existing list
with open('names.txt') as file:
    # we don't want to sort the file yet, so we just read the file
    for line in (file):
        # we append the line to the names list
        names.append(line.strip())
# we want to reverse the alphabetical order of the names
# we need to use the reverse function
for name in sorted(names, reverse=True):
    print(f"hello, {name}") # we print the names in reverse alphabetical order we use name as a separator