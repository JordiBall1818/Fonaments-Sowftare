compte_actiu = True
contrasenya_correcta = True
codi_correcte = True
dispositiu_de_confiança = False
compte_bloquejat = False
accés_permes = compte_actiu and contrasenya_correcta and not compte_bloquejat and (codi_correcte or dispositiu_de_confiança)
print(f"accés_permes = {accés_permes}")