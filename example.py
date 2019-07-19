# import math
from math import sqrt, ceil
x = sqrt(9)
print(x)

y = ceil(x)
print(y)

# y=math.ciel()

import random

# we can generate a random number using the randit method
random_numbfer =random.randint(0,20)
print(random_number)

random_number=random_number.randint(0,20)

pi=3.14
r = 8


print(2*pi*r)
x=12
print(x)
x='hello'
print(x)


print("What is your name")
name= input()
print("Where do you come from?")
place= input()
print("What do yuwant from life?")
intent= input()

import sys

name = sys.argv[1]

print("How old are you?")
age = int(input())

print(name)
print(age)

import sys

name = sys.argv[1]
age = sys.argv[2]

print(name)
print(age)
height = 24 # The unit is inches
if height > 70 :
    print("You are really tall");
if height < 70:
    print(height -40)

    height = 54 # inches
if height > 70 :
    print("You are really tall")
else:
    print("You are really short")

height = 68 # inches
if height > 70 :
    print("You are really tall")
elif height > 60:
    print("You are of average height")

else:
    print("You are really short")
name = "Dr.Eng.Joflix CGH"
list_a = []

if list_a:
    print("I will not run")
else:
        print(name)
numbers = [1,2,3,4,'john','5']

for number in numbers:
#     print(number)
list_a = list(range(0,10))
print(list_a)

for i in range(0,10):
 print('I would love'+" "+ str(i) +' '+ 'cookies')
numbers = [1, 2, 3, 4, 5,6]
for i in numbers:
    if i % 3 == 0:
        print(i)


players = 20

while True :
    print("The remaining players are",players)
    players += 10
    if players <=80:
        continue
    if players > 100:
      break
'''
in a team of members 20, some numbers are taken
and want to display the numbers that are not taken
so others don't pick the picked numbers
'''

# taken numbers
numTaken = [3,5,7,11,13]

print("Available numbers")

# loop
for i in range(1,21):
    if i in numTaken:
        continue
#     print(i)
my_list = ["a","b","c","d"]
# my_other_list =list(my_list)
#
# print(my_list + my_other_list)
list_a = ["a","b","c","d"]
list_b = [1,2,3,4,5,6]
list_b.reverse()
# Joining list_b to list_a
my_list.append(14)
list_b.extend(list_a + my_list)
my_list.sort()
# print(list_a) # this will print ["a","b","c","d",1,2,3,4,5,6]
print(list_b) # this will print [1,2,3,4,5,6]
print(my_list)
list_me=[6,7,1,2,3,8,5,4]
list_me.sort()
print(list_me)
tuple_a = ("a","b","c","d") # tuple of strings
tuple_b = (1,2,3,4,5,6) # tuple of numbers
tuple_c = (1,"west",34,"longitude") # mixed tuple
tuple_d = tuple() #empty tuple


# Creating empty dictionaries
my_dict = {}
my_dict = dict()

# Creating a dictionary with keys and values
my_cat = {'name':'Mr sniffles','age':"18", 'color':'black'}

cat_name = my_cat['name']
cat_age = my_cat['age']
print('My cat is'+' '+cat_name + ' '+'and age'+' '+ cat_age) # 'Mr sniffles'
'''
'''
birthdays = {"John":"August 1","Marcus":"April 8"}
birthdays["mary"] = "September 14"
print(birthdays) # this prints {"John":"August 1","Marcus":"April 8","Mary":"September 14"}
'''
'''
'''
'''
birthday = {"John":"August 1","Marcus":"April 8","Mary":"September 14"}

print(list(birthday.keys())) # this prints ['John', 'Marcus', 'Mary']the ne
print("Enter a string")

input_string = input()

characters = {}
for character in input_string:
    characters.setdefault(character,0)
print(characters)


print("Enter another string")

input_string = input()

characters = {}

for character in input_string:
    characters.setdefault(character,0)
characters[character] = characters[character] + 2

print(characters)
name = "James"
age = 19

print(f"My name is {name} and I am {age} years old")

print('Beyonce\'s lemonade stand')

# print(r'Beyonce\'s lemonade stand')
alpha = "Ilikeoldmusic"
password = "K34jndnks"
number_string = "12345"
tabbs = "       j"
titles = "I Love Cups"
false_titles = "I Love Cups"

print( alpha.isalpha() )
print( password.isalnum() )
print( number_string.isdecimal() )
print( tabbs.isspace() )
print( titles.istitle() )
print( false_titles.istitle())

#####MADLIB BEGINS HERE#####

print('input noun')
name = input()
print('Input an adjective')
adjective = input()
print('Input a verb')
verb = input()
characters={}
print(f"john you lied about your {name} remember that time we were with you behind the {adjective} you gave your name as {verb}")
####MADLIB ENDS HERE#####


#####Type casting begins here by converting an int to a str by usin str() method####
print out user's name and age
name = "James"
age = 19

print("My name is " + name + " I am " + str(age) +" years old")


####
name = "James"
age = 19
weight = '79' # Kilograms

age_weight_ratio = float(weight)//age

print(age_weight_ratio)


name = "James"
age = 19
weight = '79' # Kilograms

age_weight_ratio = int(weight)//age

print(age_weight_ratio)

name = "James"
age = 19
weight = '79' # Kilograms

age_weight_ratio = float(weight)/age

print(age_weight_ratio)


######TYPE CASTING ENDS HERE ####


####SLICING BEGINS HERE######
greetings = 'Hello, Moringa!'

part_one = greetings[0:8]
print(part_one)


greetings = 'Hello, Moringa!'

part_one = greetings[0:5]
print(part_one)

greetings = 'Hello, Moringa!'

part_two = greetings[5:16]
print(part_two)

greetings = 'Hello, Moringa!'

part_one = greetings[-8:-1]
print(part_one)

greetings = 'Hello, Moringa!'

part_one = greetings[0:]
print(part_one)
number = [1,2,3,4,5,6,7,8,9]
four_digits = number[:4]
print(four_digits)
number = [1,2,3,4,5,6,7,8,9]
four_digits = number[:3]
print(four_digits)


########END OF SLICING######


####to create our own functions in python.

Functions are blocks of code that begin with the def keyword#########


def fun_a():
    print("I have been called")

fun_a()

"I have been called"

This example we have created a function with no arguments and in the function we have a print statement that outputs a string

We then went on to call the function and we got our desired output.


####END OF Functions######

####PARSING ARGUMENTS ######

def fun_a (a,b):
    print((a+b)**2)

fun_a(1,4)



Python can also take on keyword arguments. These are arguments that are already defined

def fun_a(a = 1,b = 4):
    print(a+b)

fun_a(a=6,b=7);

We could also call the function without passing any parameters. Then the default keyword arguments values will be passed in

def fun_a(a = 1,b = 4):
    print(a+b)

fun_a();
#####END 0F PARSING ARGUMENTS#####


#####Creating an empty func()#####

Empty function
def fun_a():
 Python has a keyword called pass that can help us here. pass allows us to create empty blocks of code because when it runs it returns a null or nothing.
def fun_a():
    pass

######Functions that return something#####

def fun_a (a,b):
    return a*b**2

sum = fun_a(4,5)

print(sum)

##### Here, we use the return statement, to get the value from the operation performed in the function. #####

#######Exceptions and Error Handling####
