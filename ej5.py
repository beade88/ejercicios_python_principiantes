'''
Exercise 5

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on two
lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (dont worry if you cant figure this
    out at this point - we will get to it soon)
'''
# Este esta implementado con python3 desde el inicio :D

# ******************************************************************
# Please remake this excercise using a for loop to fill the lists
# then push again
# ******************************************************************

print('List 1')
list_1 = []
for elements_1 in range(0, 6):
    elements_1 = int(input('Type a number: '))
    list_1.append(elements_1)
print('List 2')
list_2 = []
for elements_2 in range(0, 5):
    elements_2 = int(input('Type a number: '))
    list_2.append(elements_2)
list_3 = []
print("The numbers that are common between the lists are: ")
for x in list_2:  # PEP8 here, lista2:
    if x in list_1:  # PEP8 here, lista1:
        list_3.append(x)
print(list_3)

# Remember, in PEP8 andy sign (, or :) goes without space before.
# Any sign like (*, +, -) goes with spaces before and after
