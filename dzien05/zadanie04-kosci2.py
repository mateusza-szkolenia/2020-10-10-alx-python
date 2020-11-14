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

def symuluj_rzuty( ile_rzutow=10000, ile_kosci=1, ile_scian=6, **kwargs ):
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


konfiguracja = {
    "ile_kosci" : 3,
    "ile_scian" : 6,
    "ile_rzutow" : 50000,
    "xxx" : 11,
    "zxcxczxczxc" : 1231
}

# symuluj_rzuty( konfiguracja['ile_rzutow'], konfiguracja['ile_kosci'], konfiguracja['ile_scian'] )

symuluj_rzuty( **konfiguracja )
