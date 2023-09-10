'''CLASSES, OBJECTS AND CONSTRUCTORS - OOPS CONCEPT 1 ENCAPSULATION

in order to avoid writing the code multiple times we used the concept of class to increase the reusability of our code
person_1 = Employee()
person_2 = Employee()

person_1.name ="Sagar"
person_1.age = 32
person_1.salary = 1000

person_2.name ="Anne"
person_2.age = 40
person_2.salary = 5000
I have kept it simple to explain the different concepts.
__init__ is a constructor which is automatically called when the object of the class is created and it always the argument self
I have also add the data types to the argument in the init function to expect the data type to be entered and
can also add the default value if needed.
I have also used the asset method to validate and check the code simultaneously to check if it throw and error.
I could have also used try and except as exception method here.'''

class Employee:
    def __init__(self,name:str, age:int, salary:int):
        self.name = name
        self.age = age
        self.salary = salary

        #will throw an error is the salary is less then 0 because it cant be negative
        assert salary >= 0 , f"The salary is less then 0 which is {self.salary}"

#creating the object of class Employee and passing the arguments through it.
person_1 = Employee("Sagar", 32, 2000)
person_2 = Employee("Anne", 40, 5000)

#Calling the function using the object. It will print Sagar and salary of Anne which is 5000
print(person_1.name)
print(person_2.salary)
