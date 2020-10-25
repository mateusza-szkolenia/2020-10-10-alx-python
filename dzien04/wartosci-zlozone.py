oferta = [
    { "nazwa" : "ziemniaki", "cena" : 2.0 },
    { "nazwa" : "migdaly", "cena" : 40.00 },
    { "nazwa" : "maka", "cena" : 4.0 },
    { "nazwa" : "ryz", "cena" : 3.5 },
    { "nazwa" : "woda", "cena" : 1.0, "mineraly" : ["Na","Mg","Cl","K"] },
    { "nazwa" : "cytryny", "cena" : 8.0 }
]

print("OFERTA:")
print( oferta )     # wyswietla caly slownik z oferta sklepu

print("OFERTA[1]:")
print( oferta[1] )  # wyswietla caly produkt nr 1 jako slownik (czyli migdaly o cenie 40.00 )

print("OFERTA[1] NAZWA:")
print( oferta[1]['nazwa'] ) # wyswietla tylko nazwe produktu nr 1, czyli string "migdaly"

print("PRZEJSCIE W PETLI FOR PRODUKT IN OFERTA:")
for produkt in oferta:  # przechodzi po wszystkich produktach z oferty...
                           # w tym momencie biezacy produkt jest w zmiennej produkt
    print( produkt )       # ... wyswietlam go (jest to slownik)


print("PRZEJSCIE W PETLI FOR PRODUKT IN OFERTA I WYPISANIE SAMEJ NAZWY:")
for produkt in oferta:  # przechodzi po wszystkich produktach z oferty...
                                    # w tym momencie biezacy produkt jest w zmiennej produkt
    print( produkt['nazwa'] )       # ... i wyswietla tylko nazwe

print("PRZEJSCIE W PETLI FOR PRODUKT IN OFERTA I WYPISANIE PRODUKTOW W LADNY SPOSOB:")
for produkt in oferta:
    print( f"{produkt['nazwa']}: {produkt['cena']}")

print("PRZEJSCIE W PETLI FOR PRODUKT IN OFERTA I WYPISANIE PRODUKTOW W LADNIEJSZY SPOSOB:")
for produkt in oferta:
    print( f"{produkt['nazwa']:20}: {produkt['cena']:5}")


print("PRZEJSCIE W PETLI FOR PRODUKT IN OFERTA I WYPISANIE PRODUKTOW W LADNIEJSZY SPOSOB ORAZ WYPISANIE MINERALOW:")
for produkt in oferta:
    print( f"{produkt['nazwa']:20}: {produkt['cena']:5}")
    if "mineraly" in produkt:
        print(f"^^^^^^^^^^^ ten produkt zawiera mineraly: {produkt['mineraly']}")

print("PRZEJSCIE W PETLI FOR PRODUKT IN OFERTA I WYPISANIE PRODUKTOW W LADNIEJSZY SPOSOB ORAZ WYPISANIE MINERALOW:")
for produkt in oferta:
    print( f"{produkt['nazwa']:20}: {produkt['cena']:5}")
    if "mineraly" in produkt:
        for mineral in produkt['mineraly']:
            print(f"    * {mineral}")

