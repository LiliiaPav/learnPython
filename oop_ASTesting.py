class Student:
    def __init__(self, name):
        self.name=name
        self.grades = (90, 90, 93, 78, 90)
    def average(self):
        return sum(self.grades)/len(self.grades)


student = Student("Bob")

print(student.name)
print(student.average())