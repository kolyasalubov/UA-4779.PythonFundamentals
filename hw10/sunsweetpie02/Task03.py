####################################################################################
# hw10.03

class Employee:
    """This is Employee class"""
    
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee(self):
        print("Name:", self.name, "| Salary:", self.salary)

    @classmethod
    def total_employees(cls):
        print("Total employees:", cls.employee_count)


emp1 = Employee("John", 5000)
emp2 = Employee("Anna", 6000)

emp1.display_employee()
emp2.display_employee()

Employee.total_employees()

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

##############################################################################