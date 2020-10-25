napis = "Ala ma <kota> a nie psa"

poczatek = napis.find("<")
koniec = napis.find(">")

dlugosc = koniec - poczatek - 1

print( f"Dlugosc: {dlugosc} ")
