# Mając daną listę liczb, znaleźć największą z nich

liczby = [ 1, 3, 100, 50, 20, 17, 60, 70, 80, 111, 50, 13 ]

# ZAIMPLEMENTOWAC

najwieksza = 0

for biezaca in liczby:
    if biezaca > najwieksza:
        najwieksza = biezaca

# nie chodzi o uzycie max(), tylko o petle for

print( f"Największa liczba to: {najwieksza}" )




# znaleźć najdłuższe słowo:
# slowa = [ 'kot', 'zolw', 'zyrafa', 'pies', 'jaskolka' ]
