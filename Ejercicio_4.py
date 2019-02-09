cantidad = int (input('Cuantas palabras tiene la lista: '))
lista= []
for i in range(cantidad):
    palabra= input('Digite la palabra {}:' .format(i+1))
    lista.append(palabra)
print ('La lista creada es' ,lista)

buscar = input('Cual es la palabra que desea eliminar: ')

for i in range(len(lista)):
    if buscar in lista:
     lista.remove(buscar)

print('Ahora la lista es: ',lista)