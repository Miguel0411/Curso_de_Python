'''Para evitar que dos listas apunten al mismo espacio de memorias,
se usa el método SLICE, esto permite crear una copia superficial de la lista original.
A= [1,2,3,4,5]
B= A[:]
Verificamos los IDs: print(id(A)), print(id(B))'''
A= [1,2,3,4,5]
B=A[:]
print(id(A))
print(id(B))
#Eliminar una posición en A:
del A[0]

#Verificar ambas listas:
print(A)
print(B)

#Agregar un valor en la lista A:
A.append(6)
print(A)
print(B)
print(id(A))
print(id(B))


#Otra forma :
lista1 = [1,2,3,4,5]
lista2 = lista1.copy()

lista2.append( 6 )

print( lista1 )
print( lista2 )
print(id(lista1))
print(id(lista2))

