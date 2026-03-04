class Employee:
    """A class to represent and employee and display info about them"""
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    @classmethod
    def count_employees(cls):
        return cls.employee_count
    
    @classmethod
    def number_of_employees(cls):
        print(f"Total number of employees is {cls.count_employees()}")
    
    def info_about_employee(self):
        print(f"Name: {self.name}, salary: {self.salary}")

e1 = Employee('Anna', 1200)
e2 = Employee('Oleksandr', 2100)

Employee.number_of_employees()
e1.info_about_employee()
e2.info_about_employee()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)