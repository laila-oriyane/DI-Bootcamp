import random
# Exercise 1: What Are You Learning?
def display_message() :
    print("I am learning about functions in Python.")
display_message()

# Exercise 2: What’s Your Favorite Book?
def favorite_book(title) :
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonderland")

# Exercise 3: Some Geography
def describe_city(city,country='Unknown') :
    print(f"{city} is in {country}.")
describe_city("Paris")
describe_city("Reykjavik", "Iceland")

# Exercise 4: Random
def compare_number(number) :
    random_number = random.randint(1, 100)
    if number == random_number :
        print("Success !")
    else :
        print(f"Fail ! your number is {number} and the random number is {random_number}")
compare_number(15)

# Exercise 5: Let’s Create Some Personalized Shirts!
def make_shirt(size="Large",text="I love Python") :
    print(f"The shirt size is : {size} and the text is {text}")
make_shirt()
make_shirt("Meduim")
make_shirt("Large","XoXo")
make_shirt(size="Small", text="Hello!")

# Exercise 6: Magicians…
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names) :
    for name in magician_names :
        print(name)

def make_great(magician_names) :
    for name in magician_names :
        print(f"{name} the Great")
show_magicians(magician_names)
make_great(magician_names)

# Exercise 7: Temperature Advice
def get_random_temp() :
    return random.uniform(-10,40)

def main() :
    random_temperature = get_random_temp()
    print(f"The temperature right now is {random_temperature:.1f} degrees Celsius.")
    
    if random_temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= random_temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= random_temperature < 24:
        print("Nice weather.")
    elif 24 <= random_temperature < 32:
        print("A bit warm, stay hydrated.")
    else:  
        print("It’s really hot! Stay cool.")

main()

# Exercise 7 : Bonus

def get_random_temp():
    month = int(input("Enter the month number (1-12): "))

    if month in [12, 1, 2]:          
        temp = random.uniform(-10, 10)
    elif month in [3, 4, 5]:         
        temp = random.uniform(10, 22)
    elif month in [6, 7, 8]:         
        temp = random.uniform(23, 40)
    elif month in [9, 10, 11]:       
        temp = random.uniform(10, 25)
    else:
        print("Invalid month. Defaulting to random temperature between -10 and 40.")
        temp = random.uniform(-10, 40)
    
    return temp

def main():
    temperature = get_random_temp()
    print(f"\nThe temperature right now is {temperature:.1f} degrees Celsius.")

    if temperature < 0:
        print(f"Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print(f"Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 24:
        print("Nice weather.")
    elif 24 <= temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print(f"It’s really hot! Stay cool.")

main()


    

