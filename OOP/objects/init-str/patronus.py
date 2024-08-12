# constuctor class
class Student:
    
    # __init__ intialize an otherwise empty object  (arguments to pass through to constructor)
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Name cannot be empty")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: # list of valid houses, if the user does not enter one of these four houses, errors will be raised
            raise ValueError("Invalid House")
        # adding a new attribute to the student object.  This is a way to store information about the student that is not part of the student's basic properties (name, house) but is related to the student's life.  In this case, the patronus.  We can add more attributes as needed.  For example, we could add attributes for student's favorite books, favorite food, or favorite color.
        self.name = name
        self.house = house
        self.patronus = patronus  
        
    # __str__ method returns a string representation of the object
    def __str__(self):
        return f"{self.name} from {self.house}"        
    
    # we want to make srue that harry and the other students from Hogwarts have the right patronus charms
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell":
                return "🐶"
            case _:
                return "🪄"
# main function prints out the name and house of the student.   
def main():
    student = get_student()
    print("Expecto Patronum! ", student.charm())
# get student function prints out the name and house of the student
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) # <----- return the student variable that is the Student object ---- constructor call constructs the Student object

if __name__ == "__main__":
    main()
    
# expected input:
# Name: Harry
# House: Gryffindor
# expected output:  
# Harry from Gryffindor