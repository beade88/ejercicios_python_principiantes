"""
Exercise 12
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and
makes a new list of only the first and last
elements of the given list. For practice,
write this code inside a function.
"""

# What happens if the list size changes?
# Dont use fixed index for the last element
# you could say list[len(list) - 1]
# But this is OLD school...
# The right way is say list[-1]
# Search about slicing in lists. When use negatives index
# you go from last to begin :D (thats cool)
my_list = []
for i in range(0, 6):
    my_list.append(input('Type a number: '))


def new_list(list_to_process):
    my_list2 = (list_to_process[0], list_to_process[5])
    return my_list2


print(new_list(my_list))

