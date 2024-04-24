class Person:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
    def get_info (self) -> None:
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, fname, lname, age, student_id) -> None:
        super().__init__(fname, lname, age)
        self.student_id = student_id
    def get_stuinfo(self) -> None:
        self.get_info()
        print("Student ID:", self.student_id)


class Employee(Person):
    def __init__(self, fname, lname, age, employee_no, salary) -> None:
        super().__init__(fname, lname, age)
        self.employee_no = employee_no
        self.salary = salary
    def get_empinfo(self) -> None:
        self.get_info()
        print("Employee No:", self.employee_no)
        print("Salary:", self.salary)


# Executing code is in main.py