'''
Exercise 4
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
print "En el siguiente programa le solicitaremos que ingrese un numero y luego le mostraremos los numeros que son divisibles por el numero ingresado"
a = int(input("Ingrese un numero: "))
my_list = range(1, a+1)
lista_divisores = []
for x in my_list : 
	if a % x == 0:
		lista_divisores.append(x)
print "Su numero es divisible por: "
print lista_divisores
