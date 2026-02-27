class Employee:
    """Represents an employee 
    with name and salary."""
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.count()

    @classmethod
    def count(cls):
        cls.counter += 1
    @classmethod
    def total(cls):
        print(f'Total number of employee: {cls.counter}')
    
    def info(self):
        print(f'Name: {self.name}, salary: {self.salary}')





c = Employee('Vitalii', 10000)


b = Employee('Vadym', 3000)


d = Employee('Andrii', 5000)

b.total()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)