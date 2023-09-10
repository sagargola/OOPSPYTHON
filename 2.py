'''INSTANCE AND CLASS VARIABLE

This code will show the example of Instance and Class variable from my previous code
Below Increment is set to 1.5 which is a class variable so first when the object is called it will first
check if the instance variable is present which is self.increment which is not present in the below case so it
will go with Employee.Increment but if there was self.increment present inside the  def salary_increment then it
will go with the self.increment variable and ignores the class variable only inside the function

Also, in the last line I have used and comment out print(person_1.__dict__) this method will actually print all the variables in the
instance of person_1 as a dictonary'''

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


#creating the object of class Employee and passing the arguments through it.
person_1 = Employee("Sagar", 32, 2000)
person_2 = Employee("Anne", 40, 5000)

print(f'The Salary of Sagar is {person_1.salary}') # will print 2000
person_1.salary_increment() #increment function is called and will increase the salary of Sagar from 2000 * 1.5
print(f"The incremented salary of Sagar is {person_1.salary}") # will print 3000

#print(person_1.__dict__)