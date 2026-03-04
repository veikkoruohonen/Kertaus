nimi = input("Kerro nimesi: ")

if nimi == "Matti":
    print("Seuraava, kiitos!")
else:
    annokset = int(input("Montako keittoannosta? "))
    hinta = annokset * 5.90
    print(f"Kokonaishinta on {hinta}")
    print("Seuraava, kiitos!")
