# Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys,values))
print(my_dict)

# Exercise 2: Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
print(family)
total_coast = 0
for name,age in family.items() :
    if age < 3 :
        price = 0
    elif 3 <= age <= 12 :
        price = 10
    else :
        price = 15
    print(f"{name.title()} ticket is : {price} $ ")
    total_coast += price

print("Total coast : ", total_coast)

# Exercise 2 : Bonus
family = {}
total_coast=0
family_member = int(input("Enter How many family member ? "))
for fam in range(family_member) :
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    family[name]=age

for name,age in family.items() :
    if age < 3 :
        price = 0
    elif 3 <= age <= 12 :
        price = 10
    else :
        price = 15
    print(f"{name.title()} ticket is : {price} $ ")
    total_coast += price

print("Total coast : ", total_coast)

# Exercise 3: Zara
brand = {
    'name' : 'Zara' ,
    'creation_date' : 1975 ,
    'creation_name' : 'Amanico Ortega Gaona' ,
    'type_of_clothes' : ['men', 'women', 'children', 'home'] ,
    'international_competitors' : ['Gap', 'H&M', 'Benetton'] , 
    'number_stores' : 7000 ,
    'major_color' : {
    'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']
    }
}

print(brand)
brand['number_stores'] = 2
print("Zara clients are " , brand['type_of_clothes'])
brand['country_creation'] = 'Spain'
print(brand)
brand['international_competitors'].append("Desigual")
del brand['creation_date']
print("Last competitor:", brand['international_competitors'][-1])
print("US color :" , brand['major_color']['US'])
print("Number of keys : ", len(brand))
print("All keys :" , brand.keys())

# Exercise 3: Bonus
more_on_zara = {
    'creation_date' : 1970 ,
    'number_stores' : 9000 
}
print(more_on_zara)
brand.update(more_on_zara)
print(brand)

# Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# mapping characters to their indices:
# enumerate give this index and the value from a list at the same time 
dict1 = {user : index for index, user in enumerate(users)}
print(dict1)
# mapping indices to characters:
dict2 = {index : user for index, user in enumerate(users)}
print(dict2)
# characters are sorted alphabetically and mapped to their indices : 
dict3 = {user : index for index, user in enumerate(sorted(users))}
print(dict3)
