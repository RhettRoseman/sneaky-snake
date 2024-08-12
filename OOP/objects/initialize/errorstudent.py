# WARNING: THIS SHOWS WHAT NOT TO DO IN OOP DO NOT TRY TO USE THIS IT WILL BREAK AS INTENDED FOR EDUCATIONAL PURPOSES ONLY SOLUTION --------- IN OOP/objects/init-str/student.py --

class Student:
 # __init__ intialize an otherwise empty object ()
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name cannot be empty")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: # list of valid houses, if the user does not enter one of these four houses, errors will be raised
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
# main function prints out the name and house of the student.   
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
# get student function prints out the name and house of the student
def get_student():
    name = input("Name: ")
    house = input("House: ")
    #constructor call constructs the Student object
    student = Student(name, house) 
    #return the student variable that is the Student object
    return student 

if __name__ == "__main__":
    main()
    
# expected input:
# Name: Harry
# House: Gryffindor
# expected output:  
# <__main__.Student object at 0x7f8b1c7b3d30>  <---the memory address of the object is printed out instead of the Harry from Hogwarts 


# WARNING: THIS SHOWS WHAT NOT TO DO IN OOP DO NOT TRY TO USE THIS IT WILL BREAK AS INTENDED FOR EDUCATIONAL PURPOSES ONLY ------- SOLUTION IN OOP/objects/init-str/student.py --