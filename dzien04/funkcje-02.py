# dopisac funkcje liczaca obwod prostokata
# dopisac funkcje liczaca pole kwadratu, ale uzywajaca funkcji pole_prostokata
# dopisac funkcje liczaca obwod kwadratu, j.w.
# dopisac funkcje liczaca przekatne kw i prost.

def pole_prostokata( a, b ):
    return a * b

def obw_prostokata( a, b ):
    return a + a + b + b
#   return 2 * a + 2 * b
#   return 2 * ( a + b )

def pole_kwadratu( bok ):
    return pole_prostokata( bok, bok )

def obw_kwadratu( bok ):
    return obw_prostokata( bok, bok )

def przekatna_prostokata( a, b ):
    return ( a**2 + b**2 )**0.5

def przekatna_kwadratu( bok ):
    return bok * 2**0.5

prostokaty = [
    ( 30, 40 ),
    ( 300, 30 ),
    ( 200, 50 )
]

for p in prostokaty:
    pole = pole_prostokata( p[0], p[1] )
    obw = obw_prostokata( p[0], p[1] )
    przek = przekatna_prostokata( p[0], p[1] )
    print(f"Pole prostokata o wymiarach: {p} wynosi {pole} a obw {obw}  przekatna: {przek}")

for bbb in [ 12, 13 ]:
    print(f"Pole kwadratu o boku {bbb} wynosi {pole_kwadratu(bbb)}  a przekatna: {przekatna_kwadratu(bbb)}")
