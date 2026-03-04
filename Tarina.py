sanat = []

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ").strip()
    if sana.lower() == "loppu":
        break
    sanat.append(sana)

print(" ".join(sanat))