print "En el siguiente programa le solicitaremos que ingrese un numero y luego le mostraremos los numeros que son divisibles por el numero ingresado"
a = int(input("Ingrese un numero: "))
my_list = range(1, a+1)
lista_divisores = []
for x in my_list : 
	if a % x == 0:
		lista_divisores.append(x)
print "Su numero es divisible por: "
print lista_divisores
