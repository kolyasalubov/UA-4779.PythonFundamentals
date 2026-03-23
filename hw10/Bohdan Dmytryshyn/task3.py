class Employee:
    """
    Class for Employees
    """
    employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # self.add_employee()
        Employee.employees += 1

    def employee_info(self):
        print(f"Employee {self.name}, salary {self.salary}")

    @classmethod
    def get_employees_count(cls):
        print(f"Total employee count: {cls.employees}")

    @classmethod
    def add_employee(cls):
        cls.employees += 1

    @classmethod
    def class_info(cls):
        print(cls.__base__)
        print(cls.__dict__)
        print(cls.__name__)
        print(cls.__module__)
        print(cls.__doc__)

    @staticmethod
    def class_info2():
        print(Employee.__base__)
        print(Employee.__dict__)
        print(Employee.__name__)
        print(Employee.__module__)
        print(Employee.__doc__)


tom = Employee("Tom", 1234)
tom.employee_info()
john = Employee("John", 4321)
john.employee_info()

tom.get_employees_count()

tom.class_info()
john.class_info2()
