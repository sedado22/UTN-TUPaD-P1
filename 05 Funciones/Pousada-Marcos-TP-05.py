######################################################
## Trabajo Practico 5 - Funciones                   ##
######################################################

####Ejercicio 1

#Funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()

####Ejercicio 2

# Funcion
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_usuario = input("Ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

####Ejercicio 3

# Funcion
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

####Ejercicio 4

# Importo libreria para usar pi
import math 

# Funcion para calcular el area del circulo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Funcion para calcular el perimetro del circulo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

####Ejercicio 5

# Funcion para convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600  

# Programa principal
segundos = float(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas} horas.")

####Ejercicio 6

# Funcion
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

####Ejercicio 7

# Funcion operaciones basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
# Condicion para las divisiones por cero
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (division por cero)"

    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))

# Llamo a la funcion
resultados = operaciones_basicas(a, b)

# Muestro resultados organizados
print(f"\nResultados para a = {a} y b = {b}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

####Ejercicio 8

# Funcion IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

####Ejercicio 9

# Funcion convertir C a F
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")

####Ejercicio 10

# Funcion para calcular el promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")