'''CLASS METHODS
So basically this methods is used which has only to do with the class variables and not the object/instance variable.
Now lets take an example Anne is working for the past 20 years now and she wants to increase her salary now we will
use the concept of class method where we dont need to pass self inside the argument instead we will use a
constructor called @classmethod and it will take the cls as an argument I am again using the code from 2.py and explaining
the concept further'''

class Employee:

    increment = 1.5 # this is a class variable and can be accessed by using the class name
    def __init__(self,name:str, age:int, salary:int):
        self.name = name
        self.age = age
        self.salary = salary

        #will throw an error is the salary is less then 0
        assert salary >= 0 , f"The salary is less then 0 which is {self.salary}"

    def salary_increment(self): # function to increase the salary
        self.salary = int(self.salary * Employee.increment) #typecasting it to into to avoid flot number like 3000.0

    @classmethod
    def change_salary(cls, amount): # class method
        cls.increment = amount

#creating the object of class Employee and passing the arguments through it.
person_1 = Employee("Sagar", 32, 2000)
person_2 = Employee("Anne", 40, 5000)

print(person_1.salary) # will Print salary 2000
Employee.change_salary(4) # passing 4 as an amount now cls.increment will be 4
person_1.salary_increment() # now it will use cls.increment as 4 and multiply with current salary so 2000 * 4
print(person_1.salary) #will print incremented salary 8000
