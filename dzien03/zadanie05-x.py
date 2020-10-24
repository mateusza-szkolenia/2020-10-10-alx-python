print("   ", end="")
for kolumna in range( 10 ):
    print(f"{kolumna:2} ", end="")
print()

for wiersz in range( 10 ):
    print(f"{wiersz}: ", end="")
    for kolumna in range( 10 ):
        wynik = wiersz * kolumna
        if wynik % 3 == 0:
            wynik = 'xx'
        print(f"{wynik:>2} ", end="")
    print()
