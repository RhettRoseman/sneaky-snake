students = [] # we create an empty list called students 

with open("students.csv") as file: # we use a with statement to open the file students.csv
    for line in file: # we iterate over the lines in the file
        name, house = line.rstrip().split(",") # we split the line into two variables name and house
        students.append(f"{name} is in {house}") # we append the name and house to the students list
 


# we print the students list
for student in sorted(students):
    print(student)