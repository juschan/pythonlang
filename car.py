class Car():
    """A simple car class"""
    
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Odometer: " + str(self.odometer_reading) + " miles")

    def update_odometer(self, mileage):
        self.odometer_reading=mileage

    def increment_odometer(self, miles):
        self.odometer_reading +=miles

my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())
my_car.read_odometer()

#update attribute directly
my_car.odometer_reading=23

#update attribute using method
my_car.update_odometer(13)

#increment attribute's value through a method
my_car.increment_odometer(33)

#Inheritance
#override parent method by defining the same class 
#For python  2.7, call super using:
#super(ElectricCar, self).__init__(make, model, year)
class ElectricCar(Car):
    """Subclass of car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size=70

    def describe_battery(self):
        print("Battery size is " + str(self.battery_size))

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#instance as attributes - composition
class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size=battery_size
        
    def describe_battery(self):
        print("Battery size is " + str(self.battery_size))

class ElectricCar2(Car):
    """Subclass of car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()

    
my_new_tesla = ElectricCar2('tesla', 'model s2', 2017)
my_new_tesla.battery.describe_battery()
