# Exercise 1: Cats
class Cat() :
    def __init__(self,name,age):
        self.name=name
        self.age=age

cat1 = Cat('kitty',5)
cat2 = Cat('Nosa',8)
cat3 = Cat('Maca',3)

def find_oldest_cat(cat1,cat2,cat3) :
    if cat1.age >= cat2.age and cat1.age >= cat3.age :
        return cat1
    elif cat2.age >= cat1.age and cat2.age >= cat3.age :
        return cat2
    else :
        return cat3

oldest_cat = find_oldest_cat(cat1,cat2,cat3)
print(f"The oldest cat name is {oldest_cat.name}, and age is {oldest_cat.age} years old")

# Exercise 2 : Dogs
class Dog() :
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def bark(self) :
        print(f"{self.name} goes woof!")
    def jump(self) :
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high")

davids_dog = Dog("Jimmy",50)
sarahs_dog = Dog("Luna",30)

print(f"{davids_dog.name} is {davids_dog.height} cm tall. ")
davids_dog.bark()
davids_dog.jump()
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall. ")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height :
    print(f"{davids_dog.name} is taller.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller.")
else:
    print("Both dogs are the same height.")

# Exercise 3 : Who’s the song producer?
class Song() :
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for line in self.lyrics :
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
class Zoo():
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]
        self.animals_groups={}
    
    # def add_animal(self, new_animal):
    # if new_animal not in self.animals:
    # self.animals.append(new_animal)

    def add_animal(self,*new_animals):
       for animal in new_animals :
           if animal not in self.animals :
             self.animals.append(animal)
        
    def get_animals(self):
        print(f"All the animals in the ZOO : {self.animals}")
    
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals :
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        self.animals.sort()
        self.animals_groups={} #Reset the dictionary for grouped animals, We clear the dictionary each time to make sure the grouping is fresh and accurate.
        for animal in self.animals:
            key=animal[0].upper()
            self.animals_groups.setdefault(key,[]).append(animal) #setdefault checks if the key exists; if not, it creates a new empty list, Then it appends the animal to the list.
    
    def get_groups(self) :
        for key,value in self.animals_groups.items() :
            print(f"{key} : {value}")

brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()








    
           
