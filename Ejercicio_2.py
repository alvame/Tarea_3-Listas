cantidad = int (input('Cuantas palabras tiene la lista: '))
lista= []
for i in range(cantidad):
    palabra= input('Digite la palabra {}:' .format(i+1))
    lista.append(palabra)

print ('La lista creada es' ,lista)
buscar = input('Cual es la palabra que desea buscar: ')
contar = lista.count(buscar)

if buscar in lista:
    print('La palabra ' ,buscar, 'aparece ', contar, 'veces en la lista')
else:
    print('La palabra', buscar, ' no aparece en la lista')