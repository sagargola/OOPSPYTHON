'''INHERITANCE
Now I am just creating another class called programmer which will inherit the properties of our class Employee
so will resuse my 3.py code again. Also will write a override methods which is Programmer'''


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

class Programmer(Employee): #Inheritance where the class Programmer inheritted all the properties of Employee
    def __init__(self,name,age,salary,proglang,exp):
        super().__init__(name,age,salary)
        self.prolang = proglang
        self.exp = exp

    def salary_increment(self):  #overide method as the programmer salary is much higher
        self.salary = int(self.salary * (Employee.increment *2))

person_1 = Programmer("John",23,8000,"python",5)
print(person_1.prolang) # will print python as a programming lanugae


#creating the object of class Employee and passing the arguments through it.
#person_1 = Employee("Sagar", 32, 2000)
#person_2 = Employee("Anne", 40, 5000)