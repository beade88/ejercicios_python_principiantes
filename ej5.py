#Este esta implementado con python3 desde el inicio :D
print("Lista 1")
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))
d = int(input("Ingrese un numero: "))
e = int(input("Ingrese un numero: "))
f = int(input("Ingrese un numero: "))
lista1 = [a, b, c, d, e, f]
print("La lista 1 es: ")
print(lista1)
print("Lista 2")
g = int(input("Ingrese un numero: "))
h = int(input("Ingrese un numero: "))
i = int(input("Ingrese un numero: "))
j = int(input("Ingrese un numero: "))
k = int(input("Ingrese un numero: "))
lista2 = [g, h, i, j, k]
print("La lista 2 es: ")
print(lista2)
lista3 = []
print("Los numeros que coinciden en ambas listas son: ")
for x in lista2 :
	if x in lista1 :
		lista3.append(x)
print(lista3)
