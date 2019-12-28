'''
Exercise 3

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''
print "Vamos a elaborar una lista. Para ello le pediremos que ingrese 10 numeros"
print "De los numeros ingresados le mostraremos los menores que 5"
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
print "De los numeros ingresados, los menores que 5 son: "
for x in my_list :
	if x < 5 :
  		print(x)
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "                                                                                                                   "
print "Ahora le solicitaremos un numero y le mostraremos los elementos de su lista inicial menores que el numero ingresado"
y = input ("Ingrese un numero: ")
print "De su lista inicial, los numeros menores que el numero ingresado son: "
for z in my_list :
	if z < y :
		print(z)

