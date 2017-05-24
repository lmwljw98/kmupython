class Employee:
    def __init__(self,name,age,gender,salary,hiredate):
        Person.__init__(self,name,age,gender)
        self.salary = salary
        self.hiredate = hiredate

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

a = Employee("name","age","gender","salary","hiredate")
print(a.name, a.age, a.gender, a.salary, a.hiredate)
