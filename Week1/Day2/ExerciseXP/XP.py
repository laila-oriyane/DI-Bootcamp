# Exercise 1: Favorite Numbers
my_fav_numbers = {3,7,9,19}
print("My favorite numbers:", my_fav_numbers)
my_fav_numbers.add(15)
my_fav_numbers.add(88)
print("After adding two numbers:", my_fav_numbers)
my_fav_numbers.remove(88)
print("After removing the last added number:", my_fav_numbers)
friend_fav_numbers = {4, 7, 20, 15}
print("Friend favorite numbers:", friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

# Exercise 2: Tuple
my_tuple = (1, 2, 3, 4, 5)
# my_tuple.append(9)   # This will cause an error because tuples are immutable
# my_tuple[0] = 0     # This will also cause an error
print("Tuple:", my_tuple)

# Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)
apples_count = basket.count("Apples")
print("Number of 'Apples' in the list:", apples_count)
basket.clear()
print("Final list:", basket)

# Exercise 4: Floats
# Float : un nombre avec une virgule décimale
# Int :  un nombre entier
# La différence est que les nombres flottants peuvent représenter des valeurs fractionnaires, contrairement aux nombres entiers.
numbers = []
start_number = 1.5
end_number = 5.0
step = 0.5
while start_number <= end_number:
    if start_number.is_integer() :
        numbers.append(int(start_number))
    else :
        numbers.append(start_number)
    
    start_number += step

print(numbers)

# Exercise 5: For Loop
for number in range(1,21):
    print(number)
print("Even numbers :")

numb=list(range(1,21))
for num in numb:
    if numb.index(num) % 2 == 0:
        print(num)

# Exercise 6: While Loop
while True:
    user_name = input("Enter your name : ")
    if user_name.isdigit() or len(user_name) < 3 :
        print("Invalid input. Please enter a valid name (at least 3 letters).")
    else :
        print("Thank you!")
        break

# Exercise 7: Favorite Fruits
fav_fruits_input = input("Enter your favorite fruits (separated by spaces): ")
fav_fruits = fav_fruits_input.split()
chosen_fruit = input("Choose a fruit: ")
if chosen_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings
toppings =[]
base_price = 10
topping_price = 2.5
while True :
    topping = input ("Enter a topping (or 'quit' to stop):")
    if topping == "quit" :
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + len(toppings) * topping_price
print("Toppings:", toppings)
print(f"Total cost: {total_cost} $")

# Exercise 9: Cinemax Tickets

total_cost = 0
num_people = int(input("How many people are buying tickets? "))
for i in range(num_people):
    age = int(input(f"Enter the age of person {i+1}: "))
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost

print("Total ticket cost: $", total_cost)


#Bonus
allowed = []

for i in range(int(input("How many people? over 16 and under 21: "))):
    age = int(input("Enter age: "))
    if 16 <= age <= 21:
        allowed.append(age)

print("Allowed ages:", allowed)


