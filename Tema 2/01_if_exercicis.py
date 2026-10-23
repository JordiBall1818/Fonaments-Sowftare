###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
num1, num2 = map(float, input("Introdueix dos noms: ").split(", "))
if num1 == num2:
    print("Els dos nombres son iguals")
elif num1>num2:
    print(f"{num1} és més gran que {num2}")
else:
    print(f"{num2} és més gran que {num1}")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
num1, num2 = map(float, input("Introdueix dos noms: ").split(", "))
operacion = input("Introdueix una operació (+,-,*,/):")

if operacion == "+":
    num3 = num1 + num2
elif operacion == "-":
    num3 = num1 - num2
elif operacion == "*":
    num3 = num1 * num2
elif operacion == "/":
    if num2==0:
        print("No es pot dividir per 0")
    else:
        num3 = num1 / num2
print(f"El resultat és {num3}")    

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
any = int(input("Introdueix un any: "))
if(any % 4  == 0 and any % 100 != 100) or any % 400 == 0:
     print(f"L'any {any} és de traspàs")
else:
     print(f"L'any {any} no és de traspàs")
# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
edat = int(input("Introdueix una edat: "))
if edat >= 0 and edat <= 2:
    print(f"L'edat de {edat}, correspon a un nadó.")
elif edat >= 3 and edat <= 12:
    print(f"L'edat de {edat}, correspon a un infant.")
elif edat >= 13 and edat <= 17:
    print(f"L'edat de {edat}, correspon a un adolescent.")
elif edat >= 18 and edat <= 64:
    print(f"L'edat de {edat}, correspon a un adult.")
elif edat >= 65:
    print(f"L'edat de {edat}, correspon a una persona gran.")
else:
    print(f"L'edat {edat} no és vàlida.")
# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
nivell_senyal = float(input("Introdueix el nivell del senyal rebut (dbm): "))
if nivell_senyal >= -50:
    print("La senyal és excel·lent.")
elif nivell_senyal >= -67 and nivell_senyal < 50:
    print("La senyal és bona.")
elif nivell_senyal >= -75 and nivell_senyal < -67:
    print("La senyal és feble.")
elif nivell_senyal <= -75:
    print("La senyal és molt feble.")
else:
    print("S'ha introduït un valor invàlid")
# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
nivell_reparacio = float(input("Introdueix la potència rebuda (dbm): "))
if nivell_reparacio >= -27 and nivell_reparacio <= -8:
    print("El nivell és acceptable.")
elif nivell_reparacio < -27:
    print("El nivell és massa baix.")
else:
    print("El nivell és massa alt.")
# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Introdueix el consum de dades (GB): "))
if consum > 20:
    print(f"El consum ha superat el pla per {consum-20} GB")
else:
    print("El consum està fins del límit: ")
# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los = input("Indica, si l'indicador los està encés (sí/no): ").strip().lower()
router = input("Indica, si l'indicador d'Internet del router està encès (sí/no): ").strip().lower()
if los == "sí" or los == "si":
    print("Cal revisar el cable de la fibra.")
elif router == "no":
    print("No hi ha pèrdua física de senyal, es nescessari revisar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
sai = float(input("Introdueix el percentatge de bateria disponible al SAI: "))
if sai < 100 and sai > 0:
    if sai < 20:
        print("El nivell de la bateria és crític.")
    if sai >= 20 and sai <= 49:
         print("El nivell de la bateria és baix.")
    if sai >= 50:
            print("El nivell de la bateria és suficient.") 
else:
    print("Fora de rang.")  

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
latencia, paquets_percentatge = map(float, input("Introdueix la latència (ms) i el percentatge de paquets perduts: ").split(", "))
if latencia < 0 or (paquets_percentatge < 0 or paquets_percentatge > 100):
    print("Valors incorrectes.")
elif latencia <= 30 and paquets_percentatge <= 1:
    print("La connexió és excel·lent.")
elif latencia <= 80 and paquets_percentatge <= 3:
    print("La connexió és bona.")
elif latencia <= 150 and paquets_percentatge <= 5:
    print("La connexió és acceptable.")
else:
    print("La connexió és deficient.")
# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
pla = input("Introdueix el tipus de pla (bàsic o plus): ").strip().lower()
consum = float(input("Introdueix el consum mensual (GB): "))
if consum < 0 or pla not in ("bàsic", "basic", "plus"):
    print("Opció incorrecte.")
else:
    if pla in ("bàsic", "basic"):
        if consum >= 10:
            total = 10 + (consum-10) * 1.5
        else:
            total = 10
    else:
        if consum >= 30:
            total = 20 + (consum-30) * 0.75
        else:
            total = 20
    print(f"El cost total és de {total: 2.f} €.")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
compte = input("El compte està actiu? (sí/no): ").strip().lower()
if compte not in ("sí", "si"):
    print("Accés denegat: el compte està desactivat.")
else:
    contrasenya = input("La contrasenya és correcta? (sí/no): ").strip().lower()
    if contrasenya not in ("sí", "si"):
        print("Accés denegat: la contrasenya és incorrecta.")
    else:
        codi = input("El codi de doble verificació és correcte? (sí/no): ").strip().lower()
        if codi not in ("sí", "si"):
            print("Accés denegat: falla el codi de doble verificació.")
        else:
            print("Accés permès: totes les comprovacions són correctes.")
# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router_ences = input("El router està encès? (sí/no): ").strip().lower()
if router_ences not in ("sí", "si"):
    print("Cal encendre el router.")
else:
    los = input("L'indicador LOS del terminal òptic està encès? (sí/no): ").strip().lower()
    internet = input("L'indicador d'Internet del router està encès? (sí/no): ").strip().lower()
    if los in ("sí", "si"):
        print("Cal revisar el cable de fibra.")
    elif internet not in ("sí", "si"):
        print("Cal contactar amb el proveïdor.")
    else:
        print("La connexió funciona correctament.")
# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
servei_critic = input("La incidència afecta un servei crític? (sí/no): ").strip().lower()
usuaris = int(input("Introdueix el nombre d'usuaris afectats: "))
alternativa = input("Hi ha una alternativa de connexió disponible? (sí/no): ").strip().lower()
if usuaris < 0:
    print("Error: el nombre d'usuaris no pot ser negatiu.")
else:
    es_critic = servei_critic in ("sí", "si")
    te_alternativa = alternativa in ("sí", "si")
    if (es_critic and not te_alternativa) or (usuaris >= 50 and not te_alternativa):
        print("Prioritat: crítica")
    elif usuaris >= 10 or es_critic:
        print("Prioritat: alta")
    else:
        print("Prioritat: baixa")