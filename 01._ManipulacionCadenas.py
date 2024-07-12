name = "Miguel"
comillas_triples = '''Comillas
sensibles al
salto de línea'''
numero = 20
#Tipo de DATO (TYPE)
print(type(name))
print(type(numero))
print(comillas_triples)
print(type(comillas_triples))
print('============================================================')

#Uso de corchetes para ver posición:
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print('============================================================')

#Concatenación de Cadenas
name_2 = 'Angel'
apellido = 'Luna'
print(name_2 + apellido)
print(name_2 + ' ' +apellido)
print(name_2,apellido)#Se añade coma
#Replicación:
print(5*(name_2+' '))
print('============================================================')

#Consultar Longitud(LEN), empieza de 1
print(len(name_2))
print(len(apellido))
print('============================================================')

#Métodos STRING van luego de un punto(.) y el método con ():
#Método LOWER(poner todo a minusculas)
print(name_2.lower())

#Método UPPER (poner todo a mayusculas)
print(name_2.upper())

#Método STRIP (elimina los espacios del comienzo y final)
name_3 = '  hola  mundo   '
print(name_3)
print(name_3.strip())




