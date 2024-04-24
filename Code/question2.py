class Student:
    passingMark = 50
    def __init__(self, name, mark) -> None:
        self.name = name
        self.mark = mark
    def __str__(self) -> str:
        return f"Name: {self.name}, Mark: {self.mark}"
    def passOrFail(self) -> str:
        if self.mark >= self.passingMark:
            return "Pass"
        else:
            return "Fail"


# Executing code is in main.py