class Student:
    
    # __init__ intialize an otherwise empty object  (arguments to pass through to constructor)
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name cannot be empty")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: # list of valid houses, if the user does not enter one of these four houses, errors will be raised
        #     raise ValueError("Invalid House")
        self.name = name
        self.house = house
        
    # __str__ method returns a string representation of the object
    def __str__(self):
        return f"{self.name} from {self.house}"        
    # Getter - gets an attribute
    @property
    def house(self):
        return self._house
    
    # Setter- sets an atribute 
    @house.setter
    def house(self, house):
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: # list of valid houses, if the user does not enter one of these four houses, errors will be raised
            raise ValueError("Invalid House")
           
         self._house = house # using underscore so computer knows difference between fucntion and property
        
# main function prints out the name and house of the student.   
def main():
    student = get_student()
    print(student)
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