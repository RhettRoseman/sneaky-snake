# dictionary 
students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"   
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell Terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        # special keyword for no value in python
        "patronus": None
    },
    {
        "name": "Ernie",
        "house": "Hufflepuff",
        "patronus": "Boar"
    }
]
# # this will throw an error
# print(students["name"])

# write out a for loop that prints out the info of each student with their name, house, and/or patronus
# writing like this can be okay, it will do the job but we can make it better
# for student in students:
#     print(student["name"])
#     print(student["house"])
#     print(student["patronus"])

# write out a for loop that prints out the info of each student with their name, house, and/or patronus

# we define student as each single name in the list of students
for student in students:
    # print out the name, house, and patronus of each student --- make a new line after each loop is run
    print(student["name"], student["house"], student["patronus"], end="\n\n")