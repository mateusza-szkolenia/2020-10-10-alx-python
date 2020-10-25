zbior1 = { "a", "b", "c" }
zbior2 = { "a", "e", "d" }

# w przypadku liter mozna i tak:
zbior3 = set("abe")

print(f"zbior1: {zbior1}")
print(f"zbior2: {zbior2}")
print(f"zbior3: {zbior3}")

# suma zbiorow, spodziewany wynik: a b c d e
suma = zbior1 | zbior2
print(f"suma = { suma }")
assert suma == { "a", "b", "c", "d", "e" }

# roznica zbiorow
roznica = zbior1 - zbior2
print( f"roznica = {roznica}" )
assert roznica == { "b", "c" }

# iloczyn (czesc wspolna)
iloczyn = zbior1 & zbior2
print( f"iloczyn (czesc wsp.) = {iloczyn}" )
assert iloczyn == { "a" }

# roznica symetryczna
rs = zbior1 ^ zbior2
print( f"roznica sym = {rs}")
assert rs == { "b", "c", "e", "d" }

