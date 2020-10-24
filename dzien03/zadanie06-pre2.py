# Mając daną listę liczb, znaleźć najmniejszą i największą z nich

liczby = [ 999, 100, 101, 200, 80, 10, 60 ]

najmniejsza = None
najwieksza = None
poz_najmniejsza = None
poz_najwieksza = None

for p, biezaca in enumerate( liczby ):
    if najmniejsza == None or biezaca < najmniejsza:
        najmniejsza = biezaca
        poz_najmniejsza = p
    if najwieksza == None or biezaca > najwieksza:
        najwieksza = biezaca
        poz_najwieksza = p

print( f"Najmniejsza liczba to: {najmniejsza} (poz: {poz_najmniejsza})" )
print( f"Najwieksza liczba to: {najwieksza} (poz: {poz_najwieksza})" )

for biezaca in liczby:
    print(f"{biezaca}: ", end="")
    if biezaca == najmniejsza:
        print("MIN ", end="")
    if biezaca == najwieksza:
        print("MAX ", end="")
    print()