import random

def los():
    wynik = set()
    while len(wynik) < 6:
        wynik = wynik | set( [ random.randint(1,49) ] )
    return wynik

def los2():
    kulki = list( range( 1, 50 ) )
    random.shuffle( kulki )
    return set( kulki[0:6] )

def los3():
    return set( random.sample( range( 1, 50 ), 6 ) )

def ile_trafien(a, b ):
    return len( a & b )

zwycieskie = los3()
wygrane = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0
}

prawdopodobienstwa = {
    6 : 1 / 13_983_816,
    5 : 1 / 54_201,
    4 : 1 / 1_032,
    3 : 1 / 57,
    2 : 13.2 / 100,
    1 : 41.3 / 100,
    0 : 43.6 / 100
}

N = 100000

for i in range( N ):
    zaklad = los3()
    tr = ile_trafien( zwycieskie, zaklad )
    wygrane[tr] += 1

print( wygrane )

for wygr, licz_trafien in wygrane.items():
    print(f"{wygr} : {licz_trafien:10} {licz_trafien/N*100:10.3f}% {prawdopodobienstwa[wygr]*100:10.3f}%")

