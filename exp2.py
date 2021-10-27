# Name: Neeraj Nair
# Roll no.: CEB438
# Aim: Write a program to demonstrate single inheritance in python
#      (with method overloading and overriding)

class Person(object):
    def __init__(self, first, last, age):
        self.firstName = first
        self.lastName = last
        self.age = age
        self.person = "From Person Class"

    def displayDetails(self):
        return '{} {}, {}'.format(self.firstName, self.lastName,
                                                         self.age)
    
class Employee(Person):
    def __init__(self, first, last, age, staffNum):
        super().__init__(first, last, age)
        self.staffNumber = staffNum
        self.employee = "From Employee Class"

    def displayDetails(self):
        return '{} {}, {}, {}'.format(self.firstName, 
                    self.lastName, self.age, self.staffNumber)
    
    def displayEmployeeSalary(self, basic=None, hra=None):
        if hra is None:
            print('Basic:',basic)
        else:
            print("Basic + hra:",basic+hra)

x = Person('Neeraj', 'Nair', 19)
y = Employee('Chandler', 'Bing', 28, "50000")
print(x.person)
print(x.displayDetails())
print('---------------------------')
print(y.employee)
print(y.displayDetails())

y.displayEmployeeSalary(5000)
y.displayEmployeeSalary(5000, 2000)