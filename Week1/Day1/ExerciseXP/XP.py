# Exercise 1 Hello World
print("Hello world\n" *4)

# Exercise 2 Some Math
print(pow(99,3)*8)

# Exercise 3 What is the output?
5 < 3  #False
3 == 3 #True
3 == "3" #False
#"3" > 3 #Type error
"Hello" == "hello" #False

# Exercise 4: Your computer brand
computer_brand = "HP"
print("I have a "+computer_brand+ " computer.")

# Exercise 5: Your information
name="Laila"
age=24
shoe_size=40
info = f"My name is {name}, I'm {age} years old and my shoe size is {shoe_size}"
print(info)

# Exercise 6: A & B
a=100
b=10
if a>b :
    print("Hello world")

# Exercise 7: Odd or Even
number=int(input("Enter a valid number :"))
if number%2==0 :
    print("The number is even")
else :
    print("The number is odd")

# Exercise 8: What’s your name?
user_name=input("Enter your name : ")
my_name="laila"
if user_name.lower() == my_name.lower() :
    print("oh we are twins, we have the same name")
else :
    print(f"My name is {my_name}, nice to meet you {user_name} ")

# Exercise 9: Tall enough to ride a roller coaster
my_height=int(input("Enter your height in centimeters : "))
if my_height > 145 :
    print("You are tall enough to ride")
else :
    print("You need to grow some more to ride")