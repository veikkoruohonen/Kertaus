tuntipalkka = float(input("Tuntipalkka: "))
tunnit = float(input("Tehdyt tunnit: "))
paiva = input("Viikonpäivä: ").strip().lower()

if paiva == "sunnuntai":
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print(f"Päiväpalkka: {paivapalkka} euroa")