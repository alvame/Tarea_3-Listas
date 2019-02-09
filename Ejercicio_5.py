cantidad = int (input('Cuantas palabras tiene la lista: '))
lista= []
for i in range(cantidad):
    palabra= input('Digite la palabra {}:' .format(i+1))
    lista.append(palabra)
print ('La lista creada es' ,lista)

cantidad2 = int (input('Cuantas palabras tiene la lista que desea eliminar: '))
lista2= []
for j in range(cantidad2):
    palabra2= input('Digite la palabra {}:' .format(j+1))
    lista2.append(palabra2)
print ('La lista a eliminar es' ,lista2)

lista = [i for i in lista if i not in lista2]

#Otra forma seria crear una nueva lista
# limpia = []
# for i in lista:
#     if i not in lista2:
#         limpia.append(i)

print('Ahora la lista es: ',lista)

