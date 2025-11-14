import string
import random
import datetime
from faker import Faker

# Exercise 1: Currencies
class Currency:
# constructor
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
# string representation
    def __str__(self):
        return f"{self.amount} {self.currency}s"
# official representation
    def __repr__(self):
        return self.__str__()
# integer representation
    def __int__(self):
        return self.amount
# addition
    def __add__(self,other):
        # add int to amount
        if isinstance(other,int):
            return self.amount + other
        # add Currency to amount
        if isinstance(other, Currency):
        # check if currencies are the same
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            return self.amount + other.amount
        raise TypeError(f"Unsupported operand type(s) for +: 'Currency' and '{type(other).__name__}'")
# in-place addition
    def __iadd__(self, other):
        # add int to amount
        if isinstance(other, int):
            self.amount += other
            return self
        # add Currency to amount
        if isinstance(other, Currency):
        # check if currencies are the same
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self
        raise TypeError(f"Unsupported operand type(s) for +=: 'Currency' and '{type(other).__name__}'")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)          # 5 dollars
print(int(c1))     # 5
print(repr(c1))    # 5 dollars
print(c1 + 5)      # 10
print(c1 + c2)     # 15
print(c1)          # 5 dollars
c1 += 5
print(c1)          # 10 dollars
c1 += c2
print(c1)          # 20 dollars
# print(c1 + c3)   result : TypeError: Cannot add between Currency type <dollar> and <shekel>

# Exercise 3: String module
all_letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# initialize an empty string
random_string = ''
# generate a random string of 5 letters
for _ in range(5):
    # append a random letter to the string
    random_string += random.choice(all_letters)  # pick a random character

print(random_string)

# Exercise 4: Current Date
def show_current_date():
    # get today's date
    today = datetime.date.today()
    print("Today's date is:", today)
show_current_date()

# Exercise 5: Amount of time left until January 1s
def time_until_january_first():
# gives you the current year, month, day, hour, minute, second.
    now = datetime.datetime.now()
    print("Current date and time:", now)
# get the next year
    next_year = now.year + 1
#create a date for January 1st at midnight:
    jan_first = datetime.datetime(next_year, 1, 1)
    print("January 1st at midnight : ",jan_first)
# calculate the difference between now and January 1st
    time_left = jan_first - now
    print("Time left until January 1st:", time_left)

time_until_january_first()

# Exercise 6: Birthday and minutes
import datetime

def minutes_lived(birthdate_str):
    # Convert the string into a datetime object (format: YYYY-MM-DD)
    birth_date = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")

    # Get current date and time
    now = datetime.datetime.now()

    # Difference between now and birthdate
    diff = now - birth_date

    # Convert seconds to minutes
    minutes = diff.total_seconds() / 60

    print(f"You have lived about {int(minutes)} minutes.")

minutes_lived("1990-01-01")

# Exercise 7: Faker Module
users = []
def generate_users(n):
# create a Faker instance
    fake = Faker()
    for _ in range(n):
# create a user dictionary
        user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
        }
        users.append(user)
    return users

# generate 5 users and print them
generated_users = generate_users(5)
print("Generated Users:")
# print each user
for user in generated_users:
    print(user)

