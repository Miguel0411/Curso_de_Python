'''
Las Matrices son Mutables.
Las posiciones en matrices tanto en fila como en columnas, 
empiezan con el 0. Para poder ubicar un elemento en la matriz
debemos buscarlo de acuerdo a la posición que toma tanto en fila
como columna.'''
#Creamos una matriz que queremos que sea una lista de listas:
matrix = [[1,2,3],
          [1,2,3],
          [1,2,3]]
print(matrix)

#Ahora buscamos por posiciones:
print(matrix[0])
#Accedemos por dimensiones:
print(matrix[1][0])
print(matrix[1][2])

#Accedemos Matriz con varias listas:
matrix2= [[[1,2,3],[1,2,3]],
          [[1,2,3],[1,2,3]]]
print(matrix2[1][1][1])

'''Las Tuplas son Inmutables: No se puede hacer modificaciones.'''
numbers=(1,2,3,4,5)#Puede o no tener parentesis.
print(numbers)
print(type(numbers))
#Ingresar por posición:
print(numbers[0])


