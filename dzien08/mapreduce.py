import functools

lista = [ 1, 3, 5, 100, 900, 20, 31, 1 ]

# wyliczenie 7-krotnosci liczb
n = [ 7*x for x in lista ]
print( n )

# stara metoda, uzywajaca map() i lambd:
n = list( map( lambda x : x*7, lista ) )
print( n )

# wyciagniecie elementow wiekszych niz 50
n = [ x for x in lista if x > 50 ]
print( n )

# stara metoda, uzywajaca filter() i lambd:
n = list( filter( lambda x : x > 50, lista ) )
print( n )

# policzenie iloczynu wszystkich liczb
n = functools.reduce( lambda a,b: a*b, lista )
print(n)

# znalezienie maksymalnej wartosci (bez uzycia sort() i max() )
n = functools.reduce( lambda a,b: a if a > b else b, lista )
print(n)