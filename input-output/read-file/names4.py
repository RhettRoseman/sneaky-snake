# we dont really need the 2nd for loop because we can just use the index of the first loop to get the value of the 2nd loop

with open('names.txt') as file:
    # for line sort the file 
    for line in sorted(file):
        #print message with no whitespace and a new line each time
        print(f'hello,' , line.rstrip())

        