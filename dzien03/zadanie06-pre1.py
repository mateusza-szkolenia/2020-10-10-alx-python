# Mając daną listę liczb, znaleźć najmniejszą z nich

liczby = [ 3, 100, 50, 20, 17, 60, 2, 70, 80, 111, 50, 13 ]

# POPRAWIC:

najwieksza = 0

for biezaca in liczby:
    if biezaca > najwieksza:
        najwieksza = biezaca

# nie chodzi o uzycie max(), tylko o petle for

print( f"Najmniejsza liczba to: {najwieksza}" )




# znaleźć najdłuższe słowo:
# slowa = [ 'kot', 'zolw', 'zyrafa', 'pies', 'jaskolka' ]
