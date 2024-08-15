

# NOT A REAL WORLD EXAMPLE THAT SHOULD BE USED AS A COPY PASTE TO YOUR CODE IT WILL NOT DO ANYTHING USEFUL

import random

class Hat:
    # This method initializes the Hat class with a list of houses; insures that every instance of the Hat class has a the list of house names
    def __init__(self):
        # List of houses at Hogwarts
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    # This method sorts the items in the Hat class based on their names.
    def sort(self, name):
        # random.choice() method returns a random element from the non-empty sequence
        # 
        print(name, "is in", random.choice(self.houses) )
    
# hat variable = Hat Class instance    
hat = Hat()
hat.sort("Harry") # == name 

# Note: This will only print out Harry is in Gryffindor, Harry is in Hufflepuff, Harry is in Ravenclaw, or Harry is in Slytherin nothing else this is a method that should not be used unless you need 1 character/person/object etc to have a list of hats or houses.  This is a method that is not used in the real world.