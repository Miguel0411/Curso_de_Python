name = "Miguel"
comillas_triples = '''Comillas
sensibles al
salto de línea'''
numero = 20
# Tipo de DATO (TYPE)
print(type(name))
print(type(numero))
print(comillas_triples)
print(type(comillas_triples))
print('============================================================')

# Uso de corchetes para ver posición:
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print('============================================================')

# Concatenación de Cadenas
name_2 = 'Angel'
apellido = 'Luna'
print(name_2 + apellido)
print(name_2 + ' ' + apellido)
print(name_2, apellido)  # Se añade coma
# Replicación:
print(5*(name_2+' '))
print('============================================================')

# Consultar Longitud(LEN), empieza de 1
print(len(name_2))
print(len(apellido))
print('============================================================')

# Métodos STRING van luego de un punto(.) y el método con ():
# Método LOWER(poner todo a minusculas)
print(name_2.lower())

# Método UPPER (poner todo a mayusculas)
print(name_2.upper())

# Método STRIP (elimina los espacios del comienzo y final)
name_3 = '  hola  mundo   '
print(name_3)
print(name_3.strip())

'''Uso parámero SEP:
# El parámetro sep permite especificar cómo separar los elementos al imprimir.'''
print("Nunca", "pares", "de", "aprender", sep="/ ")
# Nunca, pares, de, aprender

'''Uso de END
El parámetro end cambia lo que se imprime al final de la llamada a print.
En lugar de imprimir cada mensaje en una nueva línea, end="" asegura que
“Nunca” y “pares de aprender” se impriman en la misma línea, resultando en “Nunca pares de aprender”. 
Por defecto, end es un salto de línea ("\n"), lo que hace que cada llamada 
a print comience en una nueva línea.'''
print("Nunca", end=" ")
print("pares de aprender")
# Nunca pares de aprender

'''Uso de formato con F-STRING
Las f-strings permiten insertar expresiones dentro de cadenas de texto. 
Al anteponer una f a la cadena de texto, puedes incluir variables directamente 
dentro de las llaves {}. En este ejemplo, frase y author se insertarán 
en la cadena, resultando en “Frase: Nunca pares de aprender, Autor: Miguel". 
Esto hace que el código sea más legible y fácil de escribir.'''
frase = "Nunca pares de aprender"
author = "Miguel"
print(f"Frase: {frase}, Autor: {author}")
# Frase: Nunca pares de aprender, Autor: Miguel

'''Uso de formato con FORMAT
El método format es otra forma de insertar valores en cadenas de texto. 
Usando {} como marcadores de posición, puedes pasar los valores que quieres 
insertar como argumentos de format. En este ejemplo, se imprimirá 
“Frase: Nunca pares de aprender, Autor: Miguel". 
Es una forma flexible y poderosa de formatear cadenas, aunque las f-strings 
son más concisas.'''
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author))
# Frase: Nunca pares de aprender, Autor: Miguel

'''Impresión con formato específico
Puedes controlar el formato de los números al imprimir. 
En este ejemplo, :.2f indica que el número debe mostrarse con dos decimales. 
Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales.'''
valor = 3.14159
print("Valor: {:.2f}".format(valor))
# Valor: 3.14

'''Saltos de línea'''
print("Hola\nmundo")
# Hola
# mundo

'''Comillas dentro'''
print('Hola soy \'Miguel\' , mucho gusto')
# Hola soy 'Miguel' , mucho gusto
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
# La ruta de archivo es: C:\Users\Usuario\Desktop\archivo.txt
