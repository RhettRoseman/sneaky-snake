import csv  # We want to import csv from the standard library to use it in our code

students = []  # We create an empty list called students

with open("students.csv") as file:  # We use a with statement to open the file students.csv
    reader = csv.DictReader(file, delimiter='|', skipinitialspace=True)  # Use DictReader with skipinitialspace
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})  # Append the name and home to the students list

for student in sorted(students, key=lambda student: student["name"]):  # IMPORTANT: lambda = an anonymous function
    print(f"{student['name']} is in {student['home']}")  # Print the name and home of the student
