#class is blueprint for creating instance
#instance variable created each instance


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        print(f"{self.first, self.last}")


emp_1 = Employee('Hari', "S", 90000)
emp_2 = Employee('Raj' ,'S' , 60000)
emp_1.fullname()
