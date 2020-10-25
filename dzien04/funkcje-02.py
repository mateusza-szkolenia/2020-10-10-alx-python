# dopisac funkcje liczaca obwod prostokata
# dopisac funkcje liczaca pole kwadratu, ale uzywajaca funkcji pole_prostokata
# dopisac funkcje liczaca obwod kwadratu, j.w.
# dopisac funkcje liczaca przekatne kw i prost.

def pole_prostokata( a, b ):
    return a * b

prostokaty = [
    ( 100, 20 ),
    ( 300, 30 ),
    ( 200, 50 )
]

for p in prostokaty:
    pole = pole_prostokata( p[0], p[1] )
    print(f"Pole prostokata o wymiarach: {p} wynosi {pole}")
