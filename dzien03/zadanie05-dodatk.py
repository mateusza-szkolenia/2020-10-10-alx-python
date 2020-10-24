zakres = 3

szer = len( str( zakres ** 2 ))

print(f"{'':{szer}}  ", end="")
for kolumna in range( 1, zakres + 1 ):
    print(f"{kolumna:{szer}} ", end="")
print()

for wiersz in range( 1, zakres + 1 ):
    print(f"{wiersz:{szer}}: ", end="")

    for kolumna in range( 1, zakres + 1 ):
        print(f"{wiersz*kolumna:{szer}} ", end="")

    print()
