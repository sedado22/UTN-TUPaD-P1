######################################################
## Trabajo Practico 4 - Estructuras Repetitivas     ##
######################################################

####Ejercicio 1

for i in range(0, 101):
    print(i)
    
####Ejercicio 2

numero = int(input("Ingresa un numero entero: "))

# Solo numeros positivos
n = abs(numero)
contador = 0

# evito que el 0 no me devuelva digitos
if n == 0:
    contador = 1
else:
    while n > 0:
        #hago la division por 10 para obtener los digitos incrementando el contador
        n //= 10  
        contador += 1

print(f"El numero tiene {contador} digito(s).")

####Ejercicio 3

# Pido los dos valores
inicio = int(input("Ingresa el primer numero (inicio): "))
fin = int(input("Ingresa el segundo numero (fin): "))

# Inicializo la suma
suma = 0

# Uso un ciclo for para realizar la suma entre dos variables excluyendolos
for i in range(inicio + 1, fin):
    suma += i

# Imprimo el resultado
print(f"La suma de los numeros entre {inicio} y {fin}, excluyendolos, es: {suma}")


####Ejercicio 4

# Inicializo la variable
suma_total = 0

# Bucle para ingresar los numeros
while True:
    numero = int(input("Ingresa un numero entero (0 para terminar): "))
    
    # Si el numero ingresado es 0, termino el bucle
    if numero == 0:
        break
    
    # Sumo el numero ingresado a la suma total
    suma_total += numero

# Muestro el resultado acumulado
print(f"El total acumulado es: {suma_total}")


####Ejercicio 5

#importo la libreria random
import random

# Genero un numero aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

# Inicializo el contador de intentos
intentos = 0

# Bucle para el input
while True:
    # Solicitar al usuario que ingrese un número
    adivinanza = int(input("Adivina un numero entre 0 y 9: "))
    
    # Incremento el contador de intentos
    intentos += 1
    
    # Verifico si la adivinanza es correcta
    if adivinanza == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el numero en {intentos} intento(s).")
        break
    elif adivinanza < numero_aleatorio:
        print("El numero es mayor. Intenta nuevamente.")
    else:
        print("El numero es menor. Intenta nuevamente.")



####Ejercicio 6

#uso for e incluyo -1 para que cubra el numero 0 y -2 para que sean numeros pares
for numero in range(100, -1, -2):
    print(numero)
    
    
####Ejercicio 7

# Solicito un numero
numero = int(input("Ingresa un número entero positivo: "))

# Verifico que el numero sea positivo
if numero <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Calculo la suma 
    suma_total = sum(range(numero + 1))

    # Imprimo el resultado
    print(f"La suma de todos los numeros entre 0 y {numero} es: {suma_total}")
    
    
####Ejercicio 8

# Variable para ingresar la cantidad de numeros, se puede modificar
cantidad = 100  

# Inicializo los contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Bucle para leer los numeros
for i in range(cantidad):
    numero = int(input(f"Ingrese el numero {i+1}: "))

    # cuento pares o impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Cuento positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Muestro resultados
print("\nResumen:")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")


####Ejercicio 9

# Variable para ingresar la cantidad de numeros, se puede modificar
cantidad = 100

# Inicializo la suma
suma_total = 0

# Bucle para ingresar los numeros y sumarlos
for i in range(cantidad):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    suma_total += numero

# Calculo la media
media = suma_total / cantidad

# Muestro el resultado
print(f"\nLa media de los {cantidad} numeros ingresados es: {media}")


####Ejercicio 10
# input de numero
numero = int(input("Ingresa un numero entero: "))

# Detecta si es negativo
es_negativo = numero < 0
numero = abs(numero)

# Inicializa el numero invertido en 0 
numero_invertido = 0

# el bucle se repite hasta que "numero" se convierta en 0
while numero != 0:
    #extraigo el ultimo digito
    digito = numero % 10
    #construyo el numero invertido, multiplicandolo por 10 para dejar espacio a la derecha y sumo el digito al final para que se ubique en la nueva posicion                  
    numero_invertido = numero_invertido * 10 + digito 
    #elimino el ultimo digito del numero
    numero //= 10                    

# si es negativo agrego el signo al final 
if es_negativo:
    numero_invertido *= -1

# Muestro el resultado
print(f"El numero invertido es: {numero_invertido}")