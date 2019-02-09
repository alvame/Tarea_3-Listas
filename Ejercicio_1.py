cantidad = int (input('Cuantas palabras tiene la lista: '))
lista= []
for i in range(cantidad):
    palabra= input('Digite la palabra {}:' .format(i+1))
    lista.append(palabra)

print ('La lista creada es' ,lista)

digitadas = int (input('Cuantas palabras tiene la lista? '))
if (digitadas == len(lista)):
    print('Correcto!!')
else:
    print('Imposible!!')






