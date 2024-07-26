# we want to create a csv file
# we use a with statement to open a csv file called students.csv
with open("students.csv") as file:
    for line in file:
        # we can use multiple variables for one statement
      name, house = line.rstrip().split(",")
      print(f"{name} is in {house}") # this shows us in a better way what we are trying to achieve