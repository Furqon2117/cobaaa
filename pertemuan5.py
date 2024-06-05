from abc import ABC, abstractmethod

class Animal(ABC):
    def speak(self):
        pass
    def foot(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Bark!"
    def foot(self):
        return 4
    
class Chicken(Animal):
    def speak(self):
        return "Chick - Chick!"
    def foot(self):
        return 2
    
def animal_behavior(animal: Animal):
        print (f"The animal says:  {animal.speak()}")
        print(f"The animal has: " + str(animal.foot()) + " legs")
# Abstract

dog = Dog();
chicken = Chicken();

animal_behavior(dog);
animal_behavior(chicken);

# print("Sounds of the dog : " + dog.speak() + " | Dog has : " + str(dog.foot()) + ' foot ' + " | Sounds of the chicken : " + chicken.speak() + " | Chicken has : " + str(chicken.foot()) + " foot")