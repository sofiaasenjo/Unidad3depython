print("hola mundo")
lista=[1, "Hola", 3.67, [1, 2, 3]]
print(lista)#Esto me muestra la lista completa
print(lista[0])#1
print(lista[1])#Hola
print(lista[2])#3.67
print(lista[3])#[1, 2, 3]

a =[90, "Python", 3.87]
print(a[-1])#Coloca el ultimo numero de la lista
print(a[-2])#Coloca el penultimo numero o palabra de la lista
print(a[-3])#Al colocar el "-" esto hace que te lo muestra alrevez, en vez de colocarlo de izquierda a derecha, se muestra de derecha a izquierda

#print("Lista 2")
#lista_2 =[1,2, ["a", "b", "c"]]
#sublista=lista[2]
#print(sublista[1])

print("Lista 3")
lista_3 = [1, 2]
lista_3.append(3)
print(lista_3)#1, 2, 3 Esto hace qu8e se agrege un numero mas a la lista

print("Lista 4")
lista_4 =[1, 2]
lista_4.extend([3, 4])
print(lista_4)#1, 2, 3, 4 permite añadir una lista a otra lista

print("Lista 5")
lista_5 = [1, 3]
lista_5.insert(2, "casa")
print(lista_5)# permite añadir un elemento en una posicion determinada, el primer numero dice en que posicion y el segundo para decir que poner

print("lista 6")
lista_6 = [1, 2 , 3, "ultimo"]
lista_6.remove(2)
print(lista_6)#Este sirve para remover un elemento, hay que colocar el numero o palabra exacta que quieres remover

print("Lista 7 1.1")
lista_7= [1, 2, 3]
lista_7.pop()
print(lista_7)#Este elimina el ultimo objeto de la lista

#print("Lista 7 1.2")
#lista_8 =[1, 2, 3]
#lista_8.pop(1)
#print(lista_8)

print("Lista 9")
lista_9 = [1, 2, 3]
lista_9.reverse()
print(lista_9)#Esto hace que te muestra la lista al reves,ejem: [1, 2, 3] lo transforma a [3, 2, 1]

print("Lista_a")
lista_a =[1, 2, 3, 4, "ultimo"]
lista_numerica=[11, 3, 7, 2, 8]
lista_numerica.sort()
print(lista_numerica)#Esto hace que te ordena la lista de texto de menor a mayor(sirve para ordenar los numeros)


print("Lista_b")
lista_b =[1, 2, 3, 4, "ultimo"]
lista_letra=[11, 3, 7, 2, 8]
lista_letra.sort()
print(lista_letra)#cambiarlo por leytra y te lo ordena ñlos orden alfabetico

print("lista c")


#a = [12, "Python", 3.1416]
#print(a[0])#12
#print(a[1])#python
#print(a[2])#3.1416