liczby = [ 6, 10, 1, 6, 10, 20, 30, 1, 2 ]

print(f"Przed: {liczby}")

pmax, pmin = 0, 0

for p in range( len(liczby) ):
    if liczby[ p ] < liczby[ pmin ]:
        pmin = p
    if liczby[ p ] > liczby[ pmax ]:
        pmax = p

print(f"pmin={pmin} ==> {liczby[pmin]}")
print(f"pmax={pmax} ==> {liczby[pmax]}")

vmin = liczby[pmin]
vmax = liczby[pmax]

liczby[pmax] = vmin
liczby[pmin] = vmax

print(f"Po: {liczby}")