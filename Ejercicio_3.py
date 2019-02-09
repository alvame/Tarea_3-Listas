cantidad = int (input('Cuantas palabras tiene la lista: '))
lista= []
for i in range(cantidad):
    palabra= input('Digite la palabra {}:' .format(i+1))
    lista.append(palabra)

print ('La lista creada es' ,lista)

buscar = input('Cual es la palabra que desea sustituir: ')
#contar = lista.count(buscar)

nueva = input('Cual es la nueva palabra ')

for i in range(len(lista)):
    if buscar==lista[i]:
        lista[i]= nueva


print('Ahora la lista es: ',lista)

