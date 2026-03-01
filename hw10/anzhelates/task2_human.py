class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        return f"Welcome, {self.name}"
    
    @classmethod
    def is_homosapiens(cls):
        return "Homosapiens"
    
    @staticmethod
    def arbitrary_message():
        return f"Person reading this is likely Homosapiens"


name = input("Enter your name: ")

person = Human(name)
print(person.welcome_message())

print(Human.is_homosapiens())

print(Human.arbitrary_message())