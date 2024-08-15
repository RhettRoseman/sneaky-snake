class Wizard:
    def __init__(self, name, house):
        self._name = name
        self._house = house

class Student(Wizard):
    def __init__(self, name, house):
        super.__init__(name)
        self.house = house
        
class Professor:
    def __init__(self, name, subject):
        self.subject = subject
        
        
