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
print(f"El cost total és de {total}")