'''
Exercise 4
Create a program that asks the user for a number and then prints out a list
of all the divisors of that number. (If you dont know what a divisor is,
it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
# use print()
print('In the following software you type a number and them we show you a list of  all the divisors of that number')
# English please
a = int(input("Type a number: "))
my_list = range(1, a+1)  # PEP8 here please range(1, a + 1)
divisors_list = [] # English here please
for x in my_list : 
	if a % x == 0:
		divisors_list.append(x)
print('Your number divisors are: ')
print(divisors_list)

# Good!!!! just use English please and be careful with PEP8
