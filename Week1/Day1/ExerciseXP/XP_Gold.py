# Exercise 1 : Hello World-I love Python
print("Hello world\n" *4 + "I love python\n" *4)

# Exercise 2 : What is the Season ?
month=int(input("Enter a valid month between 1 and 12 : "))
if month in [3,4,5]:
    print("Spring")
elif month in [6,7,8]:
    print("Summer")
elif month in [9,10,11]:
    print("Autumn")
elif month in [12,1,2]:
    print("Winter")
else :
    print("Month invalide")