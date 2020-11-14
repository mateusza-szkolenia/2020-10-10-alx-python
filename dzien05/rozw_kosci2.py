#     1: XX   (2)
#     2: XX   (2)
#     3: XXX  (3)
#     4:      (0)
#     5: X    (1)
#     6: XX   (2)
# [ ( 1, 2 ), (2,2), (3,3), (4,0) ]

import random

def rzut():
    return random.randint(1,6)

def wykres( dane ):
    SZER = 50
    najwieksza = max([ wartosc for (klucz, wartosc) in dane ])
    for klucz, wartosc in dane:
        #print( wartosc / najwieksza )
        #print( f"{klucz} {'X' * wartosc :10}")
        print(f"{klucz:5}: {('X' * int( wartosc/najwieksza * SZER) ):{SZER}} ({wartosc})")

def symuluj_rzuty( ile_rzutow=10000, ile_kosci=1, ile_scian=6 ):
    """
    Funkcja rysuje wykres symulowanych wynikow rzutow koscmi.

    :param ile_rzutow: ile razy powtórzyć rzut
    :param ile_kosci: ile kości
    :param ile_scian: ile ścian ma kość
    :return: nic nie zwraca
    """
    rzuty = [ sum([ random.randint(1,ile_scian) for ii in range( ile_kosci ) ]) for i in range( ile_rzutow ) ]
    wyniki = [0] * ( ile_scian * ile_kosci + 1 )
    for wynik in range(1, ile_scian * ile_kosci + 1):
        wyniki[wynik] = len( [ None for r in rzuty if r == wynik ] )
    wykres( list(enumerate(wyniki))[ile_kosci:]  )


symuluj_rzuty( )



