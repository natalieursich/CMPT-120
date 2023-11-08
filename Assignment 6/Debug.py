class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    def oldCar(self):
        if self.year < 2015:
            return("old car")
        else:
            return("new car")
    
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Dixie" , 7)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("Bob", 819, "Retail")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make
    myCake = Cake("Funfetti", "Vanilla")
    print(myCake.flavor, myCake.frosting)
    
    #and now create another cake and print it out
    nextCake = Cake("Chocolate", "Chocolate")
    print(nextCake.flavor, nextCake.frosting)
    
    #create a cat!
    cat1 = Cat("Sprinkles", 6, "long-haired")
    #create another cat!
    cat2 = Cat("Kitty", 3, "short-haired")
    print(cat2.name, cat2.age, cat2.fur_length)
    
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    car1 = Car("Ford Escape", 2020, "black")
    #Now print out the function you made for car :)
    print(car1.model, car1.year, car1.color)

main()
