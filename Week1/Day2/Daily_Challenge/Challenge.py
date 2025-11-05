# 1. Multiples of a Number
number = int(input("Enter a number : "))
length = int(input("Enter the length : "))

multiples=[]
for i in range(length) :
    multiples.append(number * (i + 1))

print(multiples)

# 2. Remove Consecutive Duplicate Letters
user_word=input("Enter a String ")
new_word=""

for i in range(len(user_word)):
    if i==0 or user_word[i] != user_word[i-1] :
        new_word +=user_word[i]

print(new_word)