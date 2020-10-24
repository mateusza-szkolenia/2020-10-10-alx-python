imiona = [ "Ala", "Ola", "Ula", "Kasia", "Iza", "Magdalena" ]

print(f"Przed: {imiona}")

for n, imie in enumerate( imiona ):
    if len( imie ) <= 3:
        imiona[ n ] = "X " + str( n )

print(f"Po: {imiona}")
