"""
Exercise 14
Write a program (function!) that takes a list
and returns a new list that contains all the
elements of the first list minus all the duplicates...
"""


# This function returns  a list that contains the elements of the initial list but without duplicates elements.
def list_without_duplicates(list_to_analyze):
    return set(list_to_analyze)

    # you should return using list_to_analyze,
    # this is the name of the param
    return set(my_list)


list_length = int(input('Type a length of your list: '))
my_list = []
for i in range(0, list_length):
    my_list.append(int(input('Type a number: ')))

print(list_without_duplicates(my_list))
