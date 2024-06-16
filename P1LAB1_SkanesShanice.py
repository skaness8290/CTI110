Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> FirstName = input("firstname")
firstname
>>> Lastname = input("lastname")
lastname
>>> print("Enter you first name:", FirstName)
Enter you first name: 
>>> print("Enter your last name:", Lastname)
Enter your last name: 
>>> print("Hello!", Firstname, Lastname, "Welcome to CTI110!!")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("Hello!", Firstname, Lastname, "Welcome to CTI110!!")
NameError: name 'Firstname' is not defined. Did you mean: 'FirstName'?
>>> print("Hello", Firstname, "Welcome to CTI110!")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Hello", Firstname, "Welcome to CTI110!")
NameError: name 'Firstname' is not defined. Did you mean: 'FirstName'?
>>> print("Hello", FirstName, Lastname, "Welcome to CTI110!")
Hello   Welcome to CTI110!
>>> #ShaniceSkanes
>>> #06/15/24
>>> #P1
>>> #P1Lab2
