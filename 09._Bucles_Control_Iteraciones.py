#Bucles y control de Iteraciones:
"1. Iterar lista usando bucle for:"
numbers =[1,2,3,4,5,6]
for  i in numbers:
    print(f"i es igual a:{i}")

"2. Iterar usando range: Permite generar secuencia de números"
''' Se puede especificar el inicio, fin, y el paso'''
for i in range(10):
    print(i)#Va inprimir del 0 al 9

for i in range(3,10):
    print(i)#Inprime del 3 al 9

"3. Uso condicionales dentro del un bucle for"
frutas =["manzana","pera","uva","naranja","tomate"]
for fruta in frutas:
    if fruta =="naranja":
        print(f"La fruta {fruta} fue encontrada")

for fruta in frutas:
    if fruta =="naranja":
        print(f"La fruta {fruta} fue encontrada")
    print(fruta)

"4. Bucle While: Ejecuta código mientras se cumpla la condición"
x = 0
while x<5:
    print(x)
    x+=1
"5. Que hacer para evitar bucles infinitos: modificar condición para que termine"
"6. Uso de BREACK y CONTINUE en bucles"

numeros=[1,2,3,4,5,6,7,8,9]
for i in numeros:
    if i == 3:
        break#Al llegar se detiene
    print(i)#termina al llegar a 3

for i in numeros:
    if i == 3:
        continue#Omite iteración y salta
    print(i)#Omite el 3







