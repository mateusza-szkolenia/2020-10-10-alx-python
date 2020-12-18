import random
def rzut():
    return random.randint(1,6)

def wykres( dane ):
    SZER = 50
    najwieksza = max([ wartosc for (klucz, wartosc) in dane ])
    for klucz, wartosc in dane:
        # print( wartosc / najwieksza )
        # print( f"{klucz} {'X' * wartosc :10}")
        # print(f"{klucz:5}: {('X' * wartosc ):50} ({wartosc})")
        print(f"{klucz:5}: {('X' * int( wartosc/najwieksza * SZER) ):{SZER}} ({wartosc})")

def symuluj_rzuty(ile_rzutow = 1000, ile_kosci = 3, ile_scian = 6):
    """
    Symulator rzutow koscmi do gry o zmiennej liczbie scian, rzutów oraz liczby kosci.
    :param ile_rzutow: ile razy rzucic koscia
    :param ile_kosci: ile kostek uzyc
    :param ile_scian: ile scian maja miec kosci
    :return: rysuje wykres
    """
    rzuty = [sum([random.randint(1,ile_scian) for i in range(ile_kosci)]) for x in range(ile_rzutow)]
    wyniki = [0] * (ile_scian * ile_kosci +1 )
    for wynik in range(1, ile_scian * ile_kosci+1):
        wyniki[wynik] = len([r for r in rzuty if r == wynik])
    wykres(list(enumerate(wyniki))[ile_kosci:])

konfiguracja = { "ile_rzutow" : 10000,
                 "ile_kosci" : 5,
                 "ile_scian" : 12}

# symuluj_rzuty(konfiguracja['ilosc_rzutow'], konfiguracja['ile_kosci'], konfiguracja['ile_scian'])
symuluj_rzuty(**konfiguracja)