#function example. Default parameter value
#parameter is username
def greet_user(username, greeting="Hello"):
    print(greeting + " " + username)

#argument is Justin (ie. actual value passed to function)
greet_user("Justin")

#named arguments
greet_user(username="Jane", greeting="Hi")

#optional argument. Last parameter with empty default
def greet_user(username, greeting, misc=''):
    print(greeting +  " " + username + " " + misc)

#function with return value
def add(first, second):
    return first+second
    
#when passing list as argument into function, passed as reference and can be modified
#if you do not wish to modify, pass list as listname[:] to create a copy

#variadic arguments, must always come at the end
def make_pizza(*toppings):
    print(toppings)
    
make_pizza("mushroom")
make_pizza("mushroom", "cheese")

#arbitrary keyword arguments
#accepts as many key-value pairs as possible
def build_profile(first, last, **user_info):
    print(first)


#modules
#create a file, pizza.py, with function make_pizza()
#in a new file, import pizza.
#use the function via: pizza.make_pizza()
#or import specific functions: from pizza import make_pizza, create_pizza
#or create alias: from pizza import make_pizza as makepz
#or create alis for module: import pizza as p
#or import all functions: from pizza import *


    
