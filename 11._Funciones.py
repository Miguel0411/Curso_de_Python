#Funciones 
"Funciones nos permiten encapsular y reutilizar código, evitando duplicidad"

#Como se definen las funciones:
"Utilizando palabra reservada def"

def saludar():
    print("Hola Miguel")
saludar()

def saltoDeLinea():
    print("")
    print("============================================================")
saltoDeLinea()

#Manejar parametros en una función
def saludar(nombre,apellido):
    print(f"Hola,{nombre} {apellido}")
saludar("Miguel","Luna")
"Si falta algún argumento en la función, se genera un error."
saltoDeLinea()

#Definir valores predeterminadps para parámetros:
def saludar(nombre, apellido,alias="Agente"):
    print(f"Buenos días,{alias} {nombre} {apellido}")
saludar("Miguel","Luna")
#Pasar parámetros por nombre,permite cambiar orden argumentos
saludar(apellido="Albitres",nombre="Angel")

#Crear Calculadora:
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b
def calculadora():
    while True:
        print("Seleccione una operación")
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Salir")

        opcion =int(input("Ingrese su opción: \n"))

        if opcion == 5:
            print("Saliendo de la calculadora")
            break
        if opcion in [1,2,3,4]:
            num1 = float(input("Ingrese el primer número: "))   
            num2 = float(input("Ingrese el segundo número: "))   
            
            if opcion==1:
                print("La suma es: ",suma(num1,num2))
            elif opcion ==2:
                    print("La resta es: ",resta(num1,num2))
            elif opcion ==3:
                    print("La multiplicacion es: ",multiplicar(num1,num2))
            elif opcion ==4:
                if ((num1>=num2)or(num2>num1))and(num2!=0):
                    print("La división es: ",dividir(num1,num2))
                elif (num2==0):
                    print("El divisor es 0, vuelve a intentar")
        else:    
            print("Opción no válida, intenta de nuevo")

calculadora()








