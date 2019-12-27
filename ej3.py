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

