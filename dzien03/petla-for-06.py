imiona = [ "Ala", "Ola", "Ula", "Kasia", "Iza", "Magdalena" ]

for imie in imiona:
    if len(imie) > 3:
        break

print(f"Pierwsze imie dluzsze niz 3 litery: {imie}")

for i in range( len( imiona ) ):
    if len( imiona[i] ) > 3:
        break

print(f"Pierwsze imie dluzsze niz 3 litery: {imiona[i]} i jest na pozycji {i}")

for x in enumerate( imiona ):
    numer, imie = x
    if len( imie ) > 3:
        break

print(f"Pierwsze imie dluzsze niz 3 litery: {imie} i jest na pozycji {numer}")

for numer, imie in enumerate( imiona ):
    if len( imie ) > 3:
        break

print(f"Pierwsze imie dluzsze niz 3 litery: {imie} i jest na pozycji {numer}")