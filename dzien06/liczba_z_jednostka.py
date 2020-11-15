def podziel_lj( napis ):
    liczba = ""
    jednostka = ""
    jeszcze_cyfry = True
    for litera in napis:
        if jeszcze_cyfry and litera in "0123456789.":
            liczba += litera
        else:
            jeszcze_cyfry = False
            if litera != ' ':
                jednostka += litera
    if liczba == "":
        liczba = "0"
    return float(liczba),jednostka

print( podziel_lj( "1234cm" ) )
print( podziel_lj( "1234.55m2" ) )
print( podziel_lj( "1234in3" ) )
print( podziel_lj( "1234" ) )
print( podziel_lj( "x1234" ) )
