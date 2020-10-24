print("   ", end="")
for kolumna in range( 10 ):
    print(f"{kolumna:2} ", end="")
print()

for wiersz in range( 10 ):
    print(f"{wiersz}: ", end="")
    for kolumna in range( 10 ):
        print(f"{wiersz*kolumna:2} ", end="")
    print()
