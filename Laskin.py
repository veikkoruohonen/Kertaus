while True:
    print("\nValitse toiminto:")
    print("1 = yhteenlasku (+)")
    print("2 = vähennyslasku (-)")
    print("3 = kertolasku (*)")
    print("4 = jakolasku (/)")
    print("0 = lopeta")

    valinta = input("Valinta: ").strip()

    if valinta == "0":
        print("Lopetetaan.")
        break

    if valinta in ("1", "2", "3", "4"):
        a = float(input("Anna ensimmäinen luku: "))
        b = float(input("Anna toinen luku: "))

        if valinta == "1":
            print(f"Tulos: {a + b}")
        elif valinta == "2":
            print(f"Tulos: {a - b}")
        elif valinta == "3":
            print(f"Tulos: {a * b}")
        else:  # valinta == "4"
            if b == 0:
                print("Nollalla ei voi jakaa.")
            else:
                print(f"Tulos: {a / b}")
    else:
        print("Virheellinen valinta, yritä uudelleen.")