#Capitalised names belongs to classes
#Methods: functions that are part of classes
#In python 2.7, create class using class Dog(Object):
class Dog():
    """A simple dog class"""
    
    #must always have self as first parameter, auto passed when called
    def __init__(self, name, age):
        """Initialise name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """simulate dog sitting"""
        print(self.name + " is sitting.")
    
    def roll_over(self):
        """simulate dog rolling over"""
        print(self.name + " is rolling over.")

#create dog instance
my_dog=Dog('Willie', 5)
print("My Dog's name is " + my_dog.name)
my_dog.sit()
my_dog.roll_over()

