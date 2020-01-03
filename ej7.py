'''
Exercise 7
Lets say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list
that has only the even elements of this list in it.
'''
# I make a regular solution in some lines, not in only one line of code... :(
# I'll try later the one line of code solution...Well I hope so... :(  :)

# Please use for loop to fill the list
my_list = []
for i in range(0, 8):
	my_list.append(int(input('Type a number: ')))
even_list = []
for x in range(0, len(my_list)):
	mod = my_list[x] % 2
	if mod == 0:
		even_list.append(my_list[x])
print('The even elements in your list are: ', even_list)

# Good, very good. Just use a loop to fill the first list (my_list)

# I will help you here, because that is hard even for me.
# This is something I need still to master.
# I dont like because sometimes is harder to read and understand
# but it seems very important because read this kind of code a lot.
# It is called list comprehension. And behaves like this
# [output] for [item] in [list] if [filter]
# look here https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
print('The same list but in one line:')
even_list = [x for x in my_list if x % 2 == 0]
print(even_list)

# Its hard to understand, I know :D, but is something like give me x
# form the list only if the condition is True. And the result ALWAYS is going
# to be a list :D


