# dictionary 
students = {
    "Herimone": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin",
    "Ernie": "Hufflepuff"
}
# starts for loop search for dictionary keys
# can use this type of for loop to search for keys and values in a dictionary
for student in students:
    # tell me the student name, then the house they are in, seperate(sep) with a comma and a space 
    print(student, students[student], sep= ", ")

    # expected output:

    # Herimone,Griffindor
    # Harry,Griffindor
    # Ron,Griffindor
    # Draco,Slytherin
    # Ernie,Hufflepuff