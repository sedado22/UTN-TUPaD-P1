######################################################
## Trabajo Practico 3 - Estructuras Condicionales   ##
######################################################


####Ejercicio 1

edad = int(input("Ingresa tu edad: "))

if edad > 18:
    print("Es mayor de edad")
    
####Ejercicio 2

nota = float(input("Ingresa tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

####Ejercicio 3
numero = int(input("Ingresa un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

####Ejercicio 4
edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

####Ejercicio 5
contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

####Ejercicio 6
import random
from statistics import mean, median, mode

# Genero la lista de 50 numeros aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculo estadisticas
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Muestro valores
print("Lista de numeros:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Aplico condicionales para comparar
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Sin clasificar")

####Ejercicio 7

frase = input("Ingresa una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
    
print(frase)

####Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("Elija una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la Primera Letra en Mayúscula")

opcion = input("Ingrese una opción (1, 2 o 3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida.")
    
####Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
    
    
####Ejercicio 10

hemisferio = input("¿En que hemisferio te encontras? (N/S): ").upper()
mes = int(input("¿En que mes estamos? (1-12): "))
dia = int(input("¿Que dia es? (1-31): "))

# Convierto mes y dia a un solo numero
fecha = (mes, dia)

if (fecha >= (12, 21) or fecha <= (3, 20)):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (fecha >= (3, 21) and fecha <= (6, 20)):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (fecha >= (6, 21) and fecha <= (9, 20)):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (fecha >= (9, 21) and fecha <= (12, 20)):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = "Desconocida"
    estacion_sur = "Desconocida"

# Mostrar estación según hemisferio
if hemisferio == "N":
    print("Estas en", estacion_norte)
elif hemisferio == "S":
    print("Estas en", estacion_sur)
else:
    print("Hemisferio no valido. Ingresa 'N' o 'S'.")