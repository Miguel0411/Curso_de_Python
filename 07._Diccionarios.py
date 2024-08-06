'''Son una estructura que almacena dos datos: 
La clave y el valor.
Los diccionarios se usan mucho para guardar Datos o registros'''
#Para crear utilizamos variables y llaves{}
numbers ={1:'one',
          2:'two',
          3:'three'}
print(numbers)

#Accedemos a sus elementos mediante indexación:
print(numbers[2])

numbers2 ={1:'uno','2':'dos'}
print(numbers2['2'])

#Eliminar elementos de un diccionario:
del numbers2[1]
print(numbers2)

#Métodos para trabajar con Diccionarios:
numbers3= {1:'uno',2:'dos',3:'tres',4:'cuatro'}

# Obtener las claves
claves = numbers3.keys()
print(claves)
print(type(claves))
# Obtener los valores
valores = numbers3.values()
print(valores)
print(type(valores))
# Obtener los pares clave-valor
pares = numbers3.items()
print(pares)
print(type(pares))










