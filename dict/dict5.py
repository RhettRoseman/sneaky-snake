# you may also write the dictionarys like this as well, it takes up less space but is less readable. it is up to what you the programmer prefer
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor","patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None },
    {"name": "Ernie", "house": "Hufflepuff", "patronus": "Boar"}
       
]
# you must make the function to return the values, otherwise it will run an error for this particular code
for student in students:
    print(student["name"], student["house"], student["patronus"], end="\n\n")


# expected output:

    # Hermione Gryffindor Otter

    # Harry Gryffindor Stag

    # Ron Gryffindor Jack Russell Terrier

    # Draco Slytherin None

    # Ernie Hufflepuff Boar