#---------------------------------

# Dog: object
# Methods: actions (eat,sleep,bark)
# State: attributes(color,breed,age)

# State is the attributes
# Methods is the behaviour of the object
# Self is a reference to the object that is being created.
# Attributes that are part of the class are static.

# Reference types:

"""
    Class Student:
       pass
       
    Student.name = class variable 
    s1.name = instance/object
       
"""
#---------------------------------------------------------------
"""
   class CSStudent:
      stream = 'cse'  #Class variable
      def __init__(self,roll,name):
          self.roll = roll   #Instance variable
          self.name = name   #Instance variable
          

"""

# Slots = used to specify the name of each state variable, avoids errors

class Card:
    __slots__ = ['rank','suit','name','shorthand']
    
    def __init__(self,rank,suit,name,shorthand):
        self.rank = rank
        self.suit = suit
        self.name = name
        self.shorthand = shorthand
        
        
        
        
class Student:
    # __slots__ = ['id','name','age','gpa']
    def __init__(self,id,name,age,gpa):
        self.id = id
        self.name = name # Without slots, python does not show error
        self.age = age      # With slots, python shows attribute error
        self.gpa = gpa
        
student1 = Student(123,"Reema",19,4.0)
print(f'Student1: {student1.id}, {student1.name}, {student1.age}, {student1.gpa}')
        
        
class Fruit:
    __slots__ = ['type','price']
    def __init__(self,type,price=0):
        self.type = type
        self.price = price
        
    def display(self):
        print(f"Fruit: {self.type} | Price: {self.price:.2f} AED")
        
fruit1 = Fruit("Apple",3.50)
fruit2 = Fruit("Cherry",1.55)
fruit3 = Fruit("Mango",2.75)


fruit1.display()
fruit2.display()
fruit3.display()

fruits = [fruit1,fruit2,fruit3]
total = sum(fruit.price for fruit in fruits)
print(f"\nTotal cost of all fruits: {total:.2f} AED")


class Pet:
    __slots__ = ['species','name','weight','furcolor','age']
    
    def __init__(self,species,name,weight,furcolor,age = 0):
        self.species = species
        self.name = name
        self.weight = weight
        self.furcolor = furcolor
        self.age = age
        
    def feed(self,calories):
        pounds = calories/3000
        self.weight = self.weight + pounds
        
    def walk(self,miles):
        pounds = miles*100/3000
        self.weight = self.weight - pounds
        
        
def print_pet(pet):
    print(f"Pet: {pet.species} | {pet.name} | {pet.weight} lbs | {pet.furcolor} | {pet.age} yr")
        
pet1 = Pet("Dog","Lily",7,"Grey",2)
print_pet(pet1)

pet1.feed(1800)
print_pet(pet1)

pet1.walk(1.5)
print_pet(pet1)


# Methods: declared inside of a class, first parameter is always self
# Should always interact with the fields in an object in some way, or else not needed.
# A function that belongs to an object is called a method.


# In python, naming a field with a double underscore marks it as private.
# Trying to directly access or change the field from outside of the class causes AttributeError
# Making field private is an important aspect of encapsulation.
# Methods don't work on private fields.

#normal vs private slots
class Pet:
    __slots__ = ['species', 'name', 'weight', 'fur_color', '__age']
    def __init__(self, species, name, weigt, fur_color, age=0):
        self.species = species
        self.name = name
        self.weight = weigt
        self.fur_color = fur_color
        self.age = age
        def  get_name(self):
            return self.name
        def get_weight(self):
            return self.weight
        def feed (self, calories):
            pounds =  calories / 3000
            self.weight += self.weight + pounds
    def set_weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            print("Weight must be postive")
    def set_age(self, age):
        self.__age = age    
class Pet:
    __slots__ = ['__species','__name','__weight','__furcolor','__age']
    
    def __init__(self,species,name,weight = 0.0, fur_color="Unknown",age = 0):
        self.__species = species
        self.__name = name
        self.__weight = weight
        self.__fur_color = fur_color
        self.__age = age
    def get_species(self):
        return self.__species
    def get_name(self):
        return self.__name
    def get_weightt(self):      
        return self.__weight
    def get_fur_color(self):  
        return self.__fur_color
    def get_age(self):
        return self.__age
#QUIZZZZZZ ANSD FINALALALA

class Car:
    __slots__ = ("__vin","__make","__model","__year","__mileage","__fuel")
    def __init__ (self, vin, make, model, year, mileage, fuel):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__fuel = fuel
#Accessors - access everrything 
    def get_vin(self):
        return self.__vin 
    def get_make(self):
        return self.__make    
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year 
    def get_mileage(self):   
        return self.__mileage 
    def get_fuel(self):
        return self.__fuel
#Mutators only mutuatw smth that makes sense is practical
    def set_mileage (self, mileage):
        self.__mileage = mileage
    def set_fuel (self, fuel):  
        self.__fuel = fuel
    def print_car(self):
        print(f"Car VIN: {self.__vin} \nMake: {self.__make} \nModel: {self.__model} \nMileage: {self.__mileage} \nFuel: {self.__fuel}")
# def main():
#     car1 = Car ("1wfuybugy", "Toyota", "Corolla", 2020, 15000, 50)
#     car1.print_car()
#     car1.set_mileage(16000)
#     car1.set_fuel("Full Tank")
#     print("After update: ")
#     car1.print_car()

# if __name__ == "__main__":
#     main()
#Special methods: __init__, __str__, __repr__
#__str__ method: automatically called when we try to print an object
#__repr__ method: used to obtain an ambiguous string representaion of an object how u want to represent used for detailed function
#                 useful for debugging
# class Car:
#     __slots__ = ("__vin","__make","__model","__year","__mileage","__fuel")
#     def __init__ (self, vin, make, model, year, mileage, fuel):
#         self.__vin = vin
#         self.__make = make
#         self.__model = model
#         self.__year = year
#         self.__mileage = mileage
#         self.__fuel = fuel
#     def __str__(self):
#         return f"{self.__vin} - {self.__make}{self.__model}"
    
# def main():
#     c = Car("M2343JEW", "Honda", "civic", 2019, 60000, 45)
#     print(c)
# main()   
class Car:
    __slots__ = ("__vin","__make","__model","__year","__mileage","__fuel")
    def __init__ (self, vin, make, model, year, mileage, fuel):  
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__fuel = fuel
    def __repr__(self):
        return (
            f"Car(\n"
            f" VIN: {self.__vin}\n"
            f" Make: {self.__make}\n"
            f" Model: {self.__model}\n"
            f" Year: {self.__year}\n"
            f" Mileage: {self.__mileage}\n"
            f" Fuel: {self.__fuel}\n"
            f")"
        )
def main():
    c = Car("M2343JEW", "Honda", "civic", 2019, 60000, 45)
    print(c)

main()  
#STACKS data structures
#list like data structure where items are added and substacted from one end and the end is at the top
#LIFO last in first out
#top is nothing but a pointer that points to the top end
#push : add item to the top
#pop: remove item from the top

#queues 
#first in first out FIFO
#items are added from one end called rear and removed from the other end called front
#Enqueue: add item to the rear
#Dequeue: remove item from the front
#add = back/rear is incremented
# remove= front is incremented
#enqueue()
#linear O(n)
#binary O(log2n)
#inplace sorting is destructive and not in place is not destructive generates a copy original data stays intact
# insertion sort, merge sort, quicksort
# gein insertion sort array divded into 2 parts a sorted partition and a unsorted partition 
#best case O(n)
#average case O(n^2)
#quadratic time o(n^2)
#worst case O(n^2)
#Merge-sor: divide and conquer algorithm even indexes in half1 and odd indexes in half 2
#0 1 2 3 4 5 6 7 8
#3 4 5 8 1 6 2 0 5
#even indexes: 0 5 1 2 5
#odd indexes: 4 8 6 0
#Split again
#0 1 5 | 5 2 ---- 1  5  5  2
#4 6 | 8 0   ---- 4   6  8  0
#Merge
#when merge sort and merge all the arrays
# 5 | 6 | 2 | 7 | 8 | 9 | 3 | 4 
# 2 5 6 7 | 3 4 8 9
#2 3 4 5 6 7 8 9 


