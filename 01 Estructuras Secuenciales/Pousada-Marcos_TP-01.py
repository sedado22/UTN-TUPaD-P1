# 1
print("Hola Mundo!")

# 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4. 
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.1416
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El área es {area:.2f} y el perímetro es {perimetro:.2f}.")

# 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas:.2f} horas.")

# 6
tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

# 7.
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
while num1 == 0 or num2 == 0:
    print("Los números deben ser distintos de 0.")
    num1 = int(input("Ingrese el primer número (distinto de 0): "))
    num2 = int(input("Ingrese el segundo número (distinto de 0): "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2:.2f}")

# 8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es {imc:.2f}.")

# 9
temp_celsius = float(input("Ingrese la temperatura en Celsius: "))
temp_fahrenheit = (9/5) * temp_celsius + 32
print(f"La temperatura en Fahrenheit es {temp_fahrenheit:.2f}.")

# 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es {promedio:.2f}.")