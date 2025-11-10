import random

# Exercise 1: Concatenate lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1.extend(list2)
print(list1)

# Exercise 2: Range of numbers
for number in range(1500,2500) :
    if number % 5 == 0 and number % 7 == 0 :
        print(f"Multiples of 5 and 7 : {number}")

# Exercise 3: Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input('Enter your name : ').capitalize()
if user_name in names :
    print(f"Index : {names.index(user_name)}")
else :
    print('User not found !')

# Exercise 4: Greatest Number
a = int(input("Enter your First number : "))
b = int(input("Enter your Second number : "))
c = int(input("Enter your Third number : "))
print("The greatest number is : ",max(a,b,c))

# Exercise 5: The Alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
for letter in alphabet :
    if letter in vowels :
        print(f"{letter} is a vowel ")
    else :
        print(f"{letter} is a consonant ")

# Exercise 6: Words and letters
words = []
for i in range(7) :
    word = input(f"Enter {i+1} word : ")
    words.append(word)
letter = input("Enter a single letter : ").lower()

for word in words :
    if letter in word.lower() :
        print(f"In the word '{word}' , the letter '{letter}' found at index {word.lower().index(letter)} ")
    else :
        print(f"Sorry Letter '{letter}' not found in the Word '{word}'!")

# Exercise 7: Min, Max, Sum
numbers = list(range(1, 1000001))
print("MIN : ",min(numbers))
print("MAX : ",max(numbers))
print("SUM : ",sum(numbers))

# Exercise 8 : List and Tuple
values = input("Enter a sequence of comma-separated numbers : ")
numbers = values.split(",")
print(numbers)
print(tuple(numbers))

# Exercise 9 : Random number
wins = 0
losses = 0

print("Guess a number 1-9. Type 'q' to quit.\n")
while True :
    user_input = input("Enter your guess number (1-9) or 'q' to quit: ").strip()
    if user_input.lower() == 'q' :
        break

    if not user_input.isdigit():
        print("Please enter a number (digits only) or 'q' to quit.\n")
        continue

    user_number = int(user_input)
    number = random.randint(1, 9)

    if user_number == number :
        print("Winner !\n")
        wins += 1
    else :
        print("Looser !\n")
        losses += 1

print("\nGame Over!")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
    