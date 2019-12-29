'''
Exercise 7
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''
#I make a regular solution in some lines, not in only one line of code... :(
#I'll try later the one line of code solution...Well I hope so... :(  :)
a = int(input('Type a number: '))
b = int(input('Type a number: '))
c = int(input('Type a number: '))
d = int(input('Type a number: '))
e = int(input('Type a number: '))
f = int(input('Type a number: '))
g = int(input('Type a number: '))
h = int(input('Type a number: '))
my_list = [a, b, c, d,
           e, f, g, h
]
even_list = []
for x in range(0, len(my_list)):
	mod = my_list[x] % 2
	if mod == 0:
		even_list.append(my_list[x])
print('The even elements in your list are: ', even_list)
