from Dog import Dog
import random
# Exercise 1: Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Siamese(Cat):
    def sing(self,sounds):
        return f'{sounds}'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_cat = Bengal("Luna", 3)
chartreux_cat = Chartreux("Milo", 2)
siamese_cat = Siamese("Bella", 4)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)
sara_pets.walk()


# Exercise 3: Dogs Domesticated
class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)
        self.trained=False
    
    def train(self):
        print(self.bark())                    
        self.trained = True 
    
    def play(self,*args):
        dog_names = []
        for dog in args:
            if isinstance(dog,Dog):  # if it's a Dog object
                dog_names.append(dog.name)
            else:                    # if it's just a string
                dog_names.append(str(dog))

        all_names=" , ".join(dog_names)
        print(f"{self.name} , {all_names} all play together !")
    
    def do_a_trick(self):
        if self.trained :
            tricks = ["does a barrel roll",
                      "stands on his back legs", 
                      "shakes your hand", 
                      "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")  # choose random tricks
        else :
            print(f"{self.name} is not trained yet!")

my_dog = PetDog("Fido", 2, 10)
dog2 = PetDog("Buddy", 3, 12)
dog3 = PetDog("Max", 4, 15)
my_dog.train()
my_dog.play(dog2,dog3)
my_dog.play("Toni")
my_dog.do_a_trick()

# Exercise 4: Family and Person Classes
class Person:
    def __init__(self,first_name,age):
        self.first_name = first_name
        self.age = age
        self.last_name = "" 
    
    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []  # empty list for Person objects

    def born(self, first_name, age):
        new_person = Person(first_name, age) # create Person
        new_person.last_name = self.last_name  # set their last name to the family's last name
        self.members.append(new_person) # add to family members
        print(f"Welcome to the family, {new_person.first_name} {new_person.last_name}!")

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(f"{first_name} You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print(f"{first_name} Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No member named {first_name} found in the family.")

    def family_presentation(self):
        print(f"\nFamily name: {self.last_name}")
        print("Members:")
        for person in self.members:
            print(f"- {person.first_name}, {person.age} years old")

oriyanes= Family("Oriyane")

oriyanes.born("Alen" , 14)
oriyanes.born("Jana" , 19)
oriyanes.born("Jimmy", 22)

oriyanes.check_majority("Alen")
oriyanes.check_majority("Jana")
oriyanes.check_majority("Jimmy")
oriyanes.check_majority("Tony")  

oriyanes.family_presentation()







