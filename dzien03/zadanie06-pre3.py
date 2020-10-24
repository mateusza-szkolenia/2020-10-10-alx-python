# Mając daną listę liczb, znaleźć najmniejszą i największą z nich

liczby = [ 3, 100, 50, 20, 17, 60, 2, 70, 80, 111, 50, 13 ]

najmniejsza = None
najwieksza = None

for biezaca in liczby:
    if najmniejsza == None:
        najmniejsza = biezaca
    if biezaca < najmniejsza:
        najmniejsza = biezaca
    if najwieksza == None:
        najwieksza = biezaca
    if biezaca > najwieksza:
        najwieksza = biezaca

print( f"Najmniejsza liczba to: {najmniejsza}" )
print( f"Najwieksza liczba to: {najwieksza}" )

# wypisać wszystkie liczby w petli, przy najwiekszej napisac slowo MAX, przy najmniejsze slowo MIN