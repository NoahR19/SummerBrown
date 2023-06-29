# Name of student - Student age, Classes student is taking, Grade, GPA, learn(), doHW(), Walktoclass()
# Grades of student - Number grade, Letter grade, averageclassgrade()
# Classes possible to take - Person teaching each class, # of people in each class, liststudents(), changeteacher()

class student:
    def __init__(self, name, grade, gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa

    def myfunc(self):
        print('My name is ' + self.name + ', I am in grade ' + str(self.grade) + ', and I have a GPA of ' + str(self.gpa))

person1 = student('Noah', 11, 3.5)

if __name__ == '__main__':
    person1.myfunc()

class grades:
    def __init__(self, letter, number):
        self.number = number
        self.letter = letter

    def myfunc(self):
        print('My letter grade is ' + str(self.letter) + ' and my number grade is ' + str(self.number) + '%')

person1 = grades('A+', 97)

if __name__ == '__main__':
    person1.myfunc()