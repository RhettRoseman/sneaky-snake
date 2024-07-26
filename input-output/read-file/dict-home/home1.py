import csv # we want to import csv from the standard library to use it in our code

students = [] # we create an empty list called students 

with open("students.csv") as file: # we use a with statement to open the file students.csv
    reader = csv.DictReader(file, delimiter='|', skipinitialspace = True) # reader is a variable that reads the file, since the namesin csv have commas we seperated them with |
    for name, home in reader:
        students.append({"name": name, "home": home}) # we append the name and home to the students list 

for student in sorted(students, key=lambda student: student["name"]): # IMPORTANT:lambda = an anonymous function
    print(f"{student ['name']} is in {student['home']}") # print the name and house of the student


