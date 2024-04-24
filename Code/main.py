from question1 import Person, Student, Employee
import question2
import question3
import question4

# QUESTION 1:
print("\n QUESTION 1: \n")
new_student = Student("Anthony", "Smith", 35, "s346571")
new_student.get_stuinfo()
print("======================================")
new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
new_employee.get_empinfo()




# QUESTION 2:
print("\n QUESTION 2: \n")

student1 = question2.Student("John", 52)
status1 = student1.passOrFail()
print(status1)

student2 = question2.Student("Jenny", 69)
status2 = student2.passOrFail()
print(status2)


question2.Student.passingMark = 60
status1 = student1.passOrFail()
print (status1)

status2 = student2.passOrFail()
print(status2)

# QUESTION 3:
print("\n QUESTION 3: \n")

message1 = question3.Message("student@kristiania.no", "hadi@oslomet.no")
print(message1.get_sender())
print(message1.get_recipient())
message1.append("Hello Hadi")
message1.append("This is a nice exam!")
message1.append("Hope you are enjoying the spring with nice weather")
message1.append("BR, Student @ Kristiania")
print(message1.toString())


# QUESTION 4:
print("\n QUESTION 4: \n")

before_substitution = question4.generate_numbers()
after_substitution = question4.substitute(before_substitution)
print(f"Before substitution: {before_substitution}")
print(f"After substition: {after_substitution}")