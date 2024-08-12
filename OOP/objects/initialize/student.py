# OOP
class Student:
    
    # __init__ intialize an otherwise empty object 
    def __init__(self, name, house):
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
    student = Student(name, house) # <----- constructor call constructs the Student object
    return student # <----- return the student variable that is the Student object

if __name__ == "__main__":
    main()
    
# expected input:
# Name: Harry
# House: Gryffindor
# expected output:  
# Harry from Gryffindor