#Napisz funkcje zwracajaca zbiór wszystkich znaków wystepujacych w
#napisie wiecej niz zadana liczba razy.
#Przykład uzycia:
#>>> wiecej_niz('ala ma kota a kot ma ale', 3)
#{'a', ' '}

def wiecej_niz( napis, ile ):
    litery = set( napis )
    wynik = set()
    for litera in litery:
        ile2 = napis.count(litera)
#        print( litera, ile2 )
        if ile2 >= ile:
            wynik.add( litera )
    return wynik

def wiecej_niz2( napis, ile ):
    return { l for l in set( napis ) if napis.count(l) > ile }

print( wiecej_niz2( "ala ma kota a kot ma psa", 3 ))