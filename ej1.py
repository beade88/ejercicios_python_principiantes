'''
Exercise 1

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and
    printing out that many copies of the previous message.
    (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines.
    (Hint: the string "\n is the same as pressing the ENTER button)
'''
# nombre = raw_input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# Refactoring using English and only input not raw_input.
# Remember my advice about using '' instead of "" for string

# For some rare reason on my PC input for name
# does not work, test it on yours and tell me
name = input('Enter your name: ')
age = int(input('Enter your age: '))

# x = str ((2019 - edad) + 100)
# No need to cast to str here, because you will use format later.
# Also dont use x as var name, in Python everything
# must be as readable as possible. For example is better use
# year as name than x, because when you see x is hard to imagine
# what is for that var
year = 2019 - age + 100

# print(nombre + " usted cumplira 100 annos en el anno " + x)
print('{} you will be 100 years old on year {}'.format(name, year))
