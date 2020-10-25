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

prostokaty = [
    ( 100, 20 ),
    ( 300, 30 ),
    ( 200, 50 )
]

for p in prostokaty:
    pole = pole_prostokata( p[0], p[1] )
    obw = obw_prostokata( p[0], p[1] )
    print(f"Pole prostokata o wymiarach: {p} wynosi {pole} a obw {obw}")

for bbb in [ 12, 13 ]:
    print(f"Pole kwadratu o boku {bbb} wynosi {pole_kwadratu(bbb)}")
