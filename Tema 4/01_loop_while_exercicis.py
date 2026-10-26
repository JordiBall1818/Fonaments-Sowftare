###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
comptador = 1
while comptador <= 10:
    print(f"{comptador}")
    comptador += 1
# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
comptador_parells = 0
comptador = 1
while comptador <= 20:
    if comptador %2 == 0:
        comptador_parells += comptador
    comptador += 1
print(f"La suma de parells del 1 al 20 és: {comptador_parells}")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
enter = int(input("Introdueix un enter per calcular el seu factorial: "))
comptador = 1
factorial = 1
while comptador <= enter:
    factorial *= comptador
    comptador += 1
print(f"El factorial de {enter} és: {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contrasenya = ""
while len(contrasenya) < 8:
    contrasenya = input("Introdueix una contrasenya de al menys 8 caràcters: ")
    if len(contrasenya) < 8:
        print("La contrasenya és invàlida.")
print("La contrasenya és vàlida.")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
taula = int(input("Introdueix un número: "))
multiplicador = 1
while multiplicador <= 10:
  resultat = taula * multiplicador
  print(f"{taula} x {multiplicador} = {resultat}")
  multiplicador += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
n = int(input("Introdueix un enter positiu: "))
numero = 2
while numero <= n:
    primo = True
    divisor = 2
    while divisor * divisor < numero == 0:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1
    if primo:
        print(numero)
    numero += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
suma = 0
num = None
while num != 0:
    num = int(input("Introdueix nombres enters: "))
    if num != 0:
        suma += num
print(f"La suma és {suma}")
# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
num = int(input("Introdueix un nombre enter positiu: "))
if num == 0:
    nombre_xifres = 1
else:
    while num > 0:
        num = num//10
        nombre_xifres += 1
print(f"El nombre introduït té {nombre_xifres}.")
# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
termes = int(input("Introdueix el nombre de termes que vols de la seqüència Fibonacci: "))
anterior = 0
fibonacci = 1
comptador = 0
while comptador < termes:
    print(anterior)  # Mostrem el terme actual
    anterior, fibonacci = fibonacci, anterior + fibonacci
    comptador += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
numero_secret = 7
intent = None
while intent != numero_secret:
    intent = int(input("Endevina el número secret: "))
    if intent < numero_secret:
        print("El número secret és més gran.")
    elif intent > numero_secret:
        print("El número secret és més petit.")
    else:
        print("Molt bé! Has encertat el número!")