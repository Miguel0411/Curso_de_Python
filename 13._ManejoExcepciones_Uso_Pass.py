#Errores y excepeciones:
'''
Errores: Problemas en el código, pueden ser sintácticos(escritura) o 
semánticos(lógica).Se detiene ejeción del programa.
Excepciones: Son eventos que ocurren en ejecuci+on y que alteran flujo normal
del código. Puede ser manejado para evitar el programa se detenga.
'''
#ERRORES BÁSICOS:
#SyntaxError:
"Error en la sintaxis del código"
#TypeError:
"Operación en dato inapropiado,diferentes datos"

#TRY-EXCEPT
'''Se intenta ejecutar bloque de código y atrapar las excepciones.
try: define código donde se anticipa que puede haber error. Si encuentra error
tranfiere control del código a (except)
except: código que se ejecuta por si hay un problema, se maneja error, limpia
el desoren o proporciona mensajes interativos al usuario.
'''
#Estrutura:
'''
try:
    # Código que puede generar una excepción
    pass
except NombreDeLaExcepcion:
    # Código que maneja la excepción
    pass
'''
try:
    valor = int(input("Ingresa un número: "))
    resultado = 10 / valor
    print(f"El resultado es {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")

#Jerarquia de Excepciones:
'''
Exception
    ArithmeticError
        ZeroDivisionError
    ImportError
    LookupError
        IndexError
        KeyError
    RuntimeError
    SyntaxError
        IndentationError
    ValueError
        UnicodeError
    Warning
    ExceptionGroup
'''

#MANEJO GENERAL DE EXCEPCIONES:
try:
    nombre = input("Introduce tu nombre: ")
    print(f"Hola, {nombre}!")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")


#JERARQUIA EXCEPCIONES:
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)

#Uso de PASS
'''Error indentationError, a veces puedo usar pass.
Pass : Es una declaración nula, no hace nada, pero es útil como marcador de posición'''
def mi_funcion():
    pass  # Marcador de posición para el cuerpo de la función

print("Continuando con el código...")