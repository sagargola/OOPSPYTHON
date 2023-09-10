'''Static Method are used when we dont need to use instance or class as the arguments we will use static when we
need to create simple methods inside the class. I have not used my previous code to explain since this concept
is very basic so I used a quick function to explain it. I have not created class object here instead called
the function directly using class name Employee'''

class Employee:

    @staticmethod
    def is_tuasuniversity_open(day): #this wont ask for cls or self argument since its static
        if day == "sunday" or day == "Sunday" or day == "SUNDAY":
            return True
        else:
            return False

print(Employee.is_tuasuniversity_open("Sunday")) #  calling directly using class name and will return True