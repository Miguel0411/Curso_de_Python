#Estructuras condicionales 
"Al usar IF, se verifica si una variable cumpla con una condición especifica"
x = 10
if x > 5:
    print("x es mayor que 5")

"Si condición es falsa: Uso ELSE"
x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5")

"Multiples condiciones: else if (elif)"
x = 5
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")

"Multiples condiciones en un solo if: Utilizar operadores (and y or)"
x = 15
y = 30
if x > 10 and y > 25:
    print("x es mayor que 10 y y es mayor que 25")
if x > 10 or y > 35:
    print("x es mayor que 10 o y es mayor que 35")

"Negación de las condiciones: negar condición (not)"
x = 15
if not (x > 20):
    print("x no es mayor que 20")

"Anidación estructuras if"
'''Los IF anidados permiten evaluar condiciones 
dentro de otras condiciones. Esto es útil para 
verificar múltiples niveles de requisitos.'''
isMember = True
age = 15
if isMember:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y mayor que 15")
    else:
        print("No tienes acceso ya que eres miembro, pero menor a 15 años")
else:
    print("No eres miembro y no tienes acceso")


