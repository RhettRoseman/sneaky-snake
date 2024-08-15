import random

class Hat:
    # This houses variable can be used in all your functions in the Hat class
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # This method sorts the items in the Hat class based on their names.
    
    @classmethod
    # sort function takes in the class and name
    # cls = class ******
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
# using the Hat class and the sort function to print out the name and house of the student
Hat.sort("Harry")