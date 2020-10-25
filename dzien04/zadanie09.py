import sys

oferta = [
    { "nazwa" : "ziemniaki", "cena" : 2.0 },
    { "nazwa" : "migdaly", "cena" : 40.00 },
    { "nazwa" : "maka", "cena" : 4.0 },
    { "nazwa" : "ryz", "cena" : 3.5 },
    { "nazwa" : "woda", "cena" : 1.0 },
    { "nazwa" : "cytryny", "cena" : 8.0 },
    { "nazwa" : "wodka", "cena" : 30.0 }
]

# TUTAJ MA SIE WYPISAC OFERTA SKLEPU
print("###### Oferta: ######")
for produkt in oferta:
    print(f"{produkt['nazwa']:10}: {produkt['cena']:5}")
print()

# pytamy "Co chcesz kupic? "
wybor = input("Co chcesz kupic? ")

# sprawdzenie, czy w ogole taki produkt jest w sklepie

if len( [ None for p in oferta if p['nazwa'] == wybor ] ) == 0:
    print("Brak produktu w sklepie")
    sys.exit()

# pytamy "Ile kg?"
waga = float( input("Ile kg? ") )

# podajemy cene

# filtrujemy liste w poszukiwaniu produktu o wybranej nazwie
#print( [ p for p in oferta if p['nazwa'] == wybor ] )

# wyciagamy pierwszy z nich (numer 0)
#print( [ p for p in oferta if p['nazwa'] == wybor ][0] )

# wyciagamy pierwszy z nich (numer 0) a nastepnie jego pole "cena"
# print( [ p for p in oferta if p['nazwa'] == wybor ][0]["cena"] )

cena = [ p for p in oferta if p['nazwa'] == wybor ][0]["cena"]

# alternatywne podejscie, daje ten sam wynik
# cena = [ p['cena'] for p in oferta if p['nazwa'] == wybor ][0]

wartosc = waga * cena
print(f"Do zaplaty: {wartosc}")