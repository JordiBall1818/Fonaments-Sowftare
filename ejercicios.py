###
# ejercicios.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Jordi\nBarcelona")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print(int(12345))
print(int(3.99))
#El 3.99 es torna un 3 ya que s'extreuen els seus decimals
print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo Marc y tengo 38 años, mido 1.75 metros"
#name = "Marc"
#age = 38

### Completa aquí
nom = "Jordi"
edat = 19
altura = 1.72
print(f"Hola! Me llamo {nom} y tengo {edat} años, mido {altura} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

PI=3.14
print((round(PI))//2)
print("--------------")

print("\nEjercicio 6: Conversor de temperatura")
print("Pide al usuario una temperatura en grados Celsius.")
print("Convierte ese valor a Fahrenheit con la fórmula: F = (C * 9/5) + 32")
print("Muestra ambos valores con un mensaje claro.")

### Completa aquí
tempC = float(input("Introdueix una temperatura en Celsius: "))
tempF = (tempC * 9/5) + 32
print(f"La temperatura en Celsius és de {tempC} graus i en Farenheit de {tempF}.")
print("--------------")

print("\nEjercicio 7: Calculadora de propina")
print("Pide el total de una cuenta y el porcentaje de propina.")
print("Calcula cuánto es la propina y el total final a pagar.")
print("Muestra los resultados con 2 decimales.")

### Completa aquí
cuenta_str, propina_str = input("Introduce el total de la cuenta y el porcentaje de propina (separa con , y espacio): ").split(", ")
cuenta = float(cuenta_str)
porcentaje = float(propina_str)
total = cuenta + (porcentaje/100)*cuenta 
propina_fin = (porcentaje/100)*cuenta
print(f"La propina és de {propina_fin} euros y el total és de {total}")

print("--------------")

print("\nEjercicio 8: Validador de contraseña simple")
print("Pide una contraseña al usuario.")
print("Comprueba si tiene al menos 8 caracteres.")
print("Muestra 'Contraseña válida' o 'Contraseña no válida'.")

### Completa aquí