miastoA = "Warszawa"
miastoB = "Sieradz"
dystans = 220
cenaPaliwa = 4.6
spalanie = 7.8

koszt = dystans * cenaPaliwa * spalanie / 100

print( f"Koszt przejazdu {miastoA}-{miastoB} wynosi {koszt:.2f} PLN." )
print( "Koszt przejazdu " + miastoA + "-" + miastoB + " wynosi " + str(koszt) + " PLN." )
print( "Koszt przejazdu %s-%s wynosi %.2f PLN." % ( miastoA, miastoB, koszt ) )
print( "Koszt przejazdu {}-{} wynosi {} PLN.".format( miastoA, miastoB, koszt ) )
