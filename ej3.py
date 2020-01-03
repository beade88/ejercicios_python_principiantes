'''
Exercise 3

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the
    elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from
    the original list a that are smaller than that number given by the user.
'''

# I will not translate any more :D. I hope is clear for you
# that everytthing must be in English :D

print('Lets to create a list. Please type the numbers of your list')
list_length = int(input(print('First type a number of your list elements: ')))
'''
a = input ("Ingrese un numero: ")
b = input ("Ingrese un numero: ")
c = input ("Ingrese un numero: ")
d = input ("Ingrese un numero: ")
e = input ("Ingrese un numero: ")
f = input ("Ingrese un numero: ")
g = input ("Ingrese un numero: ")
h = input ("Ingrese un numero: ")
i = input ("Ingrese un numero: ")
j = input ("Ingrese un numero: ")
my_list = [a, b, c, d, e, f, g, h, i, j]
'''
# Very old school :D. It works, but its old school
# I will put my code without explanation this way
# I force you to understand.
# Only one tip: when somethings is repetitive always use a loop.
# Look:
my_list = []
for number in range(0, list_length):
    number = int(input('Enter one number: '))
    my_list.append(number)
print('This is your list: {}'.format(my_list))

# Only one hint here. Look the _ in the for loop.
# It is used when you want to loop but you dont care about
# the value in the loop.
# I dont know if I explained well.
# Look the difference:
# Is not the same when you have a list and you want to iterate over
# that and get the values of the list because you will do something
# with that values.
# list = [1, 4, 6, 7]
# for value in list:
#    print(value)
#    if value > 5:
#		print('YES')
# You see? I need to control value to make something
# But in the example I dont need to do anything with the value,
# thats why I use _
# But you can also do
# for value in range(0, 10):
#	number = int(input('Enter one number: '))
#	my_list.append(number)
# But yo see? you dont do anything with value, thats why you can ommit it
# and use _
# Use print() instead of print
print('Of the typed numbers, the numbers smaller than 5 are: ')
list_smaller_than_5 = []
for number2 in my_list:  # PEP8 here, it must be my_list:
    if number2 < 5:  # PEP8 here
        list_smaller_than_5.append(number2)
print(list_smaller_than_5)
# Use print() instead of print
print('Now you type a number, and I show you the elements in your list that are smaller than that number typed.')
number_to_compare = int(input("Type a number: "))
list_of_smallers = []
print('The numbers smaller than', number_to_compare,  'are: ')
for list_position in my_list:  # PEP8 here
    if list_position < number_to_compare:  # PEP8 here
        list_of_smallers.append(list_position)
print(list_of_smallers)

# A deal for you in this excercise!!!!
# Lets make the length of the list variable.
# I mean, the user will be asked about the length,
# then the list will be filled with that amount of numbers.
# Also change the way you show the numbers. Instead
# of showing one by one in different lines, show them in a list.
