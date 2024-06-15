Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Shanice Skanes
>>> #06/12/2024
>>> #P1Lab1
>>> #Using python to program basic input and output functions
>>> first_name = input()
last_name = input()
>>> print('Enter your first name', first_name)
Enter your first name last_name = input()
>>> print('Enter your last name:', last_name)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('Enter your las name:', last_name)
NameError: name 'last_name' is not defined. Did you mean: 'first_name'?
>>> print('Hello', first_name, last_name, 'Welcome to CTI 110')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print('Hello', first_name, last_name, 'Welcome to CTI 110')
NameError: name 'last_name' is not defined. Did you mean: 'first_name'?
