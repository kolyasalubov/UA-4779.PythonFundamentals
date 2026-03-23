class Human:
    species = "Human"

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return f"Hello {self.name}"

    @classmethod
    def get_species(cls):
        return f"Species is {cls.species}"

    @staticmethod
    def message():
        return "Hello"


tom = Human("Tom")
print(tom.say_hi())
print(tom.get_species())
print(tom.message())
