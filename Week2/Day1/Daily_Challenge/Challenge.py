# Step 1: Create the Farm Class
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # Step 3: Add animals to the farm
    #def add_animal(self, animal_type, count=1):
        # If animal exists, increase count; otherwise, add new animal
        # (We don't need self.animal_type — just use the local variable)
        #if animal_type in self.animals:
            #self.animals[animal_type] += count
        #else:
            #self.animals[animal_type] = count

    # Step 8: upgrade the add_animal Method
    def add_animal(self, **kwargs):
    # Loop through all animals passed as keyword arguments
       for animal_type, count in kwargs.items():
        # If the animal already exists, add to its count
        if animal_type in self.animals:
            self.animals[animal_type] += count
        # Otherwise, add it as a new animal
        else:
            self.animals[animal_type] = count

    # Step 4: Display farm info
    def get_info(self):
        info = f"{self.name}'s farm \n"
        for key, value in self.animals.items():
            info += f"{key} : {value}\n "
        info += "\nE-I-E-I-0!"
        return info

    # Step 6: Return a sorted list of animal types (keys from the dictionary)
    def get_animal_types(self):
        # sorted() returns a new list of keys in alphabetical order
        return sorted(self.animals.keys())
    
    # Step 7: Implement the get_short_info Method
    def get_short_info(self):
        animal_list=self.get_animal_types()

        names=[]
        for animal in animal_list :
            if self.animals[animal] > 1:
                names.append(animal + "'s")
            else :
                names.append(animal)
        # Join the names with commas and "and" before the last one
        sentence = ", ".join(names[:-1]) + " and " + names[-1]
        return f"{self.name}'s farm has {sentence}."



# Step 5: Test the class
macdonald = Farm("McDonald")
#macdonald.add_animal('cow', 5)
#macdonald.add_animal('sheep')
#macdonald.add_animal('sheep')
#macdonald.add_animal('goat', 12)
macdonald.add_animal(cow=5, goat=12, lion=3, camel=2, horse=12,tiger=1)
macdonald.add_animal(sheep=1)
macdonald.add_animal(sheep=1)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())