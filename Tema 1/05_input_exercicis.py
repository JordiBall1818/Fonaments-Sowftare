###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tecnic, xarxa = input("Introdueix el nom d'un técnic i de la xarxa que esà instalant: ").split(", ")
print(f"El nom del tècnic és {tecnic} i està instalant la xarxa {xarxa}.")
# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud, velocitat = map(float, input("Intodueix la longitud en km d'un enllaç de fibra i la velocitat de transmissió en Gbps: ").split(", "))
print(f"Els segons que tardaría en transmetre 1GB de dades serían {velocitat/8} ")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores, preu_hora, preu_material = map(float, input("Introdueix el nombre d'hores de feina, el preu per hora d'una instal·lació de xarxa i el del material<: ").split(", "))
print(f"El cost total és: {hores*preu_hora+preu_material}")