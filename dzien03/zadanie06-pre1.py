# Mając daną listę liczb, znaleźć najmniejszą z nich

liczby = [ 3, 100, 50, 20, 17, 60, 2, 70, 80, 111, 50, 13 ]

# POPRAWIC:

#najmniejsza = 1000
najmniejsza = liczby[0]

for biezaca in liczby:
    if biezaca < najmniejsza:
        najmniejsza = biezaca


print( f"Najmniejsza liczba to: {najmniejsza}" )




# znaleźć najdłuższe słowo:
# slowa = [ 'kot', 'zolw', 'zyrafa', 'pies', 'jaskolka' ]
