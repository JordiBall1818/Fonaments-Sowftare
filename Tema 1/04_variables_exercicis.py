###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom, ubicacio, ports, ences = input("Introdueix el nom d'un encaminador, la seva ubicació, el nombre de ports que té i si está encés (separa amb una , + espai): ").split(", ")
print(f"El nom de l'encaminador és {nom}, està ubicat a {ubicacio}, té {ports} ports y {ences} està encés.")
# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
GB_pla_de_dades, GB_consumits = map(float, input("Introdueix els GB d'un pla de dades i els GB compartits:").split(", "))

print(f"Queden {GB_pla_de_dades-GB_consumits}")
GB_consumits = float(input("Actualitza el consum amb un valor nou"))
print(f"Queden {GB_pla_de_dades-GB_consumits}")