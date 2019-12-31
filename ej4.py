'''
Exercise 4
Create a program that asks the user for a number and then prints out a list
of all the divisors of that number. (If you dont know what a divisor is,
it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
# use print()
print "En el siguiente programa le solicitaremos que ingrese un numero y luego le mostraremos los numeros que son divisibles por el numero ingresado"
# English please
a = int(input("Ingrese un numero: "))
my_list = range(1, a+1)  # PEP8 here please range(1, a + 1)
lista_divisores = [] # English here please
for x in my_list : 
	if a % x == 0:
		lista_divisores.append(x)
print "Su numero es divisible por: "
print lista_divisores

# Good!!!! just use English please and be careful with PEP8
