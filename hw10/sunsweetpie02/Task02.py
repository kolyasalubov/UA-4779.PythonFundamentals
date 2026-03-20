#####################################################################################
# hw10.02

class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name}! Welcome!")

    @classmethod
    def get_species(cls):
        return f"This species is {cls.species}"

    @staticmethod
    def random_message():
        return "Have a great day!"


person = Human("Liubov")
person.welcome()

print(Human.get_species())
print(Human.random_message())

####################################################################################