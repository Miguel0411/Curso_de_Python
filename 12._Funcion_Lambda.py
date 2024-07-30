#Funcion Lambda
'''No se necesita especificar el nombre de la función
Solo se requiere parámetros y la operación deseada.'''
sumar = lambda a,b: 3+4
print(sumar(10,4))

multiplicar= lambda a,b:a*b
print(multiplicar(10,4))

#Aplicar lambda a elementos de una lista con map
'''Cuando trabajamos con listas y queremos aplicar 
una función a cada elemento, map es útil junto con 
lambda '''

numeros = list(range(11))
cuadrados = list(map(lambda x:x**2,numeros))
print("Cuadrados: ",cuadrados)
'''
range: genera secuencia de números del 0 al 10
list: Convierte secuencia en lista
x**2: Elevar al cuadrado
map:devuelve objeto iterador aplica la funcion lambda a cada elemento de lista numeros
list: convierte ese iterador en una lista
'''
