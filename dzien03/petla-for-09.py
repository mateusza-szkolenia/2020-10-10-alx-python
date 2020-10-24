liczby = [ 1, 4, 9, 13, 27 ]

# chcialbym policzyc 3 potegi tych liczb i zapisac te,
# ktorych wartosc modulo 10 jest <= 5
# na osobnej liscie liczby3
#

liczby3 = []

for l in liczby:
    if ( l ** 3 ) % 10 <= 5:
        liczby3.append( l )

print(liczby3)

