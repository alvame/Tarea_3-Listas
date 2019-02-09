cantidad = int (input('Cuantas palabras tiene la lista: '))
lista= []
for i in range(cantidad):
    palabra= input('Digite la palabra {}:' .format(i+1))
    lista.append(palabra)
print ('La lista creada es' ,lista)
limpia = []
for i in lista:
 if i not in limpia:
     limpia.append(i)
#lista= list(set(lista))
print('Ahora la lista es: ',limpia)