# we want to create a csv file
# we use a with statement to open a csv file called students.csv
with open("students.csv") as file:
    for line in file:
        # row = split the line into a list of strings
      row = line.rstrip().split(",")
      print(f"{row[0]} is in {row[1]}") # we print the first and second element of the list using the f string syntax