cantidad = int (input('Cuantas palabras tiene la primera lista: '))
lista= []
for i in range(cantidad):
    palabra= input('Digite la palabra {}:' .format(i+1))
    lista.append(palabra)

print ('La primera lista creada es' ,lista)

cantidad2 = int (input('Cuantas palabras tiene la segunda lista '))
lista2= []
for j in range(cantidad2):
    palabra2= input('Digite la palabra {}:' .format(j+1))
    lista2.append(palabra2)

print ('La segunda lista creada es ' ,lista2)

#eliminar duplicados de cada lista
lista= list(set(lista))
lista2 = list (set(lista2))

#Lista de palabras que aparecen en las dos listas
duplicados=[]
for i in lista:
    if i in lista2:
        duplicados.append(i)
print('Las palabras que aparece en las dos listas' , duplicados)


# palabras que aparece en la primera lista pero no en la segunda
primera=[]
for i in lista:
    if i not in lista2:
        primera.append(i)
print('Las palabras que aparece en la primera lista pero no en la segunda ' , primera)

#Lista de palabras que aparecen en la segunda lista, pero no en la primera
segunda=[]
for i in lista2:
    if i not in lista:
        segunda.append(i)
print('Las palabras que aparece en la segunda lista pero no en la primera ' ,segunda)


#Lista de palabras que aparecen en ambas listas
ambas=[]
ambas =lista + lista2
ambas=list (set(ambas))
print('Las palabras que aparece en ambas listas ' ,ambas)








