Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#ShaniceSkanes
#06/15/2024
#
#P1HW2
#Traveling expense calculator
budget
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    budget
NameError: name 'budget' is not defined
budget =input("Enter budget")
Enter budget
budget =int(budget)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    budget =int(budget)
ValueError: invalid literal for int() with base 10: ''
print(type(baseVal))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(type(baseVal))
NameError: name 'baseVal' is not defined
print(type(budget))
<class 'str'>
int(budget)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int(budget)
ValueError: invalid literal for int() with base 10: ''
>>> Fuel =input("Fuel cost")
Fuel cost(int)
>>> Accomodation =input("Accomodation's cost")
Accomodation's cost(int)
>>> Food =input("Food cost")
Food cost(int)
>>> print("Enter budget", budget)
Enter budget 
>>> Location =input("Travel destination")
Travel destination
>>> print("Enter your travel destination", Location)
Enter your travel destination 
>>> print("How much do you think you will spend on fuel?", Fuel)
How much do you think you will spend on fuel? (int)
>>> print("Approximately, how much will you need for accomodation/hotel?", Accomodation)
Approximately, how much will you need for accomodation/hotel? (int)
>>> print("Last how much do you need for food?", Food)
Last how much do you need for food? (int)
>>> budget =input(budget)
int(budget)
>>> print("----------Travel Expenses---------")
----------Travel Expenses---------
>>> print("Location:", Location)
Location: 
>>> print("Initial Budget:", budget)
Initial Budget: int(budget)
>>> print("Fuel:", Fuel)
Fuel: (int)
>>> print("Accomodation:", Accomodation)
Accomodation: (int)
>>> print("Food", Food)
Food (int)
>>> print("Remaining Balance:", budget - Fuel - Accomodation - Food)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print("Remaining Balance:", budget - Fuel - Accomodation - Food)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
