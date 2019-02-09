cantidad = int (input('Cuantas palabras tiene la lista: '))
lista= []
for i in range(cantidad):
    palabra= input('Digite la palabra {}:' .format(i+1))
    lista.append(palabra)

print ('La lista creada es' ,lista)

nueva_lista= lista[::-1]

print ('La nueva lista inversa es ' ,nueva_lista)