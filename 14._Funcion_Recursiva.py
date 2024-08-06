#Recursividad:
'''Una función se llama a sí misma para resolver problemas
complejos de manera más sencilla y estructurada'''
#Ejemplo factorial:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
n =5
print(f"El factorial de los primeros {n} números naturales es: {factorial(n)}")

'''
del factorial(n): función con argumento.
if n==0:
    return 1 : El caso de factorial de 0, es igual a 1
else: return n*factorial(n-1): 
    Si n no es 0, la función calcula el factorial de n 
    multiplicando n por el factorial de n - 1. Esto se 
    hace mediante una llamada recursiva a factorial(n - 1).'''

#Sumatoria de números naturales:
def sumatoria(n):
    if n==0:
        return 0
    else:
        return n + sumatoria(n-1)
n =5
print(f"La sumatoria de los {n} primeros numeros es: {sumatoria(n)}")





