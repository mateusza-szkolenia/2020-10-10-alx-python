oferta = [
    { "nazwa" : "ziemniaki", "cena" : 2.0 },
    { "nazwa" : "migdaly", "cena" : 40.00 },
    { "nazwa" : "maka", "cena" : 4.0 },
    { "nazwa" : "ryz", "cena" : 3.5 },
    { "nazwa" : "woda", "cena" : 1.0 },
    { "nazwa" : "cytryny", "cena" : 8.0 }
]

# TUTAJ MA SIE WYPISAC OFERTA SKLEPU
print("###### Oferta: ######")
for produkt in oferta:
    print(f"{produkt['nazwa']:10}: {produkt['cena']:5}")
print()

# pytamy "Co chcesz kupic? "
wybor = input("Co chcesz kupic? ")

# pytamy "Ile kg?"
waga = float( input("Ile kg? ") )

# podajemy cene

for p in oferta:
    if p['nazwa'] == wybor:
        cena = p['cena']

wartosc = waga * cena
print(f"Do zaplaty: {wartosc}")