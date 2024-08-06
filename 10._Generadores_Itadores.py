#Iterador: Permite recorrer elementos de colección.
'''
*Para crear un iterador se usa función iter()
*Para obtener siguiente elemento se usa funcion next()
'''
"Crear lista"
lista=[1,2,3,4,5]
"Obtener iterador de la lista"
iterador=iter(lista)
"Usar el iterador para obtener elementos"
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
#Intentar obtener otro elemento despues de finalizar iteración:
"print(next(iterador)) Genera excepción StopIteration"

#Iterar a traves de cadenas texto:
text="Hola miguel"
iter_text =iter(text)
for text in iter_text:
    print(text)

#Crear iterador con range para número impares
"Funcion range, se puede usar para recorrer número impares"

"Crear iterador para número impares hasta 10"
limite = 10
iterador_impares = iter(range(1,limite +1,2))#Empieza en 1, hasta limite +1, con paso 2
"Iterar a traves de los números impares"
for numero in iterador_impares:
    print(numero)

"Para número pares se cambio el inicio"
iterador_pares = iter(range(0,limite+1,2))
for numero in iterador_pares:
    print(numero)

#Generador: Función q produce secuencia de valores para iterar. Usando palabra "yeid" en lugar de "return"
def mi_generador():
    yield 1
    yield 2
    yield 3

"Usar el generador"
for valor in mi_generador():
    print(valor)

"Generador para serie Fibonacci"
def fibonacci(limite):
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, a + b

# Usar el generador para la serie de Fibonacci hasta 10
for numero in fibonacci(10):
    print(numero)



