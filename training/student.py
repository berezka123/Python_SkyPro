class Student:
    def __init__(self, firstName, secondName, age, course):
        self.firstName = firstName
        self.secondName = secondName
        self.age = age
        self.course = course
    

    def __str__(self):
        return f"{self.firstName} {self.secondName}, {self.age} лет, курс {self.course}"
